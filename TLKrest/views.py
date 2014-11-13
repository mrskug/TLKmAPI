from rest_framework import viewsets
from TLKrest.serializers import EverythingSerializer
from TLKdb.models import *


# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = EverythingSerializer