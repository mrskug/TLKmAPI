from django.conf.urls import url, include
from rest_framework import routers

from TLKrest.views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Add
router.register(r'persons-add', PersonAddViewSet)
router.register(r'members-add', MemberAddViewSet)
router.register(r'boards-add', BoardAddViewSet)
router.register(r'committees-add', CommitteeAddViewSet)
router.register(r'officials-add', OfficialAddViewSet)
router.register(r'merits-add', MeritAddViewSet)

# Types
router.register(r'membertypes', MemberTypeViewSet)

# List
router.register(r'persons', PersonViewSet)
router.register(r'members', MemberViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
