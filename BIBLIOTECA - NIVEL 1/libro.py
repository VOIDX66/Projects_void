
# -*- coding: utf-8 -*-

class Libro:
    def __init__(self, titulo=None, autor=None, genero=None, ISBN=None, categoria = None, num_copias=0):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ISBN = ISBN
        self.categoria = categoria
        self.num_copias = num_copias
        if num_copias > 0:
            self.disponible = True
        else:
            self.disponible = False    
            
        
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, ISBN: {self.ISBN}, " \
               f"Categoria: {self.categoria}, Copias Disponibles: {self.num_copias}"

    def getTitulo(self):
        return self.titulo
    def getAutor(self):
        return self.autor
    def getGenero(self):
        return self.genero
    def getISBN(self):
        return self.ISBN
    def getNumCopias(self):
        return self.num_copias
    
    @staticmethod
    def buscarLibro(criterio,valor, libros):
        listaLibs = []
        if criterio == "titulo":
            for libro in libros:
                if libro is not None and libro.getTitulo().lower() == valor.lower():
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
        
        if criterio == "autor":
            for libro in libros:
                if libro is not None and libro.getAutor() == valor:
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
    
    def modificarTitulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def disminuirCopiasDisponibles(self):
        if self.num_copias > 0:
            self.num_copias -= 1
        else:
            self.disponible = False
           
    def aumentarCopiasDisponibles(self):
        if not(self.disponible):
            self.disponible = True
        else:
            self.num_copias += 1                
