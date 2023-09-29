from django.contrib import admin
from .models import Persona, Parentesco, Matrimonio

#registrar modelos
admin.site.register(Persona)
admin.site.register(Parentesco)
admin.site.register(Matrimonio)