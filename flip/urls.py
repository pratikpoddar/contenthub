from django.conf.urls import patterns, url
from flip import views

urlpatterns = patterns(
        '',
        url(r'^$', views.base.index, name='index'),
        url(r'^register/?$', views.user_account.user_register, name='register'),
        url(r'^login/?$', views.user_account.user_login, name='login'),
        url(r'^logout/?$', views.user_account.user_logout, name='logout'),

        url(r'^insta/?$', views.instagram_view.insta_home, name='insta_home'),
        url(r'^insta_oauth_callback/?$', views.instagram_view.insta_oauth_callback, name='insta_oauth_callback'),
        url(r'^insta/recent/?$', views.instagram_view.recent, name='insta_recent'),
        url(r'^insta/location_recent_media/?$', views.instagram_view.location_recent_media, name='insta_location_recent_media'),
        url(r'^insta/media_search/?$', views.instagram_view.media_search, name='media_search'),
        url(r'^insta/location_search/?$', views.instagram_view.location_search, name='locationm _search'),

        url(r'^search/?$', views.client.search, name='search'),
)
