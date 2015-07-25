from django.conf.urls import url, include
from rest_framework import routers

from TLKrest.views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()


# Types
router.register(r'membertypes', MemberTypeViewSet)
router.register(r'boardtypes', BoardTypeViewSet)
router.register(r'committeetypes', CommitteeTypeViewSet)
router.register(r'officialtypes', OfficialTypeViewSet)
router.register(r'merittypes', MeritTypeViewSet)

# List
router.register(r'persons', PersonViewSet)
router.register(r'members', MemberViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'officials', OfficialViewSet)
router.register(r'committees', CommitteeViewSet)
router.register(r'merits', MeritViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
