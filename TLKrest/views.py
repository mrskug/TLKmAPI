from rest_framework import viewsets, permissions
from TLKrest.serializers import *
from TLKdb.models import *

# ViewSets define the view behavior.

# Viewset for listing Persons
class PersonViewSet(viewsets.ModelViewSet):
    """
    List persons in database [Herp][ref]

    [ref]: http://derp.derp.fi/derp
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class CommitteeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer

class OfficialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Official.objects.all()
    serializer_class = OfficialSerializer

class MeritViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Merit.objects.all()
    serializer_class = MeritSerializer

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
    queryset = Person.objects.all()
    serializer_class = PersonAddSerializer

# Viewsets for types
class MemberTypeViewSet(viewsets.ModelViewSet):
    queryset = MemberType.objects.all()
    serializer_class = MemberTypeSerializer

class BoardTypeViewSet(viewsets.ModelViewSet):
    queryset = BoardPosition.objects.all()
    serializer_class = BoardPositionSerializer

class OfficialTypeViewSet(viewsets.ModelViewSet):
    queryset = OfficialType.objects.all()
    serializer_class = OfficialTypeSerializer

class CommitteeTypeViewSet(viewsets.ModelViewSet):
    queryset = CommitteeType.objects.all()
    serializer_class = CommitteeTypeSerializer

class MeritTypeViewSet(viewsets.ModelViewSet):
    queryset = MeritType.objects.all()
    serializer_class = MeritTypeSerializer
