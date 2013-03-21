from django.contrib.auth.forms import UserChangeForm

from .models import Attendee


class AttendeeUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Attendee