from dataclasses import fields
from django.shortcuts import  redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, ListView

from .models import Agent

# Create your views here.
class List_agent(ListView):
    model= Agent
    template_name='agents/wallet.html'
    context_object_name='agents'


class Statut_agent(DetailView):
    model=Agent
    template_name='agents/statut.html'
    context_object_name='agent'

def Ajouts(request):
    context = {}  # Stocker les valeurs du formulaire

    if request.method == "POST":
        context = {
            'Nom': request.POST.get('Nom'),
            'Prenom': request.POST.get('Prenom'),
            'image': request.FILES.get('image'),
            'Agrement': request.POST.get('Agrement'),
            'carte': request.POST.get('carte'),
            'etablissement': request.POST.get('etablissement'),
            'date': request.POST.get('date'),
            'date_expire': request.POST.get('date_expire'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'adresse': request.POST.get('adresse'),
            'statut': request.POST.get('statut'),
        }

        # Assurer que le statut est valide
        if context['statut'] not in ['EN REGLE', 'SUSPENDU', 'RETIRE']:
            context['statut'] = 'EN REGLE'

        # Vérifier les doublons
        if Agent.objects.filter(email=context['email']).exists():
            messages.error(request, "Cet email est déjà utilisé par un autre agent.")
        elif Agent.objects.filter(numero_carte=context['carte']).exists():
            messages.error(request, "Ce numéro de carte est déjà attribué.")
        elif Agent.objects.filter(matricule=context['Agrement']).exists():
            messages.error(request, "Ce numéro d'agrément est déjà enregistré.")
        else:
            # Création de l'agent
            Agent.objects.create(
                Nom=context['Nom'], Prenom=context['Prenom'],
                matricule=context['Agrement'], numero_carte=context['carte'],
                photo_profil=context['image'], etablissement=context['etablissement'],
                date=context['date'], date_expire=context['date_expire'],
                email=context['email'], phone=context['phone'],
                adresse=context['adresse'], statut=context['statut']
            )
            messages.success(request, "L'agent a été ajouté avec succès !")
            return redirect('list_agent')

    return render(request, "agents/ajouts.html", context)



class AgentUpdateView(UpdateView):
    model = Agent
    template_name = 'agents/updateagent.html'
    fields='__all__'
    success_url = reverse_lazy('list_agent')

    
