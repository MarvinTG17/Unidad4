from django.urls import path
from proyectos.views import Home,RegistrarProyecto,RegistrarUsuario,cerrar_session,iniciar_sesion

app_name = 'proyectos'

urlpatterns = [
    #path("",index, name="index"),
    path("home/",Home.as_view(), name="home"),
    path('registrarUsuario/',RegistrarUsuario.as_view(), name='registrarUsuario'),
    path("formularioProyecto",RegistrarProyecto.formularioProyecto,name="formularioProyecto"),
    path("guardarProyecto",RegistrarProyecto.guardarProyecto,name="guardarProyecto"),
    path("cerrar_sesion/",cerrar_session, name="cerrar_session"),
    path("iniciar_sesion/",iniciar_sesion, name="iniciar_sesion"),

]