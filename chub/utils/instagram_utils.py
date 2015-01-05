from instagram.client import InstagramAPI
import logging

logger = logging.getLogger(__name__)

def pictures(request, keyword, lat='',long=''):
    access_token = request.session['access_token']

    if not access_token:
        return 'No Access Token'

    try:
        api = InstagramAPI(access_token=access_token)
        media_search = api.media_search(lat="28.632244",lng="77.220724",distance=5000)
        photos = []
        for media in media_search:
            photos.append(media.get_standard_resolution_url())

    except Exception as e:
        logger.exception('chub.utils.instagram_utils: ' + str(e))
        photos = []

    return photos