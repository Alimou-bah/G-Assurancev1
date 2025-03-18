from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, View
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm
from users.models import User
from .utils.send_emails import send_activation_email


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy('affichage_de_film')


class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_activation_email(user)
        messages.success(
            self.request,
            ("Votre compte compte a ete cree, consulter "
                "votre boite email pour activer votre compte")
        )
        return redirect(self.success_url)


class ActivationUserView(View):
    login_url = reverse_lazy('login')

    def get(self, request, uid, token):
        ident = urlsafe_base64_decode(uid)
        try:
            user = User.objects.get(id=ident)
        except User.DoesNotExist:
            return render(request, 'registration/activation_invalid.html')

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                self.request,
                "Votre compte a ete active. Vous pouvez vous connecter "
            )
            return redirect(self.login_url)
        return render(request, 'registration/activation_invalid.html')


class ProfileUserView(ListView):
    #template_name = 'registration/user_profile.html'
    template_name = 'articles/sidebar.html'
    model = User



class LogoutView(View):
    login_url = reverse_lazy('login')

    def get(self, request):
        logout(request)
        messages.success(
            self.request,
            "Votre compte a ete déconnecté"
        )
        return redirect(self.login_url)


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')  # À ajuster avec le nom de l’URL de profil
    else:
        form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'registration/profile_update.html', {'form': form})
