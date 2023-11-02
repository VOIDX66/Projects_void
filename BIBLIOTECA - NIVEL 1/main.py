from usuario import Usuario
from libro import Libro
from categoria import Categoria
from prestamo import Prestamo
import os
import datetime #pip install datetime
from dateutil.relativedelta import * #pip install python-dateutil

usuarios = []
libros = []
categorias = []
prestamos = []

def confirmacion():
    confirmacion = input("\nDesea continuar (SI = Y / NO = N): ")
    confirmacion = confirmacion.lower()
    
    while confirmacion != "y" and confirmacion != "n":
        print("\nOpcion invalida, seleccione nuevamente...")
        confirmacion = input("\n Desea continuar (SI = Y / NO = N): ")
        confirmacion = confirmacion.lower()
    
    if confirmacion == "y":
        return True
    if confirmacion == "n":
        return False    
    

# Creación de usuarios
usuario1 = Usuario("Juan", 123, "example@example.com", 3131313131)
usuarios.append(usuario1)
usuario2 = Usuario("Pedrito Pérez", 1234, "example@example.com")
usuarios.append(usuario2)
usuario3 = Usuario("Jaider", 1006, "example@example.com")
usuarios.append(usuario3)

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
libro2 = Libro("100 años de soledad", "Gabriel García Márquez", "Novela", "NBL0001NV", categoria1)
libros.append(libro2)
libro3 = Libro("El coronel no tiene quien le escriba", "Gabriel García Márquez", "Novela", "NBL0002NV", categoria1)
libros.append(libro3)
libro4 = Libro("Carrie", "Stephen King", "Terror", "CFT0001TR", categoria1_5, 57)
libros.append(libro4)

# Creación de Prestamos
dias_prueba = 5
fecha_actual_prueba = datetime.date.today()
fecha_vencimiento_prueba = fecha_actual_prueba + datetime.timedelta(days=dias_prueba)
prestamo1 = Prestamo(usuario3,libro1,fecha_actual_prueba,fecha_vencimiento_prueba)
prestamos.append(prestamo1)

def menu():
    #os.system("cls")#Limpiar pantalla cada que se acceda al menú
    print("|--------Menu Principal-------|")
    print("|OPCIONES DE MANEJO DE USARIOS|")
    print("|  1. Crear Usuario           |")
    print("|  2. Editar Usuario          |")
    print("|  3. Eliminar Usuario        |")
    print("|  4. Buscar Usuario          |")
    print("|OPCIONES DE MANEJO DE LIBROS |")
    print("|  5. Registrar Libro         |")
    print("|  6. Buscar Libro            |")
    print("|  7. Ver Categorias          |")
    print("|  8. Realizar Devolución     |")

while True:
    menu()
    opcion = input("Seleccione una opcion: ")
    #Notas, mover a un switch case, me falta lo de calcular los dias, las multas y los inventarios
    
    if int(opcion) < 1 or int(opcion) > 8:
        print("\n¡Opcion invalida, por favor seleccione nuevamente!...")
    
    if opcion == "1":
        print("\n1. Crear Usuario\n")
        nombre = input("Ingrese el nombre del usuario: ")
        documento = input("Ingrese el número de documento: ")
        correo = input("Ingrese su correo electrónico: ")
        telefono = input("Ingrese su número de teléfono: ")
        
        if nombre and documento:
            if confirmacion():
                nuevo_usuario = Usuario(nombre, documento, correo, telefono)
                if nuevo_usuario.buscarUsuario("documento", documento, usuarios):
                    print("\nError, Ya existe un usuario con este documento...")
                else:    
                    usuarios.append(nuevo_usuario)
                    print("\nUsuario ha sido creado exitosamente...")
            else:
                print("\nAcción cancelada...")
        else:
            print("\nError, Los campos nombre y documento son obligatorios...")           
    
    if opcion == "2":
        print("\n2. Editar Usuario \n")
        documento = input("Ingrese el documento del usuario: ")
        usuario_editar = Usuario().buscarUsuario("documento", documento, usuarios)
        if usuario_editar:
            print("Datos del usuario a editar:")
            print("Presione Enter para omitir el campo")
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
            
            if confirmacion():
                usuario_editar.editarUsuario(new_name, new_id, new_correo, new_telefono)
                print ("\nEl Usuario ha sido editado con exito...")
            else:
                print("\nAcción cancelada...")        
            
        else:
            print(f"\nNo se encontró ningún usuario con el documento {documento}...\n")

    if opcion == "3":
        print("\n3. Eliminar Usuario\n")
        documento = input("Ingrese el documento del usuario: ")
        usuario_eliminar = Usuario().buscarUsuario("documento", documento, usuarios)
        if usuario_eliminar:
            print("Datos del usuario a eliminar")
            print(f"Nombre: {usuario_eliminar.getNombre()}")
            print(f"Identificación: {usuario_eliminar.getIdentificacion()}")
            print(f"Correo: {usuario_eliminar.getCorreo()}")
            print(f"Telefono: {usuario_eliminar.getTelefono()}")
            print("\n¿Esta seguro de eliminar al usuario?")
            if confirmacion():
                usuario_eliminar.eliminarUsuario(usuario_eliminar, usuarios)
                print("\nEl Usuario ha sido eliminado con exito...")
            else:
                print("\nAcción cancelada...")
                
    if opcion == "4":
            print("\n4. Buscar Usuario\n")
            print("Seleccione el criterio de busqueda para el usuario: ")
            print("1. Nombre")
            print("2. Documento")
            print("3. Volver al menú")
            criterio = input("Ingrese la opción: ")
            while int(criterio) < 1 or int(criterio) > 2:
                print("\n¡Opcion invalida, por favor seleccione nuevamente!...")
                criterio = input("Seleccione una opcion: ")
            
            if criterio == "1":
                criterio = "nombre"
                nombre_usuario = input("Ingrese el nombre del usuario: ")
                usuario_encontrado = Usuario.buscarUsuario(criterio, nombre_usuario, usuarios)
                if usuario_encontrado:
                    print("\n")
                    for user in usuario_encontrado:
                        print(user)
                    print("\n")    
                else:
                    print(f"No se encontró ningún usuario con el nombre {nombre_usuario}...\n")
                    
            if criterio == "2":
                criterio = "documento"
                documento = input("Ingrese el documento del usuario: ")
                usuario_encontrado = Usuario.buscarUsuario(criterio, documento, usuarios)
                if usuario_encontrado:
                    print(f"\n{usuario_encontrado}\n")     
                else:
                    print(f"\nNo se encontró ningún usuario con el documento {documento}...\n")
    
    if opcion == "5":
        print("\n5. Registrar Libro\n")
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el nombre del autor: ")
        genero = input("Ingrese el genero del libro: ")
        ISBN = input("Ingrese el código del libro (ISBN): ")
        num_copias = int(input("Digite el número de copias de libro: "))
        print("Es necesario seleccionar la categoria del libro...")
        print("¿Ver listado de las categorias?\n")
        if confirmacion():
            for i,categoria in enumerate(categorias):
                print(f"{i+1}: {categoria}")
            seleccion = input("Por favor seleccione el número de la categoria: ")
            
            while int(seleccion) < 1 or int(seleccion) > len(categorias):
                print("\nError, Número de categoria invalido...\n")
                seleccion = input("Por favor seleccione el número de la categoria: ")
                
            categoria_seleccionada = categorias[int(seleccion)-1]
            
            print("\nDatos ingresados: ")
            print(f"Titulo: {titulo}")
            print(f"Autor: {autor}")
            print(f"Genero: {genero}")
            print(f"ISBN: {ISBN}")
            print(f"Categoria: {categoria_seleccionada}")
            print(f"Numero de Copias: {num_copias}")
            
            if confirmacion():
                nuevo_libro = Libro(titulo, autor, genero, ISBN, categoria_seleccionada, num_copias)
                libros.append(nuevo_libro)
                print("Libro registrado exitosamente...\n")
            else:
                print("\nAcción cancelada...")
        else:
            print("\nAcción cancelada...")       
           
    if opcion == "6":
        print("\n6. Buscar Libro\n")
        print("Seleccione el criterio de busqueda para el libro: ")
        print("1. Titulo")
        print("2. Autor")
        print("3. Genero")
        print("4. Volver al menu")
        criterio = input("Ingrese la opción: ")
        
        if int(criterio) < 1 or int(criterio) > 4:  
            print("\n¡Opcion invalida, por favor seleccione nuevamente!...")
        
        if criterio == "1":
            criterio = "titulo"
            titulo_libro = input("Ingrese el titulo del libro: ")
            libro_encontrado = Libro.buscarLibro(criterio, titulo_libro, libros)
            print("")
            if libro_encontrado:
                for i,libro in enumerate(libro_encontrado):
                    print(f"{i+1}: {libro}")
            else:
                print(f"No se encontró ningún libro con el titulo {titulo_libro}...\n")
                
        if criterio == "2":
            criterio = "autor"
            aut = input("Ingrese el nombre del autor: ")
            libro_encontrado = Libro.buscarLibro(criterio, aut, libros)
            print("")
            if libro_encontrado:
                for i,libro in enumerate(libro_encontrado):
                    print(f"{i+1}: {libro}")
            else:
                print(f"No se encontró ningún libro del autor {aut}...\n")
                
        if criterio == "3":
            criterio = "genero"
            genero = input("Ingrese el genero del libro: ")
            libro_encontrado = Libro.buscarLibro(criterio, genero, libros)
            print("")
            if libro_encontrado:
                for i,libro in enumerate(libro_encontrado):
                    print(f"{i+1}: {libro}")
            else:
                print(f"No se encontró ningún libro del genero {genero}...\n")
                
        if libro_encontrado:
            print("\nOpciones")
            print("1. Realizar Prestamo")
            print("2. Volver al menú")
            seleccion = input("Seleccione una opcion: ")
            while int(seleccion) < 1 or int(seleccion) > 2:
                print("\n¡Opcion invalida, por favor seleccione nuevamente!...")
                seleccion = input("Seleccione una opcion: ")
                
            if seleccion == "1":
                print("\n1. Realizar Prestamo\n")
                indice = input("Por favor seleccione el número del libro: ")
                while int(indice) < 1 or int(indice) > len(libro_encontrado):
                    print("\n¡Opcion invalida, por favor seleccione nuevamente!...")
                    indice = input("Por favor seleccione el número del libro: ")
                
                libro_seleccionado = libro_encontrado[int(indice)-1]
                
                if libro_seleccionado.getDisponibilidad():
                    print("El libro seleccionado es: ")
                    print(libro_seleccionado)
                    
                    if confirmacion():
                        documento = input("Ingrese el documento del usuario: ")
                        usuario_encontrado = Usuario.buscarUsuario("documento", documento, usuarios)
                        if usuario_encontrado:
                            print(f"\n{usuario_encontrado}\n")
                            if confirmacion():
                                if not(usuario_encontrado.consultarMultas()):
                                    dias = input("Ingrese la cantidad de dias del prestamo: ")
                                    fecha_actual = datetime.date.today()
                                    fecha_vencimiento = fecha_actual + datetime.timedelta(days=int(dias))
                                    print("\nDatos del prestamo")
                                    print(f"Usuario: {usuario_encontrado.getNombre()}")
                                    print(f"Libro: {libro_seleccionado.getTitulo()}")
                                    print(f"Autor: {libro_seleccionado.getAutor()}")
                                    print(f"Fecha del prestamo: {fecha_actual}")
                                    print(f"Fecha limite: {fecha_vencimiento}")
                                    
                                    if confirmacion():
                                        nuevo_prestamo = Prestamo(usuario_encontrado, libro_seleccionado, fecha_actual, fecha_vencimiento)
                                        prestamos.append(nuevo_prestamo)
                                        libro_seleccionado.disminuirCopiasDisponibles()
                                        print("Prestamo realizado con exito...")
                                else:
                                    print("\nError, el usuario tiene una multa pendiente...")
                            else:
                                print("\nAcción cancelada...")        
                        else:
                            print(f"\nNo se encontró ningún usuario con el documento {documento}...\n")
                    else:
                        print("\nAcción cancelada...")
                else:
                    print("\nError, El libro no tiene copias disponibles...")
                        
                                 
    if opcion == "7":
        print("\n7. Ver Categorias\n")
        for i,categoria in enumerate(categorias):
            print(f"{i+1}: {categoria}")
            
        print("\nOpciones: ")
        print("1. Ver cantidad de Subcategorias")
        print("2. Mostrar Subcategorias")
        print("3. Volver al menú")
        seleccion = input("Seleccione una opcion: ")
        
        if seleccion == "1":
            print("\n1. Ver cantidad de Subcategorias")
            indice = input("Seleccione el número de la categoria: ")
            
            while int(indice) < 1 or int(indice) > len(categorias):
                print("\nError, Número de categoria invalido...\n")
                indice = input("Por favor seleccione el número de la categoria: ")
            
            categoria_seleccionada = categorias[int(indice)-1]
            print(f"La categoria {categoria_seleccionada} tiene {categoria_seleccionada.cantidad_de_subcategoria()} subcategorias")
        
        if seleccion == "2":
            print("\n2. Mostrar Subcategorias")
            indice = input("Seleccione el número de la categoria: ")
            
            while int(indice) < 1 or int(indice) > len(categorias):
                print("\nError, Número de categoria invalido...\n")
                indice = input("Por favor seleccione el número de la categoria: ")
            
            categoria_seleccionada = categorias[int(indice)-1]
            subcategorias = categoria_seleccionada.obtener_subcategorias()
            if subcategorias:
                print(f"\nLas subcategorias de {categoria_seleccionada} son:")
                for i,categoria in enumerate(subcategorias):
                    print(f"{i+1}: {categoria}")
            else:
                print(f"\nLa categoria {categoria_seleccionada} no tiene subcategorias registradas...")
    
    if opcion == "8":
        print("\n8. Realizar Devolucion\n")
        if prestamos:
            documento = input("Ingrese el documento del usuario: ")
            usuario_encontrado = Usuario.buscarUsuario("documento", documento, usuarios)
            if usuario_encontrado:
                print(f"\n{usuario_encontrado}\n")
                if confirmacion():
                    lista_prestamos = Prestamo.buscarPrestamos(documento, prestamos)
                    for i,prestamo in enumerate(lista_prestamos):
                        print(f"\n{i+1}: {prestamo}")
                    indice = input("Por favor seleccione el número del prestamo: ")
                    while int(indice) < 1 or int(indice) > len(lista_prestamos):
                        print("\nError, Número de prestamo invalido\n")
                        indice = input("Por favor seleccione el número del prestamo: ")
                    
                    prestamo_seleccionado = lista_prestamos[int(indice)-1]
                    
                    multa = prestamo_seleccionado.calcularMulta()
                    if multa:
                        print(f"\n El prestamo seleccionado tiene una multa por ${multa}")
                        print("¿El usuario desea pagar la multa?")
                        if confirmacion():
                            prestamo_seleccionado.libro.aumentarCopiasDisponibles()
                            prestamo_seleccionado.devolucion(prestamos)
                            print("La devolucion ha sido realizado con exito...")
                        else:
                            print("\nAcción cancelada...")
                else:
                    print("\nAcción cancelada...")                
            else:
                print(f"\nNo se encontró ningún usuario con el documento {documento}...\n")
        else:
            print("No hay prestamos en el sistema...")

    os.system("pause")
    
    print("\n")
                            
  