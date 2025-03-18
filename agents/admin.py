from django.contrib import admin 
from agents.models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display=('Nom', ' Premon','matricule','etablissement', 'date', 'date_ expire')

admin.site.register(Agent)