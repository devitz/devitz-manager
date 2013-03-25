from django.conf.urls import patterns, include, url

from .views import confirm_account_view

urlpatterns = patterns('',
    url(r'^confirm-account/(?P<key>[-\w]+)/$', confirm_account_view, name='attendee_attendee_confirm')
)
