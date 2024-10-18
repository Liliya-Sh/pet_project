from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from . import forms
from .forms import UserPasswordChangeForm
from .models import User
from .services import sendmail


class RegisterView(CreateView):
    """Регистрация пользователя, отправка запроса верификации на почту"""
    model = User
    form_class = forms.UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('restaurant:home_restaurant')

    def form_valid(self, form):
        if form.is_valid:
            fields = form.save()
            sendmail(
                f'Для верификации почты пройдите по '
                f'ссылке http://127.0.0.1:8005/users/confirm_email/{fields.pk}',
                (fields.email,),
            )
        return super().form_valid(form)


class ConfirmPage(TemplateView):
    """Подтверждение почты"""
    template_name = 'registration/mail_verified.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if User.objects.filter(pk=pk).exists():
            user = User.objects.get(pk=pk)
            user.is_active = True
            user.is_staff = True
            user.save()
        context_data['pk'] = pk
        return context_data


class ProfileView(UpdateView):
    """Просмотреть профиль пользователя"""
    model = User
    form_class = forms.UserProfileForm
    success_url = reverse_lazy('home_restaurant')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного изменения пароля."""
        return reverse_lazy('users:profile')


class UserPasswordChange(PasswordChangeView):
    """Изменить пароль"""
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = 'users/password_change_form.html'
