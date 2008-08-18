from django.conf.urls.defaults import *
urlpatterns = patterns('comfy_django_example.couch_docs.views',
    (r'^doc/(?P<id>\w+)/','detail'),
    (r'^$','index'), 
)
