from django.urls import path
from . import views

app_name = 'app_futbol'

urlpatterns = [
    # URLs para Equipos
    path('', views.listar_equipos, name='listar_equipos'),
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipo/<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
    path('equipo/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipo/editar/<int:equipo_id>/', views.editar_equipo, name='editar_equipo'),
    path('equipo/borrar/<int:equipo_id>/', views.borrar_equipo, name='borrar_equipo'),
    
    # URLs para Jugadores
    path('jugadores/', views.listar_jugadores, name='listar_jugadores'),
    path('jugador/<int:jugador_id>/', views.detalle_jugador, name='detalle_jugador'),
    path('jugador/crear/', views.crear_jugador, name='crear_jugador'),
    path('jugador/editar/<int:jugador_id>/', views.editar_jugador, name='editar_jugador'),
    path('jugador/borrar/<int:jugador_id>/', views.borrar_jugador, name='borrar_jugador'),
]