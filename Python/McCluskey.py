def diferencias(mint1, mint2):
    contador = 0
    index = 0
    for i in range(len(mint1)):
        if mint1[i] != mint2[i]:
            index = i
            contador += 1
            if contador > 1:
                return (False, -1)
    return (True, index)

def reducir(lista):
    lista_reducida = []
    for i in lista:
        lista_reducida.extend(lista[i])
    return lista_reducida         
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Metodo de Simplificacion de Quine McCluskey")

#Se recibe la lista de minterms por parte del usuario
entrada = input("Por favor ingrese los minterminos searadpos por un espacio : ")

#Se divide la lista en sub cadenas
numeros = entrada.split()

#Se convierte cada sub cadena en un numero entero y se pone en un vector
minterms = [int(i) for i in numeros]

#Ordenamos los minters de menor a mayor
minterms.sort()

#Obtenemos el tamaño del ultimo termino del vector, este debe ser el de mayor valor
#La posicion -1 en el vector denota la ultima posicion del mismo
#Le restamos dos a la lomngitud ya que el metodo bin() retorna el equivalente binario del número acompañado de un '0b' que representa que es binario
longitud = len(bin(minterms[-1]))-2

#Creamos un diccionario, aqui se guardaran las agrupaciones
grupos = {}
implicantes = set()
#Comenzamos a agrupar por la cantidad de "1" en los minterminos

"""Por cada mintermino en el vector de minterminos definimos una cantidad de unos, ya que esta ordenado de menor a mayor siempre comienza por la menor cantidad,
   luego valida si la cantidad de unos esta en el diccionario, en caso de no estar crea el espacio vacio en el diccionario, por ultimo ingresa el mintermino
   en el subgrupo correspondiente a la cantidad de unos, se aclara que se ingresa en binario con el metodo bin() apartir de la posicion 2 para evitar ingresar el '0b'.
"""
for minterm in minterms:
    num_ones = bin(minterm).count('1')
    if num_ones not in grupos:
        grupos[num_ones] = []
    grupos[num_ones].append(bin(minterm)[2:].zfill(longitud))

#Comenzamos a aparear 

copia_grupos = {}
marcados = set()
combinar = True
while combinar:
    copia_grupos = grupos.copy()
    grupos = {}
    id_grupo = 0
    marcados = set()

    num_grupo = sorted(list(copia_grupos.keys()))
    for i in range(len(num_grupo)-1):
        for j in copia_grupos[num_grupo[i]]:
            for k in copia_grupos[num_grupo[i+1]]:
                cambios = diferencias(j, k)
                if cambios[0]:
                    if id_grupo in grupos:   
                        if j[:cambios[1]]+'-'+j[cambios[1]+1:] not in grupos[id_grupo]:
                            grupos[id_grupo].append(j[:cambios[1]]+'-'+j[cambios[1]+1:])
                    else:
                        grupos[id_grupo] = [j[:cambios[1]]+'-'+j[cambios[1]+1:]]        
                    combinar = False
                    marcados.add(j)
                    marcados.add(k)
        id_grupo += 1
    desmarcados = set(reducir(copia_grupos)).difference(marcados)
    implicantes = implicantes.union(desmarcados)
    print(grupos)            
                    
# 1 4 6 7 8 9 10 11 15