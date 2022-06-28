from hashlib import new
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Registros
from AppCoder.forms import GuardarCursos, GuardarRegistros

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def cursos(request):

      return render(request, "AppCoder/cursos.html")

def profesores(request):

      return render(request, "AppCoder/profesores.html")


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")

def saveDB(request):

      if request.method == 'POST':
            mf = GuardarCursos(request.POST)
            print(mf)
            #Validamos el formulario que llega
            if mf.is_valid:
                  inf = mf.cleaned_data
                  print(inf)
                  newCurso = Curso (nombre=inf['nombre'], camada=inf['camada']) #Curso hace referencia a la Clase de models.py
                  newCurso.save()
                  mf = GuardarCursos()
                  return render(request, "AppCoder/saveDB.html", {"mf": mf})#redireccionamos
      else:
            mf = GuardarCursos() #Retornamos un formulario vacío para no genere errores
            
      return render(request, "AppCoder/saveDB.html", {"mf": mf})

def verCursosDB(request):
      #print(request.GET['camada'])
      if request.GET['camada']:#if request.GET['c']:#request.method == 'GET':#request.GET['camada']: #if request.method == 'Get':
           #print(request.method == 'GET')
           #return render(request,"AppCoder/verCursos.html")                  
            camada = request.GET['camada']
            cursos = Curso.objects.filter(camada__icontains=camada)
            #print(camada)
            return render(request, "AppCoder/verCursos.html", {"curso":cursos, "camada":camada})#"id":id, 

      else: 
	      respuesta = "No enviaste datos"
      
      return render(request,"AppCoder/verCursos.html", {"respuesta":respuesta})
      

def Regis(request):



      return render(request, "AppCoder/registros.html")

def saveRegistros(request):

      if request.method == 'POST':
            r = GuardarRegistros(request.POST)
            print(r) 
            if r.is_valid:
                  iR = r.cleaned_data
                  print(iR)
                  newRegis = Registros (sereno=iR['sereno'], planta=iR['planta'], fecha=iR['fecha'], hora=iR['hora'], punto=iR['punto'])
                  newRegis.save()
                  r = GuardarRegistros()
                  return render(request, "AppCoder/saveRegistros.html", {"r": r})#redireccionamos
      else:
            r = GuardarRegistros()
            
      return render(request, "AppCoder/saveRegistros.html", {"r": r})

def verRegistros(request):

      if request.GET["planta"]: #request.method == 'GET': #request.GET["planta"]:
            plt = request.GET['planta']
            print(plt)
            sereno = Registros.objects.filter(sereno__icontains=plt)
            planta = Registros.objects.filter(planta__icontains=plt)
            fecha = Registros.objects.filter(fecha__icontains=plt)
            hora = Registros.objects.filter(hora__icontains=plt)
            punto = Registros.objects.filter(punto__icontains=plt)
            #print(Rgt)
            return render(request, "AppCoder/verRegistros.html", {"sereno":sereno, "planta":planta, "fecha":fecha, "hora":hora, "punto":punto})
      else:
            respuesta = "No enviaste datos"
      return render(request, "AppCoder/verRegistros.html")