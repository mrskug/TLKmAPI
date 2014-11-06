from rest_framework import viewsets
from TLKrest.serializers import PersonSerializer
from TLKdb.models import Person


# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer