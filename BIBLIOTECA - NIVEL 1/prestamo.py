import datetime #pip install datetime
from dateutil.relativedelta import * #pip install python-dateutil

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
    
    def __str__(self):        
        return f"El usuario: {self.usuario.getNombre()} realizo un prestamo de {self.libro.getTitulo()} de {self.libro.getAutor()}" \
               f" el dia {self.fecha_prestamo} Fecha prevista de devolucion: {self.fecha_devolucion}"
    
    @staticmethod
    def buscarPrestamos(documento, prestamos):
        listaPrestamos = []
        for prestamo in prestamos:
            if prestamo.usuario.getIdentificacion() == documento:
                listaPrestamos.append(prestamo)
        return listaPrestamos
           
    def devolucion(self, prestamos):
        for i in range(len(prestamos)):
            if prestamos[i] == self:
                prestamos[i] = None
                break
            
    def calcularMulta(self):
        diferencia = relativedelta(self.fecha_prestamo,self.fecha_devolucion).days
        if diferencia < 0:
            return (-500*diferencia)
        else:
            None
        
