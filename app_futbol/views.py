from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipo, Jugador
from .forms import EquipoForm, JugadorForm

def listar_equipos(request):
    equipos = Equipo.objects.all().order_by('nombre')
    return render(request, 'listar_equipos.html', {'equipos': equipos})

def listar_jugadores(request):
    jugadores = Jugador.objects.all().order_by('equipo__nombre', 'numero_camiseta')
    return render(request, 'listar_jugadores.html', {'jugadores': jugadores})

# ✅ AÑADIR ESTA FUNCIÓN QUE FALTABA
def detalle_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    return render(request, 'detalle_equipo.html', {'equipo': equipo})

def detalle_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    return render(request, 'detalle_jugador.html', {'jugador': jugador})

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_futbol:listar_equipos')
    else:
        form = EquipoForm()
    return render(request, 'formulario_equipo.html', {'form': form, 'titulo': 'Crear Equipo'})

def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_futbol:listar_jugadores')
    else:
        form = JugadorForm()
    return render(request, 'formulario_jugador.html', {'form': form, 'titulo': 'Crear Jugador'})

def editar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('app_futbol:listar_equipos')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'formulario_equipo.html', {'form': form, 'titulo': 'Editar Equipo'})

def editar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('app_futbol:listar_jugadores')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'formulario_jugador.html', {'form': form, 'titulo': 'Editar Jugador'})

def borrar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('app_futbol:listar_equipos')
    return render(request, 'confirmar_borrar.html', {'objeto': equipo, 'tipo': 'equipo'})

def borrar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    if request.method == 'POST':
        jugador.delete()
        return redirect('app_futbol:listar_jugadores')
    return render(request, 'confirmar_borrar.html', {'objeto': jugador, 'tipo': 'jugador'})