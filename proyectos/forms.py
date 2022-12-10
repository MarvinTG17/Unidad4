from django import forms
    
class FormRegistrarProyecto(forms.Form):
    
    titulo          = forms.CharField(widget=forms.TextInput(
                        attrs={
                            "class": "form-control",
                            "placeholder":"Nombre del proyecto",
                            }))             
    descripcion     = forms.CharField(widget=forms.TextInput(
                        attrs={
                            "class": "form-control",
                            "placeholder":"Descripcion",
                            }))

    imagen          = forms.ImageField()

    url             = forms.URLField(widget=forms.TextInput(
                        attrs={
                            "class": "form-control",
                            "placeholder":"Colocar la URL",
                            }))
    
    tipo_proyecto   = forms.CharField(widget=forms.TextInput(
                        attrs={
                            "class": "form-control",
                            "placeholder":"Tipo proyecto: python, php, html, js",
                            }))

