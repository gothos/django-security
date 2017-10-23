from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from is_core.main import UIRESTModelISCore
from is_core.generic_views.inlines.inline_form_views import TabularInlineFormView

from security.models import InputLoggedRequest, OutputLoggedRequest, OutputLoggedRequestRelatedObjects


class InputRequestsLogISCore(UIRESTModelISCore):

    model = InputLoggedRequest
    list_display = (
        'request_timestamp', 'response_timestamp', 'response_time', 'status', 'response_code', 'host', 'short_path',
        'slug', 'ip', 'user__autocomplete_value', 'method', 'type', 'short_response_body', 'short_request_body'
    )

    form_fieldsets = (
        (_('Request'), {'fields': ('request_timestamp', 'host', 'method', 'path', 'queries', 'request_headers',
                                   'request_body', 'is_secure')}),
        (_('Response'), {'fields': ('response_timestamp', 'response_code', 'status', 'response_headers',
                                    'response_body', 'type', 'error_description')}),
        (_('User information'), {'fields': ('user', 'ip')}),
        (_('Extra information'), {'fields': ('response_time',)})
    )

    abstract = True

    create_permission = False
    update_permission = False
    delete_permission = False


class OutputLoggedRequestRelatedObjectsInlineFormView(TabularInlineFormView):

    model = OutputLoggedRequestRelatedObjects
    fields = ('display_object',)


class OutputRequestsLogISCore(UIRESTModelISCore):

    model = OutputLoggedRequest
    list_display = (
        'request_timestamp', 'response_timestamp', 'response_time', 'status', 'response_code', 'host', 'short_path',
        'method', 'slug', 'short_response_body', 'short_request_body'
    )

    form_fieldsets = (
        (_('Request'), {'fields': ('request_timestamp', 'host', 'method', 'path', 'queries', 'request_headers',
                                   'request_body', 'is_secure')}),
        (_('Response'), {'fields': ('response_timestamp', 'response_code', 'status', 'response_headers',
                                    'response_body', 'error_description')}),
        (_('Extra information'), {'fields': ('slug', 'response_time',)}),
        (_('Related objects'), {'inline_view': OutputLoggedRequestRelatedObjectsInlineFormView})
    )

    abstract = True

    create_permission = False
    update_permission = False
    delete_permission = False
