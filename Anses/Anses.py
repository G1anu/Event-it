import csv
from GestionEventos.Evento import Evento
from GestionUsuarios.Ciudadano import Ciudadano


def escribirCiudadano(ciudadano):
    CiudadanoParaEscribir = ciudadano.ciudadanoAEscribir()
    with open("../Archivos/listaUsuarios.csv","a",newline="") as listaCiudadanos:
        csv_User_writer = csv.writer(listaCiudadanos,delimiter=",")
        csv_User_writer.writerow(CiudadanoParaEscribir)
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
def leerTiposDeEvento(listaTiposEventos):
    with open("../Archivos/tiposDeEventos.csv","r") as tiposDeEventos:
        csv_event_tipe_reader = csv.reader(tiposDeEventos)
        next(tiposDeEventos)
        for line in csv_event_tipe_reader:
            listaTiposEventos.append(line[0])
def escribirEvento(newEvento):
    EventoParaEscribir = newEvento.eventoAEscribir()
    with open("../Archivos/ListaEventos.csv","a",newline="") as listaEventos:
        csv_Event_writer = csv.writer(listaEventos,delimiter=",")
        csv_Event_writer.writerow(EventoParaEscribir)
def leerDataEspecificaEventoparaMapa(lista,valorABuscar):
    with open("../Archivos/ListaEventos.csv","r") as listaEventos:
        csv_Event_reader=csv.reader(listaEventos)
        next(listaEventos)
        for line in csv_Event_reader:
            lista.append(float(line[valorABuscar]))
def leerDataEspecificaEvento(lista,valorABuscar):
    with open("../Archivos/ListaEventos.csv","r") as listaEventos:
        csv_Event_reader=csv.reader(listaEventos)
        next(listaEventos)
        for line in csv_Event_reader:
            lista.append(line[valorABuscar])

def leerDataEspecificaDeAdmin(listaAdmin,valorABuscar):
    with open("../Archivos/listaAdministradores.csv","r") as listaAdministradores:
        csv_admin_reader=csv.reader(listaAdministradores)
        next(listaAdministradores)
        for line in csv_admin_reader:
            listaAdmin.append(line[valorABuscar])
def leerAdministradores(lista):
    with open("../Archivos/listaAdministradores.csv","r") as listaAdmin:
        csv_Admin_reader = csv.reader(listaAdmin)
        next(listaAdmin)
        for line in csv_Admin_reader:
            lista.append(line)
def escribirAdministrador(admin):
    AdminParaEscribir=admin.adminAEscribir()
    with open("../Archivos/listaAdministradores.csv","a",newline="") as listaAdmin:
        csv_Admin_writer = csv.writer(listaAdmin,delimiter=",")
        csv_Admin_writer.writerow(AdminParaEscribir)
def adminCleaner():
    cleaner = open("../Archivos/listaAdministradores.csv","w")
    cleaner.close()
def adminListPlacerAfterClean(lista):
    with open("../Archivos/listaAdministradores.csv","a",newline="")as listaAdmin:
        csv_Admin_writer = csv.writer(listaAdmin,delimiter=",")
        csv_Admin_writer.writerow(["username","contraseña","esABM"])
        indice = 0
        while indice < len(lista):
            csv_Admin_writer.writerow(lista[indice])
            indice = indice + 1

