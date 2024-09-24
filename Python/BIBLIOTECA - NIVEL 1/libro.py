
# -*- coding: utf-8 -*-

class Libro:
    def __init__(self, titulo=None, autor=None, genero=None, ISBN=None, categoria = None, num_copias=0):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ISBN = ISBN
        self.categoria = categoria
        self.num_copias = int(num_copias)
        if int(num_copias) > 0:
            self.disponibilidad = True
        else:
            self.disponibilidad = False    
            
        
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
    def getDisponibilidad(self):
        return self.disponibilidad
    
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
                if libro is not None and libro.getAutor().lower() == valor.lower():
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
        
        if criterio == "genero":
            for libro in libros:
                if libro is not None and libro.getGenero().lower() == valor.lower():
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
    
    def editarLibro(self, titulo, autor, genero, ISBN, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ISBN = ISBN
        self.num_copias = int(num_copias)

    def eliminarLibro(self, libros):
        for i in range(len(libros)):
            if libros[i] == self:
                libros[i] = None
                break

    def disminuirCopiasDisponibles(self):
        if self.num_copias > 0:
            self.num_copias -= 1
        else:
            self.disponibilidad = False
           
    def aumentarCopiasDisponibles(self):
        if not(self.disponibilidad):
            self.disponibilidad = True
        self.num_copias += 1                
