from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, View
from django.urls import reverse_lazy
from .models import Controler
from .forms import ControlerForm
from django.contrib.auth import logout
from django.contrib import messages

class AuthorCreateView(CreateView):
    model = Controler
    form_class = ControlerForm
    template_name = "controleurs/ajoutControleur.html"
    success_url = reverse_lazy("connexion")

    def form_valid(self, form):
        controler = form.save(commit=False)
        controler.set_password(form.cleaned_data['password'])  # Hash du mot de passe
        controler.save()
        return super().form_valid(form)

def connexion_controleur(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('display')
        else:
            return render(request, 'controleurs/connexion.html', {'error': True})
    return render(request, 'controleurs/connexion.html')

class List_controleur(ListView):
    model = Controler
    template_name = 'controleurs/page.html'
    context_object_name = 'controleurs'

class Afichag_message(ListView):
    model = Controler
    template_name = 'controleurs/confirmation.html'
    context_object_name = 'controleurs'

class Deconnexion(View):
    login_url = reverse_lazy('connexion')

    def get(self, request):
        logout(request)
        messages.success(
            self.request,
            "Votre compte a ete déconnecté"
        )
        return redirect(self.login_url)
