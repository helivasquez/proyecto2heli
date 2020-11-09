class Comentary:

    def __init__(self, nombre, comentario,cancion,imagen,artista):
        self.nombre = nombre
        self.comentario = comentario
        self.cancion = cancion
        self.imagen =imagen
        self.artista =artista

    def getNombre(self):
        return self.nombre
    def getComentario(self):
        return self.comentario
    def getCancion(self):
        return self.cancion
    def getImagen(self):
        return self.imagen
    def getArtista(self):
        return self.artista

    def setNombre(self,nombre):
        self.nombre=nombre
    def setComentario(self,comentario):
        self.comentario =comentario
    def setCancion(self,cancion):
        self.cancion= cancion
    def setImagen(self,imagen):
        self.imagen= imagen
    def setArtista(self,artista):
        self.artista= artista
