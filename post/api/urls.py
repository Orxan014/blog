from django.conf.urls import url
from post.api.views import PostListAPIView

app_name='post'

urlpatterns = [
    
    url(r'^index/$',PostListAPIView.as_view() , name='index'),
    #url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    #url(r'^create/$', post_create, name='create'),
    #url(r'^(?P<id>\d+)/update/$', post_update, name='update'),
    #url(r'^(?P<id>\d+)/delete/$', post_delete, name='delete'),

    
]


