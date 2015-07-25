from rest_framework import viewsets, filters

from TLKrest.filters import PersonFilter
from TLKrest.serializers import *
from TLKdb.models import *


# ViewSets define the view behavior.

# Viewset for listing Persons
class PersonViewSet(viewsets.ModelViewSet):
    """
    Lists all persons in database with type in string format

    Usable methods: GET

    Search by appending ?search=searchquery to url

    Valid queries: firstname, lastname, birthplace, city, zip, country, company

    Filter by ?field=value&otherfield=othervalue&foreign__field=value
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    filter_class = PersonFilter
    search_fields = ('firstname', 'lastname',
                     'birthplace', 'city', 'zip',
                     'country', 'company')

class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all members by PK with type in string format

    Usable methods: GET

    Search by appending ?search=<searchquery> to url

    Valid queries: year, typename, lastname
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

class BoardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all board members by PK with type in string format

    Usable methods: GET

    Search by appending ?search=<searchquery> to url

    Valid queries: year, typename, lastname
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

class CommitteeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all committee members by PK with type in string format

    Usable methods: GET

    Search by appending ?search=<searchquery> to url

    Valid queries: year, typename, lastname
    """
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

class OfficialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all officials by PK with type in string format

    Usable methods: GET

    Search by appending ?search=<searchquery> to url

    Valid queries: year, typename, lastname
    """
    queryset = Official.objects.all()
    serializer_class = OfficialSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

class MeritViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all merit awards by PK with type in string format

    Usable methods: GET

    Search by appending ?search=<searchquery> to url

    Valid queries: year, typename, lastname
    """
    queryset = Merit.objects.all()
    serializer_class = MeritSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')


# Viewsets for types
class MemberTypeViewSet(viewsets.ModelViewSet):
    """
    List, add and delete member types

    Usable methods: GET, PUT, UPDATE, DELETE
    """
    queryset = MemberType.objects.all()
    serializer_class = MemberTypeSerializer

class BoardTypeViewSet(viewsets.ModelViewSet):
    """
    List, add and delete board types

    Usable methods: GET, PUT, UPDATE, DELETE
    """

    queryset = BoardPosition.objects.all()
    serializer_class = BoardPositionSerializer

class OfficialTypeViewSet(viewsets.ModelViewSet):
    """
    List, add and delete official types

    Usable methods: GET, PUT, UPDATE, DELETE
    """

    queryset = OfficialType.objects.all()
    serializer_class = OfficialTypeSerializer

class CommitteeTypeViewSet(viewsets.ModelViewSet):
    """
    List, add and delete committee types

    Usable methods: GET, PUT, UPDATE, DELETE
    """

    queryset = CommitteeType.objects.all()
    serializer_class = CommitteeTypeSerializer

class MeritTypeViewSet(viewsets.ModelViewSet):
    """
    List, add and delete merit types

    Usable methods: GET, PUT, UPDATE, DELETE
    """

    queryset = MeritType.objects.all()
    serializer_class = MeritTypeSerializer
