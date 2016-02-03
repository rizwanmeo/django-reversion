from django.conf.urls import patterns

import django_filters
from django_nav import nav_groups
from better_admin.admin import BetterAppAdmin, BetterModelAdmin

from reversion.models import Revision, Version
from reversion.filters import RevisionFilterSet

urlpatterns = patterns(
    '',
)


class RevisionModelAdmin(BetterModelAdmin):
    queryset = Revision.objects.all()
    list_template = 'reversion/revision_list.html'
    create_template = 'reversion/revision_create.html'
    update_template = 'reversion/revision_update.html'
    popup_template = 'reversion/revision_popup.html'
    detail_template = 'reversion/revision_detail.html'
    filter_set = RevisionFilterSet

    def get_request_queryset(self, request):
        qs = super(RevisionModelAdmin,
                   self).get_request_queryset(request)
        if not request.user.is_superuser:
            return Revision.objects.sieve(user=request.user)
        return qs

    def get_import_urls(self):
        return patterns('',)

    def get_export_urls(self):
        return patterns('',)


class VersionModelAdmin(BetterModelAdmin):
    queryset = Version.objects.all()
    list_template = 'reversion/version_list.html'
    create_template = 'reversion/version_create.html'
    update_template = 'reversion/version_update.html'
    popup_template = 'reversion/version_popup.html'
    detail_template = 'reversion/version_detail.html'

    def get_request_queryset(self, request):
        qs = super(VersionModelAdmin,
                   self).get_request_queryset(request)
        if not request.user.is_superuser:
            return Version.objects.sieve(user=request.user)
        return qs

    def get_import_urls(self):
        return patterns('',)

    def get_export_urls(self):
        return patterns('',)


class ReversionAppAdmin(BetterAppAdmin):
    app_name = 'reversion'
    model_admins = {
        'Revision': RevisionModelAdmin(),
        'Version': VersionModelAdmin(),
    }


reversion_app_admin = ReversionAppAdmin()
nav_groups.register(reversion_app_admin.get_nav())
urlpatterns += reversion_app_admin.get_urls()
