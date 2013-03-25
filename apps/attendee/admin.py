from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf.urls import patterns
from django.template.loader import render_to_string
from django.contrib.auth.admin import UserAdmin
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


    def get_urls(self):
        urls = super(AttendeeUserAdmin, self).get_urls()
        extra_urls = patterns('',
            (r'^send-confirmation-mail/$', self.send_confirmation_mail_view),

        )
        return extra_urls + urls

    def send_confirmation_mail_view(self, request):
        queryset = self.model.objects.filter(confirmed=False, attendee_type__name='Participante')

        email_sent_count = 0

        for user_obj in queryset:
            context = {'user': user_obj}
            subject = render_to_string('attendee/mail/account_confirmation_subject.txt', context)
            message = render_to_string('attendee/mail/account_confirmation_body.html', context)

            if user_obj.email_user(subject, message):
                email_sent_count += 1

        messages.success(request, _('%s email sent' % email_sent_count))

        return HttpResponseRedirect('../')



admin.site.register(Ocupation, OcupationAdmin)
admin.site.register(Attendee, AttendeeUserAdmin)
admin.site.register(AttendeeType, AttendeeTypeAdmin)
admin.site.register(AttendeeListImport, AttendeeListImportAdmin)