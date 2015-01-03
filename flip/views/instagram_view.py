from instagram.client import InstagramAPI
from django.http import HttpResponse, HttpResponseRedirect

username = 'ankitagarwal248'
client_id = '7934780455214274b79f582404ebf49f'
client_secret = '44fda5bba030441ca38fdb3fcd3c186f'
redirect_uri = 'http://localhost:8000/insta_oauth_callback/'

unauthenticated_api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)


def insta_home(request):
    try:
        url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
        return HttpResponseRedirect(url)
    except Exception as e:
        return HttpResponse(str(e))


def insta_oauth_callback(request):
    code = request.GET.get("code")
    if not code:
        return HttpResponse('Missing Code')

    access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)

    if not access_token:
        return HttpResponse('Could not get access token')

    api = InstagramAPI(access_token=access_token)
    request.session['access_token'] = access_token

    return HttpResponseRedirect('/search/')

def recent(request):
    content = "<h2>User Recent Media</h2>"
    access_token = request.session['access_token']
    if not access_token:
        return HttpResponse('Missing Access Token')
    try:
        api = InstagramAPI(access_token=access_token)
        recent_media, next = api.user_recent_media()
        photos = []
        for media in recent_media:
            photos.append('<div style="float:left;">')
            if(media.type == 'video'):
                photos.append('<video controls width height="150"><source type="video/mp4" src="%s"/></video>' % (media.get_standard_resolution_url()))
            else:
                photos.append('<img src="%s"/>' % (media.get_low_resolution_url()))
            print media

            photos.append("<br/> <a href='/media_like/%s'>Like</a>  <a href='/media_unlike/%s'>Un-Like</a>  LikesCount=%s</div>" % (media.id, media.id, media.like_count))
        content += ''.join(photos)
    except Exception as e:
        return HttpResponse(str(e))
    return HttpResponse("%s <br/>Remaining API Calls = %s/%s" % (content, api.x_ratelimit_remaining, api.x_ratelimit))


def location_recent_media(request):
    access_token = request.session['access_token']
    content = "<h2>Location Recent Media</h2>"
    if not access_token:
        return HttpResponse('Missing Access Token')
    try:
        api = InstagramAPI(access_token=access_token)
        recent_media, next = api.location_recent_media(location_id=514276)
        photos = []
        for media in recent_media:
            photos.append('<img src="%s"/>' % media.get_standard_resolution_url())
        content += ''.join(photos)
    except Exception as e:
        return HttpResponse(str(e))

    return HttpResponse("%s <br/>Remaining API Calls = %s/%s" % (content, api.x_ratelimit_remaining, api.x_ratelimit))


def media_search(request):
    access_token = request.session['access_token']
    content = "<h2>Media Search</h2>"

    try:
        api = InstagramAPI(access_token=access_token)
        media_search = api.media_search(lat="28.632244",lng="77.220724",distance=5000)
        photos = []
        for media in media_search:
            photos.append('<img src="%s"/>' % media.get_standard_resolution_url())
        content += ''.join(photos)
    except Exception as e:
        HttpResponse(str(e))

    return HttpResponse(content)

def location_search(request):
    access_token = request.session['access_token']
    content = "<h2>Location Search</h2>"
    try:
        api = InstagramAPI(access_token=access_token)
        location_search = api.location_search(lat="28.632244",lng="77.220724",distance=5000)
        locations = []
        for location in location_search:
            locations.append('<li>%s  <a href="https://www.google.com/maps/preview/@%s,%s,19z">Map</a>  </li>' % (location.name,location.point.latitude,location.point.longitude))
        content += ''.join(locations)
    except Exception as e:
        HttpResponse(str(e))

    return HttpResponse(content)