from django.contrib import auth
from django.http import HttpResponse


def confirm_account_view(request, key):
    user_model = auth.get_user_model()
    
    user_obj = user_model.objects.get(username=key)
    user_obj.confirmed = True
    user_obj.save()

    return HttpResponse('Confimated')