from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


def confirm_account_view(request, key):
    user_model = auth.get_user_model()
    
    user_obj = get_object_or_404(user_model, username=key)
    user_obj.confirmed = True
    user_obj.save()

    return HttpResponseRedirect('http://devitz.com?confirmed=%s' % user_obj.first_name)
