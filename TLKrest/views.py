from rest_framework import viewsets
from TLKrest.serializers import PersonSerializer
from TLKdb.models import *


# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    """
    Derp Derp Derpity Derp [Herp][ref]

    [ref]: http://derp.derp.fi/derp
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer