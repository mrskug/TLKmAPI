from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from TLKrest.urls import router

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TLKmAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
