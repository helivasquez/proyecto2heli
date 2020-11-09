class Master:


   def __init__(self, Nombre, Apellido, Usuario,Contra):
    self.Nombre = Nombre
    self.Apellido = Apellido
    self.Usuario = Usuario
    self.Contra = Contra

   def getNombre(self):
       return self.Nombre
   def getApellido(self):
       return self.Apellido
   def getUsuario(self):
       return self.Usuario
   def getContra(self):
       return self.Contra

   def setNombre(self,Nombre):
       self.Nombre = Nombre
   def setApellido(self,Apellido):
       self.Apellido=Apellido
   def setUsuario(self,Usuario):
       self.Usuario = Usuario
   def setContra(self,Contra):
       self.Contra=Contra