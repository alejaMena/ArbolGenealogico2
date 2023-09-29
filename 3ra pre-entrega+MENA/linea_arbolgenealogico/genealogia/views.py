from django.shortcuts import render, redirect
from .forms import PersonaForm, ParentescoForm, MatrimonioForm, BusquedaForm
from .models import Persona

def persona_form(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genealogia:persona_form')  # Puedes redirigir a donde necesites
    else:
        form = PersonaForm()
    return render(request, 'genealogia/persona_form.html', {'form': form})

def parentesco_form(request):
    if request.method == 'POST':
        form = ParentescoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genealogia:parentesco_form')  # Puedes redirigir a donde necesites
    else:
        form = ParentescoForm()
    return render(request, 'genealogia/parentesco_form.html', {'form': form})

def matrimonio_form(request):
    if request.method == 'POST':
        form = MatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genealogia:matrimonio_form')  # Puedes redirigir a donde necesites
    else:
        form = MatrimonioForm()
    return render(request, 'genealogia/matrimonio_form.html', {'form': form})

def index(request):
    return render(request, 'genealogia/index.html')  # Asume que tienes una plantilla llamada index.html

#vista de la busqueda

def buscar_persona(request):
    resultado = None

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre_persona']

            # Buscar la persona por nombre
            try:
                persona = Persona.objects.get(nombre=nombre)
                resultado = {
                    'persona': persona,
                    'parentesco': persona.parentesco,
                    'estado_civil': 'Casado' if persona.matrimonio.exists() else 'Soltero'
                }
            except Persona.DoesNotExist:
                resultado = {
                    'persona': nombre,
                    'parentesco': 'Falta registro',
                    'estado_civil': 'Falta registro'
                }
    else:
        form = BusquedaForm()

    return render(request, 'genealogia/buscar_persona.html', {'form': form, 'resultado': resultado})
