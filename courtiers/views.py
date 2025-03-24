from django.shortcuts import  redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, ListView
from .models import Courtier

# Create your views here.
class liste_courtier(ListView):
    model=Courtier
    template_name='courtiers/liste.html'
    context_object_name='courtiers'

class Statut_courtier(DetailView):
    model=Courtier
    template_name='courtiers/statut.html'
    context_object_name='courtiers'

def Ajout(request):
    context = {}  # Stocker les valeurs du formulaire

    if request.method == "POST":
        context = {
            'nom': request.POST.get('nom'),
            'prenom': request.POST.get('prenom'),
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
        if Courtier.objects.filter(email=context['email']).exists():
            messages.error(request, "Cet email est déjà utilisé par un autre courtier.")
        elif Courtier.objects.filter(numero_carte=context['carte']).exists():
            messages.error(request, "Ce numéro de carte est déjà attribué.")
        elif Courtier.objects.filter(matricule=context['Agrement']).exists():
            messages.error(request, "Ce numéro d'agrément est déjà enregistré.")
        else:
            # Création de courtier
            Courtier.objects.create(
                nom=context['nom'], prenom=context['prenom'],
                matricule=context['Agrement'], numero_carte=context['carte'],
                photo_profil=context['image'], etablissement=context['etablissement'],
                date=context['date'], date_expire=context['date_expire'],
                email=context['email'], phone=context['phone'],
                adresse=context['adresse'], statut=context['statut']
            )
            messages.success(request, "Courtier  ajouté avec succès !")
            return redirect('liste_courtier')

    return render(request, "courtiers/ajoutcourtier.html", context)


class CourtierUpdateView(UpdateView):
    model = Courtier
    template_name = 'courtiers/updatecourtier.html'
    fields='__all__'
    success_url = reverse_lazy('liste_courtier')


