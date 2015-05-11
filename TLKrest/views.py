from rest_framework import viewsets, filters

from TLKrest.filters import PersonFilter
from TLKrest.serializers import *
from TLKdb.models import *


# Vy uppsättningar definierar vyernas betéende.

class PersonViewSet(viewsets.ModelViewSet):
    """
    Förteckning på alla personer i databasen

    Användbara metoder: GET

    Sökning med ?search=sökord

    Giltiga sökfält: firstname, lastname,
     birthplace, city, zip, country, company

    Filtrering med ?fältnamn=värde&främmande__fältnamn=värde
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
    Förteckning på alla medlemmar enligt primärnyckel

    Användbara metoder: GET

    Sökning med ?search=sökord

    Giltiga sökfält: year, typename, lastname

    Filtrering med ?fältnamn=värde&främmande__fältnamn=värde
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

class BoardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Förteckning på alla styrelsemedlemmar enligt primärnyckel

    Användbara metoder: GET

    Sökning med ?search=sökord

    Giltiga sökfält: year, typename, lastname

    Filtrering med ?fältnamn=värde&främmande__fältnamn=värde
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

class CommitteeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Förteckning på alla utskott enligt primärnyckel

    Användbara metoder: GET

    Sökning med ?search=sökord

    Giltiga sökfält: year, typename, lastname

    Filtrering med ?fältnamn=värde&främmande__fältnamn=värde
    """
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

class OfficialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Förteckning på alla funktionärer enligt primärnyckel

    Användbara metoder: GET

    Sökning med ?search=sökord

    Giltiga sökfält: year, typename, lastname

    Filtrering med ?fältnamn=värde&främmande__fältnamn=värde
    """
    queryset = Official.objects.all()
    serializer_class = OfficialSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

class MeritViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Förteckning på alla förtjänsttecken enligt primärnyckel

    Användbara metoder: GET

    Sökning med ?search=sökord

    Giltiga sökfält: year, typename, lastname

    Filtrering med ?fältnamn=värde&främmande__fältnamn=värde
    """
    queryset = Merit.objects.all()
    serializer_class = MeritSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('year', 'type__name', 'person__lastname')

# Vy uppsättningar för tilläggning
class MemberAddViewSet(viewsets.ModelViewSet):
    """
    Lägg till medlemmar med person primärnyckel

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """
    queryset = Member.objects.all()
    serializer_class = MemberAddSerializer

class BoardAddViewSet(viewsets.ModelViewSet):
    """
    Lägg till styrelsemedlemmar med person primärnyckel

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """
    queryset = Board.objects.all()
    serializer_class = BoardAddSerializer

class CommitteeAddViewSet(viewsets.ModelViewSet):
    """
    Lägg till utskott med person primärnyckel

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """
    queryset = Committee.objects.all()
    serializer_class = CommitteeAddSerializer

class OfficialAddViewSet(viewsets.ModelViewSet):
    """
    Lägg till funktionärer med person primärnyckel

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """
    queryset = Official.objects.all()
    serializer_class = OfficialAddSerializer

class MeritAddViewSet(viewsets.ModelViewSet):
    """
    Lägg till förtjänsttecken med person primärnyckel

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """
    queryset = Merit.objects.all()
    serializer_class = MeritAddSerializer

class PersonAddViewSet(viewsets.ModelViewSet):
    """
    Lägg till nya personer i databasen

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """
    queryset = Person.objects.all()
    serializer_class = PersonAddSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    filter_class = PersonFilter

# Viewsets for types
class MemberTypeViewSet(viewsets.ModelViewSet):
    """
    Visa, lägg till och radera medlemstyper

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """
    queryset = MemberType.objects.all()
    serializer_class = MemberTypeSerializer

class BoardTypeViewSet(viewsets.ModelViewSet):
    """
    Visa, lägg till och radera styrelseposter

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """

    queryset = BoardPosition.objects.all()
    serializer_class = BoardPositionSerializer

class OfficialTypeViewSet(viewsets.ModelViewSet):
    """
    Visa, lägg till och radera funktionärsposter

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """

    queryset = OfficialType.objects.all()
    serializer_class = OfficialTypeSerializer

class CommitteeTypeViewSet(viewsets.ModelViewSet):
    """
    Visa, lägg till och radera utskott

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """

    queryset = CommitteeType.objects.all()
    serializer_class = CommitteeTypeSerializer

class MeritTypeViewSet(viewsets.ModelViewSet):
    """
    Visa, lägg till och radera förtjänstteckentyper

    Användbara metoder: GET, PUT, UPDATE, DELETE
    """

    queryset = MeritType.objects.all()
    serializer_class = MeritTypeSerializer
