from django_filters import FilterSet
from django_filters import filters

from better_admin.filters import WildCardFilter
from reversion.models import Revision


class RevisionFilterSet(FilterSet):
    comment = WildCardFilter(name='comment')
    created_by = WildCardFilter(name='user__username')

    class Meta:
        model = Revision
        fields = ('manager_slug', 'created_by', 'comment')



