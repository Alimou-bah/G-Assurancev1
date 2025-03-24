from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  liste_courtier, Statut_courtier, Ajout, CourtierUpdateView
urlpatterns = [
    path('listeC/', liste_courtier.as_view(), name='liste_courtier'),  # Liste des courtiers
    path('statutC/<int:pk>/', Statut_courtier.as_view(), name='courtier_status'),  # Modifier statut courtier
    path('EnregistrerC/', Ajout, name='register'),  # Ajouter un courtier
    path('updatecourtier/<int:pk>/', CourtierUpdateView.as_view(), name='courtier_update'),  # Modifier un courtier
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)