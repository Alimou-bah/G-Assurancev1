from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  List_courtier, Statut_courtier, Ajouts, CourtierUpdateView, Supcourtier
urlpatterns = [

    path('listeC/',List_courtier.as_view(), name='liste_courtier' ),
    path('statutC/<int:pk>/',Statut_courtier.as_view(), name='courtier_status' ),
    path('EnregistrerC/',Ajouts, name='ajout_courtier' ),
    path('updateagent/<int:pk>/', CourtierUpdateView.as_view(), name='courtier_update'),
    path('supprimerC/<int:pk>/', Supcourtier.as_view(), name='courtier_supprimer'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)