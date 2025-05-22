from django.contrib import admin
from controleur.models import Controler

class AgentAdmin(admin.ModelAdmin):
    list_display=('nom', ' premon', 'email')

admin.site.register(Controler)
# Register your models here.
