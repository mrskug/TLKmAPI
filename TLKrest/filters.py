
import django_filters
from TLKdb.models import *

# Filterklass för Person
class PersonFilter(django_filters.FilterSet):

    class Meta:
        model = Person
        fields = ['firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'email', 'joined', 'graduated',
                  'birthplace', 'city', 'zip', 'country', 'company']