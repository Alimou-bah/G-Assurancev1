# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from .models import User
from .utils.send_emails import send_activation_email


class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)

        if user is None:
            raise ValidationError("Email ou Mot de passe incorrect.")

        if not user.is_active:
            send_activation_email(user)
            raise ValidationError(
                "Votre compte n'est pas actif, consultez votre boîte email pour l'activer."
            )
        self.user_cache = user
        return self.cleaned_data


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Requis. Entrez une adresse email valide."
    )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cette adresse email existe déjà.")
        return email


