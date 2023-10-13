import django_filters
from Apiapp.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model=User
        fields=['task_title']
