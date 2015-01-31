from rest_framework import viewsets
from TLKrest.serializers import *
from TLKdb.models import *


# ViewSets define the view behavior.

# Viewset for listing Persons
class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List persons in database [Herp][ref]

    [ref]: http://derp.derp.fi/derp
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Add Viewsets
class MemberAddViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberAddSerializer

class BoardAddViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardAddSerializer

class CommitteeAddViewSet(viewsets.ModelViewSet):
    queryset = Committee.objects.all()
    serializer_class = CommitteeAddSerializer

class OfficialAddViewSet(viewsets.ModelViewSet):
    queryset = Official.objects.all()
    serializer_class = OfficialAddSerializer

class MeritAddViewSet(viewsets.ModelViewSet):
    queryset = Merit.objects.all()
    serializer_class = MeritAddSerializer

class PersonAddViewSet(viewsets.ModelViewSet):
    """
    List persons in database [Herp][ref]

    [ref]: http://derp.derp.fi/derp
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# Viewsets for types
class MemberTypeViewSet(viewsets.ModelViewSet):
    queryset = MemberType.objects.all()
    serializer_class = MemberTypeSerializer
