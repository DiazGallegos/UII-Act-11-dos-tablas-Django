from django.db import models

class Equipo(models.Model):
    POSICIONES_ENTRENADOR = [
        ('DT', 'Director Técnico'),
        ('AC', 'Asistente Técnico'),
        ('PT', 'Preparador Físico'),
        ('MG', 'Manager General'),
    ]
    
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fecha_fundacion = models.DateField()
    entrenador = models.CharField(max_length=100)
    posicion_entrenador = models.CharField(max_length=2, choices=POSICIONES_ENTRENADOR, default='DT')
    siglas = models.CharField(max_length=5, help_text="Ej: FCB, RMA, ATM")
    color_principal = models.CharField(max_length=7, default='#000000', help_text="Código hexadecimal del color")
    escudo = models.ImageField(upload_to='escudos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

class Jugador(models.Model):
    POSICIONES = [
        ('POR', 'Portero'),
        ('DEF', 'Defensa'),
        ('MED', 'Mediocampista'),
        ('DEL', 'Delantero'),
    ]
    
    equipo = models.ForeignKey(
        Equipo, 
        on_delete=models.CASCADE, 
        related_name='jugadores',
        verbose_name="Equipo del jugador"
    )
    nombre_completo = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    posicion = models.CharField(max_length=3, choices=POSICIONES)
    numero_camiseta = models.PositiveIntegerField()
    nacionalidad = models.CharField(max_length=100)
    # ✅ CAMPO DE FOTO AGREGADO
    foto_jugador = models.ImageField(upload_to='fotos_jugadores/', blank=True, null=True, verbose_name="Foto del Jugador")

    def __str__(self):
        return f"{self.nombre_completo} - {self.equipo.siglas}"

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        unique_together = ['equipo', 'numero_camiseta']