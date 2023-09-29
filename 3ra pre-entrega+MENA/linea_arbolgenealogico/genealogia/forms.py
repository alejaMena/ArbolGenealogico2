from django import forms
from .models import Persona, Parentesco, Matrimonio

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'fecha_nacimiento']  

class ParentescoForm(forms.ModelForm):
    class Meta:
        model = Parentesco
        fields = ['padre', 'hijo']  

class MatrimonioForm(forms.ModelForm):
    class Meta:
        model = Matrimonio
        fields = ['persona1', 'persona2']  

# formulario de busqueda
class BusquedaForm(forms.Form):
    nombre_persona = forms.CharField(label='Nombre de la persona a buscar', max_length=100)
