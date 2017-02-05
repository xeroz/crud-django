from django.contrib import admin
from .models import Registrado

# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display  = ["email", "nombre"]
    search_fields = ["email", "nombre"] 

    class Meta:
        model = Registrado

admin.site.register(Registrado, AdminRegistrado)