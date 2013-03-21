import os

from django.contrib import auth
from django.test import TestCase
from django.core.files import File as DjangoFile


from apps.attendee.models import AttendeeListImport


class AttendeeListUploadTest(TestCase):
    def setUp(self):
        self.user_model = auth.get_user_model()
        self.csv_file = os.path.join(os.path.dirname(__file__), 'files', 'list_file.csv')
        self.attendee_list_obj = AttendeeListImport.objects.create(list_file=DjangoFile(open(self.csv_file), "list_file.csv"))

    def test_attendee_list_import(self):
        self.assertTrue(self.user_model.objects.get(email="gabrielamodenesi@hotmail.com"))