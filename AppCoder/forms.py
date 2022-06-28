from django import forms   


class GuardarCursos(forms.Form):
    #especificamos bien los campos de la DB
    nombre = forms.CharField()
    camada = forms.IntegerField()

class GuardarRegistros(forms.Form):
    sereno = forms.CharField(max_length=50)
    planta = forms.IntegerField()
    fecha = forms.DateField()
    hora = forms.TimeField()
    punto = forms.IntegerField()