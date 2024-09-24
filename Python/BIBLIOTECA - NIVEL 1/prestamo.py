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
    def buscarPrestamos(usuario, prestamos):
        listaPrestamos = []
        for prestamo in prestamos:
            if prestamo.usuario == usuario:
                listaPrestamos.append(prestamo)
        return listaPrestamos    
           
    def devolucion(self, prestamos):
        for i in range(len(prestamos)):
            if prestamos[i] == self:
                prestamos.pop(i)
                break
            
    def calcularMulta(self):
        diferencia = relativedelta(self.fecha_devolucion,self.fecha_prestamo).days
        if diferencia < 0:
            return (-500*diferencia)
        else:
            return 0
        
    @staticmethod      
    def consultarMultas(usuario, prestamos):
        encontro_multa = False
        for prestamo in prestamos:
            if prestamo.calcularMulta() > 0 and prestamo.usuario == usuario:
                return True
        return encontro_multa

        
