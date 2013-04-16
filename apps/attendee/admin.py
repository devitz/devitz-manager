import csv 

from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponse
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
    list_filter = UserAdmin.list_filter + ('confirmed', 'present')
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
            (r'^export-csv/$', self.export_attendee_list_to_csv_view),
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


    def export_attendee_list_to_csv_view(self, request):
        queryset = self.model.objects.all()

        if request.GET:
            queryset = queryset.filter(**request.GET.dict())
        
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment;filename="export.csv"'

        writer = csv.writer(response)

        for attendee_obj in queryset:
            ocupations = " ,".join(attendee_obj.ocupations.values_list('name', flat=True))

            writer.writerow([unicode(attendee_obj.get_full_name()).encode('utf-8'), 
                             attendee_obj.email, 
                             unicode(attendee_obj.institution).encode('utf-8'), 
                             ocupations])

        return response


admin.site.register(Ocupation, OcupationAdmin)
admin.site.register(Attendee, AttendeeUserAdmin)
admin.site.register(AttendeeType, AttendeeTypeAdmin)
admin.site.register(AttendeeListImport, AttendeeListImportAdmin)