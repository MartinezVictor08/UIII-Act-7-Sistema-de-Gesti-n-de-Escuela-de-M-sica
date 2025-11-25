
from django.db import models

class EstudianteMusica(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    instrumento_principal = models.CharField(max_length=50)
    nivel_habilidad = models.CharField(max_length=50)
    fecha_inscripcion = models.DateField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ProfesorMusica(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    instrumento_especialidad = models.CharField(max_length=50)
    experiencia_anos = models.IntegerField()
    fecha_contratacion = models.DateField()
    salario_hora = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Instrumento(models.Model):
    id_instrumento = models.AutoField(primary_key=True)
    nombre_instrumento = models.CharField(max_length=100)
    tipo_instrumento = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=100)
    ano_fabricacion = models.IntegerField()
    costo_alquiler_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    estado_disponibilidad = models.BooleanField()
    num_serie = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_instrumento


class ClaseMusica(models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre_clase = models.CharField(max_length=100)
    id_profesor = models.ForeignKey(ProfesorMusica, on_delete=models.CASCADE)
    instrumento_ensenanza = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    duracion_minutos = models.IntegerField()
    horario = models.CharField(max_length=100)
    cupo_maximo = models.IntegerField()
    costo_clase = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_clase = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_clase


class InscripcionClase(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(EstudianteMusica, on_delete=models.CASCADE)
    id_clase = models.ForeignKey(ClaseMusica, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado_inscripcion = models.CharField(max_length=50)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2)
    comentarios_profesor = models.TextField()

    def __str__(self):
        return f"Inscripción {self.id_inscripcion}"


class AlquilerInstrumento(models.Model):
    id_alquiler = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(EstudianteMusica, on_delete=models.CASCADE)
    id_instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    fecha_inicio_alquiler = models.DateField()
    fecha_fin_alquiler = models.DateField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    estado_instrumento_alquiler = models.CharField(max_length=50)
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"Alquiler {self.id_alquiler}"


class PagoMusica(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(EstudianteMusica, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=50)
    id_inscripcion_asociada = models.ForeignKey(InscripcionClase, on_delete=models.CASCADE)
    estado_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago {self.id_pago}"
