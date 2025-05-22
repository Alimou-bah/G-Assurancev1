from django import forms
from .models import Controler

class ControlerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Controler
        fields = ['prenom', 'nom', 'email', 'telephone', 'adresse', 'password']

    def save(self, commit=True):
        controler = super().save(commit=False)
        controler.set_password(self.cleaned_data['password'])  # Hash du mot de passe
        if commit:
            controler.save()
        return controler
