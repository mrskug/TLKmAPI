from django.conf.urls import patterns, include, url
from django.contrib import admin

from TLKrest.urls import router

# URL mönster
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
