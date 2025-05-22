# urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path('ajouter/', AuthorCreateView.as_view(), name='ajouter_controler'),
    path('connexion/', connexion_controleur, name='connexion'),
    path('liste/', List_controleur.as_view(), name='list_controler'),
    path('display/', Afichag_message.as_view(), name='display'),
    path('logout/', Deconnexion.as_view(), name='logout'),
]