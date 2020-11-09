from flask import Flask,jsonify,request
from flask_cors import CORS
import json
from Datospersona import Dato
from Canciones import Musica
from Solocancionesagregadas import agregadas
from Guardar_comentario_nombreusuario import Comentary
from Solicitudes import Solicitud
from LlaveMaestro import Master
import Datospersona
import Canciones

app = Flask(__name__)
CORS(app)

Nombres = []
Cancion = []
Solicitudesmusic =[]
maestro = []
Agre = []
GuardarComentarioUsuario = []
contador = 0

Nombres.append(Dato('heli','saul','heli23','123','123','admin'))
Nombres.append(Dato('Usuario','Maestro','admin','admin','admin','admin'))
Nombres.append(Dato('german','gomez','german23','12','12','cliente'))
Nombres.append(Dato('usario','usuario','usuario','usuario','usuario','cliente'))
Nombres.append(Dato('mama','saul','mama12','13','13','cliente'))
Nombres.append(Dato('saul','vasquez','saul23','14','14','cliente'))
#GuardarComentarioUsuario.append(Comentary('','esta canciones bonita','','',''))

maestro.append(Master('Usuario','Maestro','admin','admin'))

#Cancion.append(Musica(0,'vasquez','saul23','14','14','https://image.freepik.com/vector-gratis/casa-dos-pisos_1308-16176.jpg','casa','3'))

#AQUI ES PARA AGREGAR LAS CANCIONES Y RECUPERAR CANCION
@app.route('/agregados', methods = ['POST'] )
def Guardar():

     global Agre


     Mus = request.json['cancion']
     Mus2 = request.json['cancion2']


     nueva_cancion = agregadas(Mus,Mus2)
     Agre.append(nueva_cancion)

     return jsonify({
                'message':'Success',
                'reason':'Se ha agregado '
                    })

@app.route('/c3/<string:n>', methods = ['GET'] )
def c3(n):
    global Agre


    for can  in Agre:
        if can.getMusic() == n:
                  Da = {
                        'cancion': can.getMusic(),
                        'cancion2': can.getMusic2()

                  }
                  break
    respuesta = jsonify(Da)
    return(respuesta)


@app.route('/c4', methods = ['GET'] )
def c4():
    global Agre
    Datos = []
    Da = {}

    for can  in Agre:

                  Da = {
                        'cancion': can.getMusic(),
                        'cancion2': can.getMusic2()

                  }
                  Datos.append(Da)
    respuesta =jsonify(Datos)
    return(respuesta)




#FIN PARA

#LOS METODOS QUE ACONTINUACION SE PRESENTAN SON SOLO PARA LAS SOLICITUDES DE CANCIONES
#LUEGO EL ADMINISTRADOR LOS REVISARA
#POST
@app.route('/Solicitud', methods = ['POST'] )
def Solici():
     global Solicitudesmusic
     nombre = request.json['nombre']
     artista = request.json['artista']
     album = request.json['album']
     fecha = request.json['fecha']
     imagen = request.json['imagen']
     spotify = request.json['spotify']
     youtube = request.json['youtube']
     nueva_cancion = Solicitud(nombre , artista , album , fecha , imagen , spotify , youtube)
     Solicitudesmusic.append(nueva_cancion)
     return jsonify({
                'message':'Success',
                'reason':'Se ha agregado con exito la concion'
                    })

#GET
@app.route('/cc', methods = ['GET'] )
def c7():
    global Solicitudesmusic
    dat1 = []
    Da ={}
    for can  in Solicitudesmusic:
        Da = {
            'nombre': can.getNombre(),
            'artista': can.getArtista(),
            'album': can.getAlbum(),
            'fecha': can.getFecha(),
            'imagen': can.getImagen(),
            'spotify': can.getSpotify(),
            'youtube': can.getYoutube()
           }

        dat1.append(Da)
    respuesta = jsonify(dat1)
    return(respuesta)


#GET PARA ACEPTAR LA SOLICITUD

@app.route('/c8/<string:n>', methods = ['GET'] )
def c8(n):
    global Solicitudesmusic


    for can  in Solicitudesmusic:
        if can.getNombre() == n:
                  Da = {

                        'nombre': can.getNombre(),
                        'artista': can.getArtista(),
                        'album': can.getAlbum(),
                        'fecha': can.getFecha(),
                        'imagen': can.getImagen(),
                        'spotify': can.getSpotify(),
                        'youtube': can.getYoutube()
                  }
                  break
    respuesta = jsonify(Da)
    return(respuesta)

# METODO DELETE

@app.route('/c8/<string:borrar>', methods = ['DELETE'] )
def EliminarCancionsolicitada(borrar):
      global Solicitudesmusic


      for i in range(len(Solicitudesmusic)):
            if borrar == Solicitudesmusic[i].getNombre():
               del Solicitudesmusic[i]
               break

      return jsonify({'message':'se ha eliminado el dato '})







#FIN DE LAS SOLICITUDES











                             #ESTA FUNCION ES PARA MOSTRAR LOS DATOS DE JSON#

@app.route('/Datos', methods = ['GET'] )
def Obtenerdatos():
      global Nombres
      Datos = []
      Dat = {}
      for nombres in Nombres:
            Dat = {"Nombre":nombres.getNombre(),
                   "Apellido":nombres.getApellido(),
                   "Usuario":nombres.getNombre_usuario(),
                   "Contrasenia":nombres.getContrasenia(),
                   "ConfirmarContrasenia":nombres.getConfirmar_contrasenia()}
            Datos.append(Dat)
      respuesta =jsonify(Datos)
      return(respuesta)


@app.route('/D', methods = ['GET'] )
def Ob():
      global Cancion
      Datos = []

      for nombres in Cancion:
            Dat = {'id':nombres.getId(),
                  'nombre':nombres.getMusica(),
                   'artista':nombres.getArtista(),
                   'album':nombres.getAlbum(),
                   'fecha':nombres.getFecha(),
                   'imagen':nombres.getImagen(),
                   'spotify':nombres.getSpotify(),
                   'youtube':nombres.getYoutube()}
            Datos.append(Dat)
      respuesta =jsonify(Datos)
      return(respuesta)




                             #PARA FUNCION INGRESAR DATOS DE LAS PERSONAS#




@app.route('/Datos', methods = ['POST'] )
def Datos():
      global Nombres

      Nombre = request.json['Nombre']
      Apellido = request.json['Apellido']
      Usuario = request.json['Usuario']
      Contrasenia = request.json['Contrasenia']
      ConfirmarContrasenia = request.json['ConfirmarContrasenia']
      Tipo = 'cliente'
      #este es para localizar al usuario
      sielusuariesta = False
      for nombre in Nombres:
          if nombre.getNombre_usuario() == Usuario:
                sielusuariesta = True
                break
      if  sielusuariesta:
             return jsonify({
                       'message':'Failed',
                        'reason':'El usuario que ingresastes ya se encuentra registrado'
                             })
      else:
             nuevo_dato = Dato(Nombre,Apellido,Usuario,Contrasenia,ConfirmarContrasenia,Tipo)
             Nombres.append(nuevo_dato)
             return jsonify({
                     'message':'Success',
                      'reason' :'Se ha registrado exitosamente',
                      'tipo': nombre.getTipo()
                     })



#AQUI ES PARA CREAR DATOS DE ADMINISTRADOR
@app.route('/Datosadmin', methods = ['POST'] )
def Datosadmin():
      global Nombres

      Nombre = request.json['Nombre']
      Apellido = request.json['Apellido']
      Usuario = request.json['Usuario']
      Contrasenia = request.json['Contrasenia']
      ConfirmarContrasenia = request.json['ConfirmarContrasenia']
      Tipo = 'admin'
      #este es para localizar al usuario
      sielusuariesta = False
      for nombre in Nombres:
          if nombre.getNombre_usuario() == Usuario:
                sielusuariesta = True
                break
      if  sielusuariesta:
             return jsonify({
                       'message':'Failed',
                        'reason':'El usuario que ingresastes ya se encuentra registrado'
                             })
      else:
             nuevo_dato = Dato(Nombre,Apellido,Usuario,Contrasenia,ConfirmarContrasenia,Tipo)
             Nombres.append(nuevo_dato)
             return jsonify({
                     'message':'Success',
                      'reason' :'Se ha registrado exitosamente otro Administrador',
                      'tipo': 'admin'
                     })



#FIN PARA DATOS DE ADMINISTRADOR








             #ESTE ES LA FUNCION PARA CONSULTAR DATOS#









@app.route('/Datosper/<string:nombre>', methods = ['GET'] )
def Consultardato(nombre):
      global Nombres



      for nombres in Nombres:
            if nombres.getNombre_usuario() == nombre:

                  Dat = {
                    'Nombre':nombres.getNombre(),
                   'Apellido':nombres.getApellido(),
                   'Usuario':nombres.getNombre_usuario(),
                   'Contrasenia':nombres.getContrasenia(),
                   'ConfirmarContrasenia':nombres.getConfirmar_contrasenia()
                     }

                  break
      respuesta =jsonify(Dat)
      return(respuesta)





                                      #FUNCION PARA MODIFICAR LOS DATOS#

@app.route('/Datos/<string:nombre>', methods = ['PUT'] )
def Actualizardato(nombre):
      global Nombres



      for i in range(len(Nombres)):
            if nombre == Nombres[i].getNombre_usuario():
               Nombres[i].setNombre(request.json['Nombre'])
               Nombres[i].setApellido(request.json['Apellido'])
               Nombres[i].setNombre_usuario(request.json['Usuario'])
               Nombres[i].setContrasenia(request.json['Contrasenia'])
               Nombres[i].setConfirmar_contrasenia(request.json['ConfirmarContrasenia'])
               break

      return jsonify({'message':'se ha actualizado el dato '})




                                     #FUNCION PARA ELIMINAR LOS DATOS#

@app.route('/Datos/<string:nombre>', methods = ['DELETE'] )
def Eliminardato(nombre):
      global Nombres


      for i in range(len(Nombres)):
            if nombre == Nombres[i].getNombre_usuario():
               del Nombres[i]
               break

      return jsonify({'message':'se ha eliminado el dato '})





@app.route('/Entrar', methods = ['POST'] )
def Entrar():
    global Nombres
   # D = {}
    username =  request.json['Usuario']
    password =  request.json['Contrasenia']
    for usuario in Nombres:
         if usuario.getNombre_usuario() == username and usuario.getContrasenia() == password:
               D    =    {
                        'message':'Success',
                        'Usuario' : usuario.getNombre_usuario(),
                        'tipo':usuario.getTipo()
                       }
               break
         else:
               D ={
                        'message':'Failed',
                        'Usuario' : ''

                   }

    respuesta = jsonify(D)
    return (respuesta)


@app.route('/Buscar', methods = ['POST'] )
def Buscar():
    global Nombres
   # D = {}
    username =  request.json['Usuario']

    for usuario in Nombres:
         if usuario.getNombre_usuario() == username:
               D    =    {
                        'message':'Success',
                        'Usuario' : usuario.getNombre_usuario()

                       }
               break
         else:
               D ={
                        'message':'Failed',
                        'Usuario' : ''

                   }

    respuesta = jsonify(D)
    return (respuesta)


@app.route('/Buscar2', methods = ['POST'] )
def Buscar2():
    global Nombres
   # D = {}
    username =  request.json['Usuario']

    for usuario in Nombres:
         if usuario.getNombre_usuario() == username:

               D    =    {
                        'message':'Success',
                        'Usuario' : usuario.getNombre_usuario(),
                        'Contrasenia':usuario.getContrasenia()

                       }

               break
         else:
               D ={
                        'message':'Failed',
                        'Usuario' : ''

                   }

    respuesta = jsonify(D)
    return (respuesta)
    return (Jsonify ({

           'Contrasenia':usuario.getContrasenia()

    }))

'''
AQUI VAN LOS METODOS PARA LAS CANCIONES POST
'''

@app.route('/cancion', methods = ['POST'] )
def GuardarMusica():

     global Cancion, contador

     id = contador
     nombre = request.json['nombre']
     artista = request.json['artista']
     album = request.json['album']
     fecha = request.json['fecha']
     imagen = request.json['imagen']
     spotify = request.json['spotify']
     youtube = request.json['youtube']

     nueva_cancion = Musica(id, nombre , artista , album , fecha , imagen , spotify , youtube)
     Cancion.append(nueva_cancion)
     contador += 1
     return jsonify({
                'message':'Success',
                'reason':'Se ha agregado con exito la concion'
                    })


'''
AQUI VAN LOS METODOS PARA LAS CANCIONES GET
'''
@app.route('/c', methods = ['GET'] )
def c():
    global Cancion,contador
    dat1 = []

    for can  in Cancion:
        Da = {
            'id': can.getId(),
            'nombre': can.getMusica(),
            'artista': can.getArtista(),
            'album': can.getAlbum(),
            'fecha': can.getFecha(),
            'imagen': can.getImagen(),
            'spotify': can.getSpotify(),
            'youtube': can.getYoutube()
           }

        dat1.append(Da)
    respuesta = jsonify(dat1)
    return(respuesta)


#AQUI ES PARA CONSEGUIR EL DATO DE LA CANCIOn DE SOLA UNA CANCION
@app.route('/c2/<string:n>', methods = ['GET'] )
def c2(n):
    global Cancion


    for can  in Cancion:
        if can.getArtista() == n:
                  Da = {
                        'id': can.getId(),
                        'nombre': can.getMusica(),
                        'artista': can.getArtista(),
                        'album': can.getAlbum(),
                        'fecha': can.getFecha(),
                        'imagen': can.getImagen(),
                        'spotify': can.getSpotify(),
                        'youtube': can.getYoutube()
                  }
                  break
    respuesta = jsonify(Da)
    return(respuesta)
#AQUI ES PARA MODIFICAR LOS DATOS DE LAS CANCIONES DE LA TABLA
@app.route('/cancion/<string:nombre>', methods = ['PUT'] )
def Actualizardatocanciontabla(nombre):
      global Cancion



      for i in range(len(Cancion)):
            if nombre == Cancion[i].getArtista():
               Cancion[i].setMusica(request.json['nombre'])
               Cancion[i].setArtista(request.json['artista'])
               Cancion[i].setAlbum(request.json['album'])
               Cancion[i].setFecha(request.json['fecha'])
               Cancion[i].setImagen(request.json['imagen'])
               Cancion[i].setSpotify(request.json['spotify'])
               Cancion[i].setYoutube(request.json['youtube'])
               break

      return jsonify({'message':'se ha actualizado la cancion '})
#AQUI ES PARA ELIMINAR LOS DATOS DE LAS CANCIONES DE LA TABLA

@app.route('/cancion/<string:nombre>', methods = ['DELETE'] )
def Eliminardatocanciontabla(nombre):
      global Cancion


      for i in range(len(Cancion)):
            if nombre == Cancion[i].getArtista():
               del Cancion[i]
               break

      return jsonify({'message':'se ha eliminado la cancion '})




#FIN PARA CONSEGUIR LOS DATOS DE LAS




#QUI ES PARA POSTEAR UN DATO O BSUCAR UN DATO SE LA CANCIN

@app.route('/Buscar3', methods = ['POST'] )
def Buscar3():
    global Cancion
   # D = {}
    nom =  request.json['artista']

    for usuario in Cancion:
         if usuario.getArtista() == nom:
               D    =    {
                        'message':'Success',
                        'artista' : usuario.getArtista()

                       }
               break
         else:
               D ={
                        'message':'Failed',
                        'artista' : ''

                   }

    respuesta = jsonify(D)
    return (respuesta)

###################################

'''
AQUI ES PARA CREAR TODOS LOS DATOS DE MAESTRO
'''
@app.route('/Mast', methods = ['GET'] )
def Mast():
      global maestro
      Datos = []
      Dat = {}
      for maestrito in maestro:
            Dat = {"Nombre":maestrito.getNombre(),
                   "Apellido":maestrito.getApellido(),
                   "Usuario":maestrito.getUsuario(),
                   "Contra":maestrito.getContra()
                  }
            Datos.append(Dat)
      respuesta =jsonify(Datos)
      return(respuesta)




@app.route('/Mast', methods = ['POST'] )
def Mast2():
    global maestro
   # D = {}
    username =  request.json['Usuario']
    password =  request.json['Contra']
    for usuario in maestro:
         if usuario.getUsuario() == username and usuario.getContra() == password:
               D    =    {
                        'message':'Success',
                        'Usuario' : usuario.getUsuario()

                       }
               break
         else:
               D ={
                        'message':'Failed',
                        'Usuario' : ''

                   }

    respuesta = jsonify(D)
    return (respuesta)

'''
AQUI FINALIZAR LOS TODOS LOS DATOS DEL MAESTRO
'''






'''
AUI ES PARA GUARDAR LOS COMENTARIOS Y NOMBRE DE USUARIO Y NOMBRE DE LA CANCION
TAMBIEN TAMBIEN ES PARA TENER LOS DATOS ANTERIORES
'''
@app.route('/comentario', methods = ['POST'] )
def Guardarcomentario():

     global GuardarComentarioUsuario


     nom = request.json['nombrecan']
     comen = request.json['comentario']
     nomcan = request.json['nombreus']
     nomimg = request.json['imagen']
     nomimg1 = request.json['artista']


     nueva_cancion = Comentary(nom,comen,nomcan,nomimg,nomimg1)
     GuardarComentarioUsuario.append(nueva_cancion)

     return jsonify({
                'message':'Success',
                'reason':'Se ha guardado su comentario '
                    })

@app.route('/comentario', methods = ['GET'] )
def comentario():
    global GuardarComentarioUsuario
    Datos = []
    Da = {}

    for can  in GuardarComentarioUsuario:

                  Da = {
                        'nombrecan': can.getNombre(),
                        'comentario': can.getComentario(),
                        'nombreus': can.getCancion(),
                        'imagen': can.getImagen(),
                        'artista': can.getArtista()

                  }
                  Datos.append(Da)
    respuesta =jsonify(Datos)
    return(respuesta)

#AQUI ES PARA CONSEGUIR LOS COMENTARIOS DE LOS USUARIOS


@app.route('/comentario/<string:n>', methods = ['GET'] )
def conseguircomentario(n):
    global GuardarComentarioUsuario


    for can  in GuardarComentarioUsuario:
        if can.getArtista() == n  :
                  Da = {

                        'comentario': can.getComentario(),
                        'nombreus': can.getCancion()

                  }
                  break
        else:
                  Da = {

                        'comentario': ''

                          }
    respuesta = jsonify(Da)
    return(respuesta)

if __name__=='__main__':
    app.run( threaded = True ,host="0.0.0.0",port = 3000,debug = True)




