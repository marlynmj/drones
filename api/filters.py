import django_filters
from api.models import Dron

class DronFilter(django_filters.FilterSet):
    class Meta:
        model = Dron
        fields = ['status']