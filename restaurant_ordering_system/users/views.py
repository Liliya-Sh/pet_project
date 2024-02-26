from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from users import forms
from users.models import User
from users.services import sendmail


class RegisterView(CreateView):  # регистрация, отправка запроса верификации на почту
    model = User
    form_class = forms.UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid:
            fields = form.save()
            sendmail(
                f'Для верификации почты пройдите по ссылке http://127.0.0.1:8000/users/confirm_email/{fields.pk}',
                (fields.email,),
            )
        return super().form_valid(form)


class ConfirmPage(TemplateView):  # подтверждение почты
    template_name = 'registration/mail_verified.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        pk = context_data['pk']
        if User.objects.filter(pk=pk).exists():
            user = User.objects.get(pk=pk)
            user.is_active = True
            user.is_staff = True
            user.save()
        return context_data


class ProfileView(UpdateView):
    model = User
    form_class = forms.UserProfileForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user