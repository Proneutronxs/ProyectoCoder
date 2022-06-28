from django.urls import path

from AppCoder import views


urlpatterns = [   
    path('', views.inicio, name="Inicio"),

    path('cursos', views.cursos, name="Cursos"),
    path('saveDB', views.saveDB, name="guardarCurso"),
    path('verCursosDB', views.verCursosDB, name="verCursos"),

    path('profesores', views.profesores, name="Profesores"),

    path('estudiantes', views.estudiantes, name="Estudiantes"),

    path('entregables', views.entregables, name="Entregables"),

    path('Registros', views.Regis, name="Registros"),
    path('saveRegistros', views.saveRegistros, name="saveRegistros"),
    path('verRegistros/', views.verRegistros, name="verRegistros"),

]

