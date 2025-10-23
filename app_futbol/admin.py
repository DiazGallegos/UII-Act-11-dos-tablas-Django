from django.contrib import admin
from .models import Equipo, Jugador

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'entrenador', 'siglas']
    list_filter = ['ciudad', 'posicion_entrenador']
    search_fields = ['nombre', 'ciudad']

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'equipo', 'posicion', 'numero_camiseta']
    list_filter = ['posicion', 'nacionalidad', 'equipo']
    search_fields = ['nombre_completo', 'equipo__nombre']