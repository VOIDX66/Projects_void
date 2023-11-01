class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
    
    def __str__(self):        
        return f"El usuario: {self.usuario} realizo un prestamo de {self.libro} el dia {self.fecha_prestamo}" \
               f"Fecha prevista de devolucion: {self.fecha_devolucion}"
        
