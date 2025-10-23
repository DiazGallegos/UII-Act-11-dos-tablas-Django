from django import forms
from .models import Equipo, Jugador

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'ciudad', 'fecha_fundacion', 'entrenador', 
                 'posicion_entrenador', 'siglas', 'color_principal', 'escudo']
        widgets = {
            'fecha_fundacion': forms.DateInput(attrs={'type': 'date'}),
            'color_principal': forms.TextInput(attrs={'type': 'color'}),
        }

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['equipo', 'nombre_completo', 'fecha_nacimiento', 
                 'posicion', 'numero_camiseta', 'nacionalidad', 'foto_jugador']  # ✅ Foto incluida
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'foto_jugador': 'Foto del Jugador (Opcional)',
        }