# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import math
import datetime
import serial 
import time
import os
import string



def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))




    
def recogida_datos():
	
	"""Funcion temporizada que te abre un txt que contiene los datos mandados desde arduino, es decir una cadena 
	   que contiene el valor del potenciometro y una letra que indica si el pin de la bombilla esta encendido o apagado"""	
	try:
		datos=open('/home/francisco/Escritorio/datos_bscada.txt','r')
		valores=datos.read()
		datos.close()
	except:
		valores="f500"  		#valor aleatorio si falla la apertura
	
	diccionario = {'valores': 0,'on': 1}		#asignacion inicial del diccionario, no vale de nada ya que despues toma los valores adecuados
	lon_cadena = len(valores)
	
	if lon_cadena>2:
		
		if valores.find("z") == 0:
			diccionario['on'] = 0
		if valores.find("y") == 0:	
			diccionario['on'] = 2
		valores = valores[1:lon_cadena]
		valores = int(valores)
		diccionario['valores'] = valores		

	else:
		diccionario['valores'] = 1500		#Si lee un valor erroneo del txt le damos 1500 para que no se mueva la temperatura_if_
		
	return diccionario
    


def abrir_puerta():
	'''Esta funcion se realiza al pulsar el boton abrir. Abre el txt encargado de mandar datos al arduino y le escribe el dato'''
	try:
		datos=open('/home/francisco/Escritorio/datos_bscada_2.txt','w')
		datos.write("a")
		datos.close()
	except:
		datos = "c"	
	print ("La puerta se abre",datos)
	apertura = 1

	return apertura
	
def cerrar_puerta():
	'''Lo mismo que la anterior pero le manda el dato de cierre'''
	try:
		datos=open('/home/francisco/Escritorio/datos_bscada_2.txt','w')
		datos.write("b")
		datos.close()
	except:
		datos = "c"	
	print ("La puerta se cierra",datos)
	cierre = 1

	return cierre
    

	

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
