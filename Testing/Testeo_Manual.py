from GestionUsuarios.Ciudadano import Ciudadano
from Anses.Anses import escribirCiudadano
from Anses.Anses import leerCiudadano


#esto lo usamos para testear por el camino que los metodos funcionaran
ciudadano1 = Ciudadano(23440529259,1154885993)
ciudadano2 = Ciudadano(93390545674,1188549359)
#escribirCiudadano(ciudadano1)
#escribirCiudadano(ciudadano2)
listaUsuarios = []
leerCiudadano(listaUsuarios)
print(listaUsuarios)
listaYo= listaUsuarios[0]
print(listaYo)
