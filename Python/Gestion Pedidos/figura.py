class Figura:
    def __init__(self, nombre_figura, tamaño, precio, cantidad_yeso, cantidad_unidades):
        self.nombre_figura = nombre_figura
        self.tamaño = tamaño
        self.precio = precio
        self.cantidad_yeso = cantidad_yeso
        self.cantidad_unidades = cantidad_unidades

    def __str__(self):        
        return f"Nombre : {self.nombre_figura}, Tamaño : {self.tamaño} cm, Precio : ${self.precio}, Cantidad de yeso : {self.cantidad_yeso} lb, Unidades Pedidas: {self.cantidad_unidades}"
    
    def obtener_precio(self):
        return str(int(self.precio)*int(self.cantidad_unidades))
    
    def modificar_figura(self, nombre_figura, tamaño, precio, cantidad_yeso, cantidad_unidades):
        self.nombre_figura = nombre_figura
        self.tamaño = tamaño
        self.precio = precio
        self.cantidad_yeso = cantidad_yeso
        self.cantidad_unidades = cantidad_unidades