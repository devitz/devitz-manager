from django.conf.urls import patterns, include, url

from .views import confirm_account_view

urlpatterns = patterns('',
    # Removed to open new accounts creation area
    # url(r'^confirm-account/(?P<key>.*)/$', confirm_account_view, name='attendee_attendee_confirm')
)
