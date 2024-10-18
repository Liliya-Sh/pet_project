from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from .models import User


class UserRegisterForm(auth_forms.UserCreationForm):
    """Форма для регистрации пользователя."""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'address', 'password1', 'password2')


class UserProfileForm(auth_forms.UserChangeForm):
    """Форма для изменения профиля пользователя."""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserPasswordChangeForm(PasswordChangeForm):
    """Форма для изменения пароля пользователя."""

    old_password = forms.CharField(label="Старый пароль",
                                   widget=forms.PasswordInput(
                                       attrs={'class': 'form-input'})
                                   )
    new_password1 = forms.CharField(label="Новый пароль",
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-input'})
                                    )
    new_password2 = forms.CharField(label="Подтверждение пароля",
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-input'})
                                    )

    class Meta:
        """Метаданные для формы изменения пароля."""
        model = get_user_model()
        fields = ['old_password', 'new_password1', 'new_password2']

    def __str__(self):
        """Возвращает строковое представление формы."""
        return "UserPasswordChangeForm"
