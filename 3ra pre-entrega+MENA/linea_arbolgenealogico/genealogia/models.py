from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    # Otras informaciones relevantes

    def __str__(self):
        return self.nombre

class Parentesco(models.Model):
    padre = models.ForeignKey('Persona', related_name='hijos', on_delete=models.CASCADE)
    hijo = models.ForeignKey('Persona', related_name='padres', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.padre.nombre} es padre/madre de {self.hijo.nombre}'

class Matrimonio(models.Model):
    persona1 = models.ForeignKey('Persona', related_name='matrimonios', on_delete=models.CASCADE)
    persona2 = models.ForeignKey('Persona', on_delete=models.CASCADE)

    def __str__(self):
        return f'Matrimonio entre {self.persona1.nombre} y {self.persona2.nombre}'
