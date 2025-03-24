from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  List_agent, Statut_agent, Ajouts, AgentUpdateView
urlpatterns = [
    path('list/', List_agent.as_view(), name='list_agent'),  # Liste des agents
    path('statut/<int:pk>/', Statut_agent.as_view(), name='agent_statuts'),  # Modifier statut agent
    path('Enregistrer/', Ajouts, name='enregistrer'),  # Ajouter un agent
    path('updateagent/<int:pk>/', AgentUpdateView.as_view(), name='agent_update'),  # Modifier un agent

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)