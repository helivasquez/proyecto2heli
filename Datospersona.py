class Dato:

 def __init__(self, nombre, apellido, nombre_usuario,contrasenia,confirmar_contrasenia,tipo):
    self.nombre = nombre
    self.apellido = apellido
    self.nombre_usuario = nombre_usuario
    self.contrasenia = contrasenia
    self.confirmar_contrasenia = confirmar_contrasenia
    self.tipo = tipo


 def setNombre(self,nombre):
     self.nombre = nombre

 def setApellido(self,apellido):
      self.apellido = apellido

 def setNombre_usuario(self,nombre_usuario):
     self.nombre_usuario = nombre_usuario

 def setContrasenia(self,contrasenia):
     self.contrasenia = contrasenia


 def setConfirmar_contrasenia(self,confirmar_contrasenia):
     self.confirmar_contrasenia = confirmar_contrasenia

 def setTipo(self,tipo):
     self.tipo = tipo


 def getNombre(self):
    return  self.nombre

 def getApellido(self):
    return  self.apellido

 def getNombre_usuario(self):
    return self.nombre_usuario

 def getContrasenia(self):
    return self.contrasenia


 def getConfirmar_contrasenia(self):
    return self.confirmar_contrasenia

 def getTipo(self):
        return self.tipo


