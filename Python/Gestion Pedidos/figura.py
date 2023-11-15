class Figura:
    def __init__(self, nombre_figura, tamaño, precio, cantidad_yeso):
        self.nombre_figura = nombre_figura
        self.tamaño = tamaño
        self.precio = precio
        self.cantidad_yeso = cantidad_yeso

    def __str__(self):        
        return f"Nombre : {self.nombre_figura}, Tamaño : {self.tamaño} cm, Precio : ${self.precio}, Cantidad de yeso : ${self.cantidad_yeso} lb"