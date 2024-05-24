from django.contrib import admin
from .models import Syndrome

# Register your models here.
@admin.register(Syndrome)
class SyndromeAdmin(admin.ModelAdmin):
    list_display=('id','code_envoyé','code_reçu','valeur_syndrome','état')

