from django.shortcuts import render, redirect
from almacen.models import Tareas

def listar(request):
    tareas = Tareas.objects.all()
    return render(request, 'listar.html', {"tareas": tareas})

def crear(request):
    tarea = Tareas(title=request.POST['title'], description=request.POST['description'])
    tarea.save()
    return redirect('/almacen/')

def eliminar(request, id):
    tareas = Tareas.objects.get(id=id)
    tareas.delete()
    return redirect('/almacen/')