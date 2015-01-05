from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url('', include('chub.urls')),

    # url(r'^$', 'chub_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

