from rest_framework import routers

from TLKrest.views import *

# Routrar gör det enkelt att automatiskt definiera URLar.
router = routers.DefaultRouter()

# Lägga till
router.register(r'persons/add', PersonAddViewSet, base_name='persons')
router.register(r'members/add', MemberAddViewSet, base_name='members')
router.register(r'boards/add', BoardAddViewSet, base_name='boards')
router.register(r'committees/add', CommitteeAddViewSet, base_name='committees')
router.register(r'officials/add', OfficialAddViewSet, base_name='officials')
router.register(r'merits/add', MeritAddViewSet, base_name='merits')

# Typer
router.register(r'membertypes', MemberTypeViewSet)
router.register(r'boardtypes', BoardTypeViewSet)
router.register(r'committeetypes', CommitteeTypeViewSet)
router.register(r'officialtypes', OfficialTypeViewSet)
router.register(r'merittypes', MeritTypeViewSet)

# Listningar
router.register(r'persons', PersonViewSet)
router.register(r'members', MemberViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'officials', OfficialViewSet)
router.register(r'committees', CommitteeViewSet)
router.register(r'merits', MeritViewSet)

