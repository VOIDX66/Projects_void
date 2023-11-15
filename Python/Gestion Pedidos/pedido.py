class Pedido:
    def __init__(self, nombre, direccion , figuras, celular = None, estado = "pendiente"):
        self.nombre = nombre
        self.direccion = direccion
        self.figuras = figuras
        self.celular = celular
        self.estado = estado
    
    def __str__(self):        
        return f"Nombre : {self.nombre}, Direccion : {self.direccion}, Cantidad de figuras : {len(self.figuras)}"
    
        
    