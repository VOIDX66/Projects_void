#Metodo de simplificacion de Quine McCluskey
#Jaider Alberto Rendón Moreno
#29/08/2023
"""
    recorta(lista)

    Concatena todos los elementos dentro de una lista y retorna una lista nueva 

    Argumentos:
    lista (list): La lista de entrada.

    Retorna:
    elementos_recortados (list): Una nueva lista con los elementos de la lista de entrada concatenados.

    Ejemplo

    Entrada:

        lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = recorta(lista)
        print(result)

    Salida:

        [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
def recorta(lista):
    elementos_recortados = []
    for i in lista:
        elementos_recortados.extend(lista[i])
    return elementos_recortados

"""
    buscaMinterminos(mt)
    Convierte una cadena binaria con caracteres ("-") en una lista de todas las combinaciones posibles de posiciones rellenas con ceros y unos.

    Argumentos:
        mt (str): La cadena con los terminos binarios y los guiones "1-01".

    Retorna:
        temporal (list): Una lista de números decimales que representan todas las combinaciones posibles de las posiciones llenas de ceros y unos.

    Ejemplo

    Entrada:

        mt = "1-01"
        result = buscaMinterminos(mt)
        print(result)
        
    Salida:

        ['1001', '1101']

"""
def buscaMinterminos(mt):
    guiones = mt.count('-')
    if guiones == 0:
        return [str(int(mt,2))]
    opciones = [bin(i)[2:].zfill(guiones) for i in range(pow(2,guiones))]
    temporal = []
    for i in range(pow(2,guiones)):
        temporal2 = mt[:]
        indice = -1
        for j in opciones[0]:
            if indice != -1:
                indice += temporal2[indice+1:].find('-')+1
            else:
                indice = temporal2[indice+1:].find('-')
            temporal2 = temporal2[:indice]+j+temporal2[indice+1:]
        temporal.append(str(int(temporal2,2)))
        opciones.pop(0)
    return temporal

"""
    diferencias(mt1, mt2)
    Compara dos listas 'mt1' y 'mt2' elemento por elemento, si hay un cambio se retorna una tupla con un True y el indice del cambio,
    de lo contrario si hay mas de un cambio se retorna False y un -1. 
    
    Argumentos:
        mt1 (list): La primera lista (Primer mintermino).
        mt2 (list): La segunda lista (Segundo mintermino).
    
    Retorna:
        Si hay un solo cambio
            tupla: Una tupla con dos valores uno boolenao(True) y el indice del cambio hallado.

        Si hay más de un cambio
            tupla: Una tupla con dos valores uno boolenao(False) y un -1.

    Ejemplo

    Entrada:

        mt1 = [1, 0, 1, 1]
        mt2 = [1, 0, 0, 1]
        result = diferencias(mt1, mt2)
        print(result)

    Salida:
    
    (True, 2)

"""
def diferencias(mt1, mt2):
    contador = 0
    indice = 0
    for i in range(len(mt1)):
        if mt1[i] != mt2[i]:
            indice = i
            contador += 1
            if contador > 1:
                return (False, -1)
    return (True, indice)

"""
    convertir(mintermino)

    Convierte una cadena binaria en variables y sus negaciones.

    Argumentos:
        mintermino (str): Una cadena binaria representado un mintermino.

    Retorna:
        var_formula (list): Una lista de variables y sus negaciones.

    Ejemplo

    Entrada:

        mintermino = '101'
        result = convertir(mintermino)
        print(result)

    Salida:

        ['A', 'B'', 'C']
        
"""
def convertir(mintermino):
    
    var_formula = []
    for i in range(len(mintermino)):
        if mintermino[i] == '1':
            var_formula.append(chr(i + 65))  # CODIGO ASCII 65 = A, 66= B, 67 = C,...
        elif mintermino[i] == '0':
            var_formula.append(chr(i + 65) + "'")
    return var_formula

"""
    buscar_implicantes_unicos(tabla)    

    Busca los implicantes unicos en una tabla (diccionario).

    Argumentos:
    tabla (dict): Un diccionario que representa la tabla donde las claves representan los nombres de las columnas y los valores representan los implicantes en cada columna.

    Retorna:
    implicantes_unicos: Una lista de todos los implicantes unicos hallados en la tabla.

    Ejemplo

    Entrada:

        tabla = {
        '1': ['0-1','-01'],
        '2': ['01-'],
        '3': ['0-1','01-'],
        '4': ['10-'],
        '5': ['-01','10-']
        }
        implicantes = buscar_implicantes_unicos(tabla)
        print(implicantes)

    Salida:

        ['01-' , '10-']

"""
def buscar_implicantes_unicos(tabla):
    implicantes_unicos = []
    for i in tabla:
        if len(tabla[i]) == 1: #Unico implicante en la columna
            if tabla[i][0] not in implicantes_unicos:
                implicantes_unicos.append(tabla[i][0])

    return implicantes_unicos

"""
    marcar_todos(dos, opciones_dict)
    
     Marca ciertos elementos en el diccionario 'tabla' dependiendo de su cantidad de marcas en otros minterms.

     Argumentos:
         dos (lista): Una lista de elementos que se marcarán en el diccionario 'tabla'.
         opciones_dict (dict): Un diccionario donde las claves son cadenas que representan elementos y los valores son listas de dos elementos.

     Retorna:
         confirmados: un conjunto de elementos confirmados.

     Ejemplo:
         dos = [1, 2, 3]
         tabla = {'1': [10-1, 1001], '2': [0001, 1001], '3': [0001, 10-1]}
         confirmados = marcar_todos(dos, tabla)
         print(confirmados)
         # Salida: {10-1, 1001}
         
    Como se puede apreciar en el ejemplo anterior, retorno las      
     """
def marcar_todos(dos, tabla, confirmados):
    if len(tabla) > 0:
        dos.sort()
        temporal = set(dos)
        nueva_tabla = dict(tabla)
        for i in dos:
            opciones = tabla[str(i)]
            x = -1
            y = -1
            for j in tabla:
                if (opciones[0] in tabla[j]) and (str(i) != j):
                    x = j
                elif (opciones[1] in tabla[j]) and (str(i) != j):
                    y = j
            if int(x) == -1 and int(y) == -1:
                confirmados.add(opciones[0])
            elif int(x) == -1 and int(y) > 0:
                confirmados.add(opciones[1])
                nueva_tabla.pop(y)
            elif int(y) == -1 and int(x) > 0:
                confirmados.add(opciones[0])
                nueva_tabla.pop(x)       
            elif len(tabla[str(x)]) > len(tabla[str(y)]):
                confirmados.add(opciones[0])
                nueva_tabla.pop(x)
            elif len(tabla[str(x)]) < len(tabla[str(y)]):
                confirmados.add(opciones[1])
                nueva_tabla.pop(y)
            temporal.discard(i)
            nueva_tabla.pop(str(i))    
            marcar_todos(list(temporal),nueva_tabla,confirmados)
            break
    return confirmados
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\nMÉTODO DE SIMPLIFICACIÓN DE QUINE MCCLUSKEY\n")
print("Por favor ingrese los términos separados por un espacio. \n")
mt = [int(i) for i in input("Ingrese los mintérminos: ").strip().split()]
mt.sort() #Ordenamos de menor a mayor los minterminos
minterminos = mt
max_minterm = len(bin(minterminos[-1]))-2
grupos = {}
implicantes = set()

# Comenzamos la agrupación primaria
'''
    Contamos el número de unos en cada mintermino, luego guardamos el equivalente binario desde la posicion 2 para evitar '0b' que agrega la funcion
    seguido lo metemos en una cadena y rellenamos con ceros a la izquierda equivalentes al mintermino más grande. Despues validamos si ya existe
    una clave con ese número de unos, si ya existe simplemente agregamos el mintermino al grupo con esa clave, de lo contrario se crea la clave y
    se introduce de igual manera.
'''
for minterm in minterminos:
    count = bin(minterm).count('1')
    minterm_str = bin(minterm)[2:].zfill(max_minterm)

    if count in grupos:
        grupos[count].append(minterm_str)
    else:
        grupos[count] = [minterm_str]
# Término de la agrupación primaria

# Proceso para crear las tablas y encontrar los implicantes primos 
while True:
    temporal = grupos.copy()
    grupos = {}
    n = 0
    marcados = set()
    debo_parar = True
    lclaves = sorted(list(temporal.keys()))
    for i in range(len(lclaves)-1):
        for j in temporal[lclaves[i]]: # Iteración a través del grupo de elementos actual 
            for k in temporal[lclaves[i+1]]: # Iteración a través del siguiente grupo de elementos
                cambio = diferencias(j,k) # Comparamos los mintérminos
                if cambio[0]: # Si los mintérminos difieren solamente en un bit
                    minterm_cambio = j[:cambio[1]] + '-' + j[cambio[1]+1:]
                    if n in grupos:
                        if minterm_cambio not in grupos[n]:
                            grupos[n].append(minterm_cambio)
                    else:
                        grupos[n] = [minterm_cambio]
                    debo_parar = False
                    marcados.add(j) # Marca el elemento j
                    marcados.add(k) # Marca el elemento k

        n += 1
    desmarcados_local = set(recorta(temporal)).difference(marcados) # Desmarcamos los elementos de cada tabla
    implicantes = implicantes.union(desmarcados_local) # Agregamos el implicante primo a la lista.
    if debo_parar: # Si los mintérminos no pueden ser combinados
        break #Detenemos el ciclo
'''
    El fragmento de código es un bucle que itera sobre la lista de implicantes. Para cada implicante genera una lista de minterminos mezclados
    llamando a la función buscaMinterminos. Luego, verifica si cada mintermino de la lista ya existe en el diccionario de tabla.
    Si es así, agrega el implicante a la lista de valores para esa clave. Si el mintermino no existe, crea un nuevo par clave-valor en el diccionario
    de tabla con el mintermino valor y el implicante como clave.
'''

tabla = {}
for i in implicantes:
    minterminos_mezclados = buscaMinterminos(i)
    for j in minterminos_mezclados:
        if j in tabla:
            if i not in tabla[j]:
                tabla[j].append(i)
        else:
            tabla[j] = [i]

"""
    Este fragmento de código busca elementos únicos y compartidos en dos listas.

    Entradas:
    - implicantes_unicos: Una lista de elementos únicos.
    - tabla: Diccionario que representa una tabla con claves como nombres de columnas y valores como listas de implicantes en cada columna.
"""
implicantes_unicos = buscar_implicantes_unicos(tabla)

#En reducir_tabla dejaremos el dicionario unicamente con los implicantes unicos y sus respectivas claves
reducir_tabla = {}
for i in tabla:
    for j in implicantes_unicos:
        if j in tabla[i]:
            reducir_tabla[i] = tabla[i]

#En nueva_tabla dejaremos todo lo demás a exepcion de los implicantes unicos
nueva_tabla = {}
for i in tabla:
    if i not in reducir_tabla:
        nueva_tabla[i] = tabla[i]

#En dos marcas dejaremos las claves de los elementos que tengan dos elementos en su columna
dos_marcas = []
for i in nueva_tabla:
    if len(nueva_tabla[i]) == 2:
        dos_marcas.append(int(i))
dos_marcas.sort()#Los ordenamos

complemento = marcar_todos(dos_marcas, nueva_tabla, complemento)

#Agregamos los terminos en complemento a los implicantes unicos que ya teniamos
formula_final = list(complemento)+implicantes_unicos
formato_ecuacion = []

#Convertimos termino por termino en sus repectiva variable
for i in range(len(formula_final)):
    formato_ecuacion.append(convertir(formula_final[i]))
    
#VAMOS A IMPRIMIR EL RESULTADO
#Por cada termino ponemos un espacio un "+" y otro espacio.
print("\nSOLUCION: \n")
for i in range(len(formato_ecuacion)):
    for j in formato_ecuacion[i]:
        print(j, end = '')
    if i < len(formato_ecuacion)-1:
        print(" + ", end = '')    
print("\n")

#EJEMPLOS DE ENTRADAS
#Tambien se pueden ingresar en desorden, es indiferente.
# 1 2 3 4 5
# 1 4 6 7 8 9 10 11 15
# 0 1 3 4 6 7 9 10 11 12 15 16 23 24 25 26 27
