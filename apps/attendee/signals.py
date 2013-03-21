import os
import csv
import random
import string

from django.db import models
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist


def get_random_string(number_of_chars):
    return "".join(random.choice(string.ascii_letters + string.digits + "[]") for x in range(number_of_chars))


def import_attendee_from_list(sender, instance, created, raw, using, update_fields, signal, **kwargs):
    from .models import Ocupation
    from .models import AttendeeType

    user_model = auth.get_user_model()
    list_file_path = instance.list_file.path

    if created and os.path.splitext(list_file_path)[1] == '.csv':
        with open(instance.list_file.path, 'r') as list_file:
            next(list_file)
            
            csv_fieldnames = ['timestamp', 'name', 'email', 'institution', 'ocupation']
            csv_dict = csv.DictReader(list_file, fieldnames=csv_fieldnames)
            
            for csv_line in csv_dict:
                fullname_list = csv_line['name'].split()
                first_name, last_name = fullname_list[0], " ".join(fullname_list[1:])
                username = get_random_string(12)
                password = get_random_string(8)

                try:
                    user_model.objects.get(email=csv_line['email'])
                except ObjectDoesNotExist:
                    user_obj = user_model.objects.create_user(username, csv_line['email'], password)
                    user_obj.first_name = first_name
                    user_obj.last_name = last_name
                    user_obj.institution = csv_line['institution']
                    user_obj.attendee_type, created = AttendeeType.objects.get_or_create(name='Participante')

                    user_obj.save()

                    for ocupation in csv_line['ocupation'].split(', '):
                        ocupation_obj, created = Ocupation.objects.get_or_create(name=ocupation)
                        user_obj.ocupations.add(ocupation_obj)
