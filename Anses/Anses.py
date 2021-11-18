import csv
from GestionEventos.Evento import Evento
from GestionUsuarios.Ciudadano import Ciudadano

def escribirCiudadano(ciudadano):
    CiudadanoAEscribir=ciudadano.ciudadanoAEscribir()
    with open("../Archivos/listaUsuarios.csv","a",newline="") as listaCiudadanos:
        csv_User_writer = csv.writer(listaCiudadanos,delimiter=",")
        csv_User_writer.writerow(CiudadanoAEscribir)
def leerCiudadano(listaUsuarios):
    with open("../Archivos/listaUsuarios.csv","r") as listaCiudadanos:
        csv_User_Reader=csv.reader(listaCiudadanos)
        next(listaCiudadanos)
        for line in csv_User_Reader:
            listaUsuarios.append(line)
def leerDataEspecificaDeCiudadano(listaUsuarios,valorABuscar):
    with open("../Archivos/listaUsuarios.csv","r") as listaCiudadanos:
        csv_User_Reader=csv.reader(listaCiudadanos)
        next(listaCiudadanos)
        for line in csv_User_Reader:
            listaUsuarios.append(line[valorABuscar])

def leerCuilsDelAnses(listaCuils):
    with open("../Archivos/CUIL.csv","r") as ansesCUILs:
        csv_CUILs_reader = csv.reader(ansesCUILs)
        next(ansesCUILs)
        for line in csv_CUILs_reader:
            listaCuils.append(line[0])

def escribirTipoDeEvento(tipoDeEvento):
    with open("../Archivos/tiposDeEventos.csv","a",newline="") as listaTipos:
        csv_event_tipe_writer = csv.writer(listaTipos,delimiter=",")
        csv_event_tipe_writer.writerow([tipoDeEvento])
def leerDataEspecificaDeAdmin(listaAdmin,valorABuscar):
    with open("../Archivos/listaAdministradores.csv","r") as listaAdministradores:
        csv_admin_reader=csv.reader(listaAdministradores)
        next(listaAdministradores)
        for line in csv_admin_reader:
            listaAdmin.append(line[valorABuscar])
def leerTiposDeEvento(listaTiposEventos):
    with open("../Archivos/tiposDeEventos.csv","r") as tiposDeEventos:
        csv_event_tipe_reader = csv.reader(tiposDeEventos)
        next(tiposDeEventos)
        for line in csv_event_tipe_reader:
            listaTiposEventos.append(line[0])