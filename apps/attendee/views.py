from django.contrib import auth
from django.views.generic import TemplateView


class ConfirmAccountView(TemplateView):
    user_obj = auth.get_user_model().objects.none()
    template_name = 'attendee/attendee_account_confirmated.html'

    def get_context_data(self, **kwargs):
        context_data = super(ConfirmAccountView, self).get_context_data(**kwargs)

        context_data.update({
            'user': self.get_user_obj(),
        })

        return context_data

    def get_user_obj(self):
        if not self.user_obj:
            user_model = auth.get_user_model()
            self.user_obj = user_model.objects.get(username=self.kwargs['key'])

        return self.user_obj


    def confirm_account(self):
        user_obj = self.get_user_obj()        
        user_obj.confirmed = True
        user_obj.save()

    def get(self, request, *args, **kwargs):
        
        self.confirm_account()

        return super(ConfirmAccountView, self).get(request, *args, **kwargs)