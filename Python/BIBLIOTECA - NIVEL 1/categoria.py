class Categoria:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
        self.subcategorias = []
    
    def __str__(self):        
        return self.nombre
    
    def obtener_subcategorias(self):
        return self.subcategorias
    
    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)
        
    def cantidad_de_subcategoria(self):
        return len(self.subcategorias)
    