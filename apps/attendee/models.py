from django.db import models
from django.core import urlresolvers
from django.core.mail import EmailMessage
from django.contrib.sites.models import Site
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .signals import import_attendee_from_list

class BaseModel(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        ordering = ('-timestamp', )


class AttendeeListImport(BaseModel):
    list_file = models.FileField(_('list file'), upload_to='attendee/list_import/')
    confirmed = models.BooleanField(_('confirmed'))
    present = models.BooleanField(_('present'))


    class Meta:
        verbose_name = _('attendee list import')
        verbose_name_plural = _('attendee list imports')

    def __unicode__(self):
        return _('attendee list #%s' % self.id)


class Ocupation(BaseModel):
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name = _('ocupation')
        verbose_name_plural = _('ocupation')

    def __unicode__(self):
        return unicode(self.name)


class AttendeeType(BaseModel):
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name = _('attendee type')
        verbose_name_plural = _('attendee type')

    def __unicode__(self):
        return unicode(self.name)


class Attendee(AbstractUser):
    attendee_type = models.ForeignKey(AttendeeType, verbose_name=_('attendee type'), null=True)
    institution = models.CharField(_('institution'), max_length=255)
    ocupations = models.ManyToManyField(Ocupation, verbose_name=_('ocupations'), null=True)
    confirmed = models.BooleanField(_('confirmed'))
    present = models.BooleanField(_('present'))

    def email_user(self, subject, message, from_email=None):
        msg = EmailMessage(subject, message, from_email, [self.email])
        msg.content_subtype = "html"
        return msg.send()

    def get_confirmation_url(self):
        site = Site.objects.get_current()
        return "http://in.devitz.com/confirm-account/%s/" % self.username


models.signals.post_save.connect(import_attendee_from_list, sender=AttendeeListImport)