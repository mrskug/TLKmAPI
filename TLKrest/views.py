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

# Add Viewsets
class MemberAddViewSet(viewsets.ModelViewSet):
    """
    List and add members by person pk

    Usable methods: GET, PUT, UPDATE, DELETE
    """
    queryset = Member.objects.all()
    serializer_class = MemberAddSerializer

class BoardAddViewSet(viewsets.ModelViewSet):
    """
    List and add board members by person pk

    Usable methods: GET, PUT, UPDATE, DELETE
    """
    queryset = Board.objects.all()
    serializer_class = BoardAddSerializer

class CommitteeAddViewSet(viewsets.ModelViewSet):
    """
    List and add committee members by person pk

    Usable methods: GET, PUT, UPDATE, DELETE
    """
    queryset = Committee.objects.all()
    serializer_class = CommitteeAddSerializer

class OfficialAddViewSet(viewsets.ModelViewSet):
    """
    List and add officials by person pk

    Usable methods: GET, PUT, UPDATE, DELETE
    """
    queryset = Official.objects.all()
    serializer_class = OfficialAddSerializer

class MeritAddViewSet(viewsets.ModelViewSet):
    """
    List and add merits by person pk

    Usable methods: GET, PUT, UPDATE, DELETE
    """
    queryset = Merit.objects.all()
    serializer_class = MeritAddSerializer

class PersonAddViewSet(viewsets.ModelViewSet):
    """
    Add new persons to database

    Usable methods: GET, PUT, UPDATE, DELETE
    """
    queryset = Person.objects.all()
    serializer_class = PersonAddSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    filter_class = PersonFilter

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
