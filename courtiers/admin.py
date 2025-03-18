from django.contrib import admin 
from courtiers.models import Courtier

class AgentAdmin(admin.ModelAdmin):
    list_display=('nom', ' premon','matricule','etablissement', 'date', 'date_ expire')

admin.site.register(Courtier)