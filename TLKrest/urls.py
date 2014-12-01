from django.conf.urls import url, include
from rest_framework import routers

from TLKrest.views import PersonViewSet, MemberViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'members', MemberViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]