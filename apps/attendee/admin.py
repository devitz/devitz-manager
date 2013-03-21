from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _

from .forms  import AttendeeUserChangeForm
from .models import Ocupation
from .models import Attendee
from .models import AttendeeType
from .models import AttendeeListImport


class AttendeeListImportAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'list_file')


class OcupationAdmin(admin.ModelAdmin):
    list_display = ('name', )


class AttendeeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )


class AttendeeUserAdmin(UserAdmin):
    form = AttendeeUserChangeForm
    list_display = UserAdmin.list_display + ('attendee_type', 'confirmed', 'present')
    list_editable = UserAdmin.list_editable + ('confirmed', 'present')
    fieldsets = UserAdmin.fieldsets + (
                    (_('Attendee Informations'), {'fields': ('attendee_type',
                                                             'institution',
                                                             'ocupations',
                                                             'confirmed',
                                                             'present')}
                    ),
                )


admin.site.register(Ocupation, OcupationAdmin)
admin.site.register(Attendee, AttendeeUserAdmin)
admin.site.register(AttendeeType, AttendeeTypeAdmin)
admin.site.register(AttendeeListImport, AttendeeListImportAdmin)