from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  List_agent, Statut_agent, Ajouts, AgentUpdateView, Supagent
urlpatterns = [

    path('list/',List_agent.as_view(), name='list_agent' ),
    path('statut/<int:pk>/',Statut_agent.as_view(), name='agent_statuts' ),
    path('Enregistrer/',Ajouts, name='enregistrer' ),
    path('updateagent/<int:pk>/', AgentUpdateView.as_view(), name='agent_update'),
    # path('supprimer/<int:pk>/', Supagent.as_view(), name='agent_supprimer'),
     path('agents/supprimer/<int:pk>/', Supagent.as_view(), name='agent_supprimer'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)