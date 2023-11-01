from usuario import Usuario
from libro import Libro
from categoria import Categoria
from prestamo import Prestamo
import os
import datetime

usuarios = []
libros = []
categorias = []

# Creación de usuarios
usuario1 = Usuario("Juan", 12345, "example@example.com", 3131313131)
usuarios.append(usuario1)
usuario2 = Usuario("Pedrito Pérez", 12345, "example@example.com")
usuarios.append(usuario2)

#Creación de categorias
categoria1 = Categoria("Literatura")
categorias.append(categoria1)
#Subcategorias de Literatura-------------------------------------
categoria1_1 = Categoria("Romance", categoria1)
categoria1.agregar_subcategoria(categoria1_1)
categorias.append(categoria1_1)

categoria1_2 = Categoria("Drama", categoria1)
categoria1.agregar_subcategoria(categoria1_2)
categorias.append(categoria1_2)

categoria1_3 = Categoria("Paranormal", categoria1)
categoria1.agregar_subcategoria(categoria1_3)
categorias.append(categoria1_3)

categoria1_4 = Categoria("Comedia", categoria1)
categoria1.agregar_subcategoria(categoria1_4)
categorias.append(categoria1_4)

categoria1_5 = Categoria("Horror", categoria1)
categoria1.agregar_subcategoria(categoria1_5)
categorias.append(categoria1_5)
#----------------------------------------------------------------
categoria2 = Categoria("Ficción")
categorias.append(categoria2)
#Subcategorias de Ficción----------------------------------------
categoria2_1 = Categoria("Fantasia", categoria2)
categoria2.agregar_subcategoria(categoria2_1)
categorias.append(categoria2_1)

categoria2_2 = Categoria("Apocalipsis", categoria2)
categoria2.agregar_subcategoria(categoria2_2)
categorias.append(categoria2_2)

categoria2_3 = Categoria("Espacial", categoria2)
categoria2.agregar_subcategoria(categoria2_3)
categorias.append(categoria2_3)

categoria2_4 = Categoria("Ciberpunk", categoria2)
categoria2.agregar_subcategoria(categoria2_4)
categorias.append(categoria2_4)

categoria2_5 = Categoria("Futurista", categoria2)
categoria2.agregar_subcategoria(categoria2_5)
categorias.append(categoria2_5)
#----------------------------------------------------------------
categoria3 = Categoria("Información")
categorias.append(categoria3)
#Subcategorias de Información-------------------------------------
categoria3_1 = Categoria("Manual", categoria3)
categoria3.agregar_subcategoria(categoria3_1)
categorias.append(categoria3_1)

categoria3_2 = Categoria("Diccionario", categoria3)
categoria3.agregar_subcategoria(categoria3_2)
categorias.append(categoria3_2)

categoria3_3 = Categoria("Enciclopedia", categoria3)
categoria3.agregar_subcategoria(categoria3_3)
categorias.append(categoria3_3)
#----------------------------------------------------------------
categoria4 = Categoria("Infantil")
categorias.append(categoria4)
#Subcategorias de Infantil---------------------------------------
categoria4_1 = Categoria("Cuento",categoria4)
categoria4.agregar_subcategoria(categoria4_1)
categorias.append(categoria4_1)

categoria4_2 = Categoria("Libro Iustrado",categoria4)
categoria4.agregar_subcategoria(categoria4_2)
categorias.append(categoria4_1)

categoria4_3 = Categoria("Aprendizaje",categoria4)
categoria4.agregar_subcategoria(categoria4_3)
categorias.append(categoria4_1)
#----------------------------------------------------------------
categoria5 = Categoria("Autoayuda")
categorias.append(categoria5)
#Subcategorias de Autoayuda--------------------------------------
categoria5_1 = Categoria("Desarrollo personal",categoria5)
categoria5.agregar_subcategoria(categoria5_1)
categorias.append(categoria5_1)

categoria5_2 = Categoria("Relaciones personales",categoria5)
categoria5.agregar_subcategoria(categoria5_2)
categorias.append(categoria5_2)

categoria5_3 = Categoria("Finanzas",categoria5)
categoria5.agregar_subcategoria(categoria5_3)
categorias.append(categoria5_3)
#----------------------------------------------------------------
categoria6 = Categoria("Biografias")
categorias.append(categoria6)
#----------------------------------------------------------------
categoria7 = Categoria("Historia")
categorias.append(categoria7)
#----------------------------------------------------------------
categoria8 = Categoria("Ciencias Sociales")
categorias.append(categoria8)
#Subcategorias de Ciencias Sociales------------------------------
categoria8_1 = Categoria("Antropología",categoria8)
categoria8.agregar_subcategoria(categoria8_1)
categorias.append(categoria8_1)

categoria8_2 = Categoria("Sociología",categoria8)
categoria8.agregar_subcategoria(categoria8_2)
categorias.append(categoria8_2)

categoria8_3 = Categoria("Economia",categoria8)
categoria8.agregar_subcategoria(categoria8_3)
categorias.append(categoria8_3)
#----------------------------------------------------------------
categoria9 = Categoria("Ciencias Naturales")
categorias.append(categoria9)
#Subcategorias de Ciencias Naturales-----------------------------
categoria9_1 = Categoria("Matemáticas",categoria9)
categoria9.agregar_subcategoria(categoria9_1)
categorias.append(categoria9_1)

categoria9_2 = Categoria("Física",categoria9)
categoria9.agregar_subcategoria(categoria9_2)
categorias.append(categoria9_2)

categoria9_3 = Categoria("Quimica",categoria9)
categoria9.agregar_subcategoria(categoria9_3)
categorias.append(categoria9_3)

categoria9_4 = Categoria("Biología",categoria9)
categoria9.agregar_subcategoria(categoria9_4)
categorias.append(categoria9_4)
#----------------------------------------------------------------
categoria10 = Categoria("Filosofia")
categorias.append(categoria10)
#----------------------------------------------------------------

# Creación de libros
libro1 = Libro("IT", "Stephen King", "Terror", "CFT0001TR",categoria1_5, 57)
libros.append(libro1)
libro2 = Libro("100 años de soledad", "Gabriel García Márquez", "Novela", categoria1, "NBL0001NV")
libros.append(libro2)
libro3 = Libro("El coronel no tiene quien le escriba", "Gabriel García Márquez", categoria1, "Novela", "NBL0002NV")
libros.append(libro3)
libro4 = Libro("Carrie", "Stephen King", "Terror", "CFT0001TR", categoria1_5, 57)
libros.append(libro4)


def menu():
    #os.system("cls")#Limpiar pantalla cada que se acceda al menú
    print("|--------Menu Principal-------|")
    print("|OPCIONES DE MANEJO DE USARIOS|")
    print("|  1. Crear usuario           |")
    print("|  2. Editar usuario          |")
    print("|  3. Eliminar usuario        |")
    print("|  4. Buscar usuario          |")
    print("|OPCIONES DE MANEJO DE LIBROS |")
    print("|  5. Registrar Libro         |")
    print("|  6. Buscar Libro            |")
    print("|  7. Ver Categorias          |")
    print("|  8. Realizar Prestamo       |")
    print("|  9. Realizar Devolución     |")

while True:
    menu()
    opcion = input("Seleccione una opcion: ")
    #Notas, mover a un switch case, me falta lo de calcular los dias, las multas y los inventarios
    
    if int(opcion) < 1 or int(opcion) > 9:
        print("\n¡Opcion invalida, por favor seleccione nuevamente!...")
    
    if opcion == "1":
        print("\n Crear Usuario \n")
        nombre = input("Ingrese el nombre del usuario: ")
        documento = input("Ingrese el número de documento: ")
        correo = input("Ingrese su correo electrónico: ")
        telefono = input("Ingrese su numero de teléfono: ")
        nuevo_usuario = Usuario(nombre, documento, correo, telefono)
        if nuevo_usuario.buscarUsuario("documento", documento, usuarios):
            print("Ya existe un usaurio con este documento")
            os.system("pause")
        else:    
            usuarios.append(nuevo_usuario)
            print("Usuario creado exitosamente.")
            os.system("pause")
    
    if opcion == "2":
        print("\n Editar Usuario \n")
        documento = input("Ingrese el documento del usuario: ")
        usuario_editar = Usuario().buscarUsuario("documento", documento, usuarios)
        if usuario_editar:
            print("Datos del usuario:")
            print("Presione Enter para omitir")
            print(f"Nombre: {usuario_editar.getNombre()}")
            new_name = input("Nuevo nombre: ")
            print(f"Identificación: {usuario_editar.getIdentificacion()}")
            new_id = input("Nueva Identificación: ")
            print(f"Correo: {usuario_editar.getCorreo()}")
            new_correo = input("Nuevo correo: ")
            print(f"Telefono: {usuario_editar.getTelefono()}")
            new_telefono = input("Nuevo telefono: ")
            
            if not(new_name):
                new_name = usuario_editar.getNombre()
            if not(new_id):
                new_id = usuario_editar.getIdentificacion()
            if not(new_correo):
                new_correo = usuario_editar.getCorreo()
            if not(new_telefono):
                new_telefono = usuario_editar.getTelefono()
            
            usuario_editar.editarUsuario(new_name, new_id, new_correo, new_telefono) 
        else:
            print(f"No se encontró ningún usuario con el documento {ident}.\n")

                             
        
    if opcion == "4":
            print("Seleccione el criterio de busqueda para el usuario: ")
            print("0. Nombre")
            print("1. Documento")
            criterio = input("Ingrese la opción: ")
            
            if criterio == "0":
                criterio = "nombre"
                nombre_usuario = input("Ingrese el nombre del usuario: ")
                usuario_encontrado = Usuario.buscarUsuario(criterio, nombre_usuario, usuarios)
                if usuario_encontrado:
                    for user in usuario_encontrado:
                        print(user)
                        
                else:
                    print(f"No se encontró ningún usuario con el nombre {nombre_usuario}.\n")
                    
            if criterio == "1":
                criterio = "documento"
                ident = int(input("Ingrese el documento del usuario: "))
                usuario_encontrado = Usuario.buscarUsuario(criterio, ident, usuarios)
                if usuario_encontrado:
                    print(usuario_encontrado)     
                else:
                    print(f"No se encontró ningún usuario con el documento {ident}.\n")
    
    
    if opcion == "5":
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el nombre del autor: ")
        genero = input("Ingrese el genero del libro: ")
        ISBN = input("Ingrese el código del libro (ISBN): ")
        num_copias = int(input("Digite el número de copias de libro: "))
        print("Es necesario seleccionar la categoria del libro...")
        print("Ver listado de las categorias: ")
        os.system("pause")
        
        for i,categoria in enumerate(categorias):
            print(f"{i+1}: {categoria}")
        opcion = input("Por favor seleccione el número de la categoria: ")
        categoria_seleccionada = categorias[int(opcion)-1]
        
        print("\nDatos ingresados: ")
        print(f"Titulo: {titulo}")
        print(f"Autor: {autor}")
        print(f"Genero: {genero}")
        print(f"ISBN: {ISBN}")
        print(f"Categoria: {categoria_seleccionada}")
        print(f"Numero de Copias: {num_copias}")
        
        os.system("pause")
        nuevo_libro = Libro(titulo, autor, genero, ISBN, categoria_seleccionada, num_copias)
        libros.append(nuevo_libro)
        print("Libro registrado exitosamente.\n")
        
    
                
    if opcion == "7":
        print("Seleccione el criterio de busqueda para el libro: ")
        print("1. Titulo")
        print("2. Autor")
        print("3. Volver al menu")
        criterio = input("Ingrese la opción: ")
        libro_encontrado = None
        
        if int(criterio) < 1 or int(criterio) > 3:  
            print("\n¡Opcion invalida, por favor seleccione nuevamente!...")
        
        if criterio == "1":
            criterio = "titulo"
            titulo_libro = input("Ingrese el titulo del libro: ")
            libro_encontrado = Libro.buscarLibro(criterio, titulo_libro, libros)
            if libro_encontrado:
                for i,libro in enumerate(libro_encontrado):
                    print(f"{i+1}: {libro}")
                    
            else:
                print(f"No se encontró ningún libro con el titulo {titulo_libro}.\n")
                
                
        if criterio == "2":
            criterio = "autor"
            aut = input("Ingrese el nombre del autor: ")
            libro_encontrado = Libro.buscarLibro(criterio, aut, libros)
            if libro_encontrado:
                for i,libro in enumerate(libro_encontrado):
                    print(f"{i+1}: {libro}")
            else:
                print(f"No se encontró ningún libro del autor {aut}.\n")
         
        
        if libro_encontrado:
            print("\n Opciones ")
            print("1. Realizar Prestamo")
            print("2. Volver al menu")       
            seleccion = input("Ingrese la opcion: ")     
            
            if seleccion == "1":
                seleccion = input("Ingrese el número del libro : ")
                ident = int(input("Ingrese el documento del usuario: "))
                usuario_encontrado = Usuario.buscarUsuario("documento", ident, usuarios)
                if usuario_encontrado:
                    fecha_actual = datetime.date.today()
                    nuevo_prestamo = Prestamo(usuario_encontrado,libro_encontrado[int(seleccion)-1,fecha_actual,])     
                else:
                    print(f"No se encontró ningún usuario con el documento {ident}.\n")
            
            
            
    if opcion == "7":
        print("\n")
        for i,categoria in enumerate(categorias):
            print(f"{i+1}: {categoria}")
            
        print("\nOpciones: ")
        print("1. Ver cantidad de Subcategorias")
        print("2. Mostrar Subcategorias")
        print("3. Volver al menú")
        
        seleccion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            seleccion = input("Seleccione el número de la categoria: ")
            categoria_seleccionada = categorias[int(seleccion)-1]
            print(f"La categoria {categoria_seleccionada} tiene {categoria_seleccionada.cantidad_de_subcategoria()} subcategorias")
        
        if opcion == "2":
            seleccion = input("Seleccione el número de la categoria: ") 
            categoria_seleccionada = categorias[int(seleccion)-1]
            subcategorias = categoria_seleccionada.obtener_subcategorias()
            if subcategorias:
                print(f"\nLas subcategorias de {categoria_seleccionada} son:")
                for i,categoria in enumerate(subcategorias):
                    print(f"{i+1}: {categoria}")
            else:
                print(f"\nLa categoria {categoria_seleccionada} no tiene subcategorias registradas:")
                
        if opcion == "3":
            pass
            
    os.system("pause")
    print("\n")
                            
  