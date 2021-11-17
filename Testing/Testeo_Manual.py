from GestionUsuarios.Ciudadano import Ciudadano
from Anses.Anses import escribirCiudadano
from Anses.Anses import leerCiudadano
from Anses.Anses import leerCuilsDelAnses
from Anses.Anses import leerDataEspecificaDeCiudadano


#esto lo usamos para testear por el camino que los metodos funcionaran
ciudadano1 = Ciudadano(23440529259,1154885993)
ciudadano2 = Ciudadano(13903989504,1188549359)
#escribirCiudadano(ciudadano1)
#escribirCiudadano(ciudadano2)
listaUsuarios = []
leerCiudadano(listaUsuarios)
print(listaUsuarios)
listaYo= listaUsuarios[0]
print(listaYo)
listaCUILMembrillero= []
leerCuilsDelAnses(listaCUILMembrillero)
print(listaCUILMembrillero)
listaCUILMacumbero = []
leerDataEspecificaDeCiudadano(listaCUILMacumbero,0)
print(listaCUILMacumbero)


