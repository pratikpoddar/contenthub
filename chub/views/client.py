from chub.utils import instagram_utils
from django.http import HttpResponse, HttpResponseRedirect


def search(request):
    user = request.user

    tweets = []
    articles = []
    pictures = []
    videos = []

    keyword = requests.GET.get('keyword')
    if keyword:
        pictures = instagram_utils.pictures(request=request, keyword=keyword)
        if pictures == 'No Access Token':
            return HttpResponseRedirect('/insta/')

    context = {
        'tweets': tweets,
        'articles': articles,
        'pictures': pictures,
        'videos': videos,
    }

    return render(request, 'chub/search.html', context)