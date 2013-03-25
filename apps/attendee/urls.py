from django.conf.urls import patterns, include, url

from .views import ConfirmAccountView

urlpatterns = patterns('',
    url(r'^confirm-account/(?P<key>[-\w]+)/$', ConfirmAccountView.as_view(), name='attendee_attendee_confirm')
)
