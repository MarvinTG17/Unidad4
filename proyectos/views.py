from django.shortcuts import render,redirect
from django.views.generic import ListView,View
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from .models import Proyecto
from .forms import FormRegistrarProyecto

def index(request):
    return render(request,"index.html",None)

class Home(ListView):
    model = Proyecto
    template_name = "home.html"
    context_object_name = 'proyecto'

class RegistrarProyecto(HttpRequest):

    def formularioProyecto(request):
        forms = FormRegistrarProyecto()
        return render(request,"registrarProyecto.html",{"form":forms})
    
    def guardarProyecto(request):
        if request.method == "POST":
            formProyecto = FormRegistrarProyecto(request.POST,request.FILES)
            proyecto = Proyecto()
            if formProyecto.is_valid():
                proyecto.titulo         =request.POST.get("titulo")
                proyecto.descripcion    =request.POST.get("descripcion")
                proyecto.imagen         =request.FILES.get("imagen")
                proyecto.url            =request.POST.get("url")   
                proyecto.tipo_proyecto  =request.POST.get("tipo_proyecto")
                proyecto.save()
                forms = FormRegistrarProyecto()
                return render(request,"registrarProyecto.html",{"mensaje":"OK","form":forms})
            else:
                print("El formulario no es valido")
            
class RegistrarUsuario(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request,"registrar.html",{"form":form})

    def post(self,request):
        form=UserCreationForm(request.POST)
        print(form.errors)
        print(form.is_valid())

        if form.is_valid():

            usuario = form.save()

            login(request, usuario)

        return redirect("proyectos:home")
        #return render(request,"home.html",{})

def cerrar_session(request):
    logout(request)
    return redirect("proyectos:home")
    

def iniciar_sesion(request):
    if request.method=="POST":
        form1=AuthenticationForm(request,data=request.POST)
        
        if form1.is_valid():
            usuario=form1.cleaned_data.get("username")
            clave=form1.cleaned_data.get("password")

            user = authenticate(username=usuario,password=clave)

            if user is not None:
                login(request,user)
                return redirect("proyectos:home")
            else:
                messages.error(request,"Usuario no registrado.")
        else:
            messages.error(request,"Informacion incorrecta.")

    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})



