#Metodo de simplificacion de Quine McCluskey
#Jaider Alberto Rendón Moreno

def recorta(x): # Recorta la lista
    elementos_recortados = []
    for i in x:
        elementos_recortados.extend(x[i])
    return elementos_recortados
def buscaMinterminos(a): # Función para encontrar a los mintérminos mezclados. Por ejemplo, 10-1 son obtenidos al combinar 9(1001) y 11(1011)
    gaps = a.count('-')
    if gaps == 0:
        return [str(int(a,2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
    temp = []
    for i in range(pow(2,gaps)):
        temp2,ind = a[:],-1
        for j in x[0]:
            if ind != -1:
                ind = ind+temp2[ind+1:].find('-')+1
            else:
                ind = temp2[ind+1:].find('-')
            temp2 = temp2[:ind]+j+temp2[ind+1:]
        temp.append(str(int(temp2,2)))
        x.pop(0)
    return temp

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

def convertir(mintermino):
    var_formula = []
    for i in range (len(mintermino)):
        if mintermino[i] == '1':
            var_formula.append(chr(i+65)) #CODIGO ASCII 65 = A, 66= B, 67 = C,...
        elif mintermino[i] == '0':
            var_formula.append(chr(i+65)+"'")
    return var_formula

def buscar_implicantes_unicos(tabla):
    implicantes_unicos = []
    for i in tabla:
        if len(tabla[i]) == 1: #Unico implicante en la columna
            implicantes_unicos.append(tabla[i][0]) if tabla[i][0] not in implicantes_unicos else None
    return implicantes_unicos

def buscar_dos_implicantes(tabla):
    dos_implicantes = []
    for i in tabla:
        if len(tabla[i]) == 2: #Dos implicante en la columna
            dos_implicantes.append(i) if i not in dos_implicantes else None
    return dos_implicantes
#------------------------------------------------------------------------------------------------------------------------
print('Por favor ingrese los términos separados por un espacio')
mt = [int(i) for i in input("Ingrese los mintérminos ").strip().split()]
mt.sort()
minterminos = mt
minterminos.sort()
size = len(bin(minterminos[-1]))-2
grupos,all_pi = {},set()

# Comenzamos la agrupación primaria
for minterm in minterminos:
    try:
        grupos[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
    except KeyError:
        grupos[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]
# Término de la agrupación primaria

#Comenzamos la impresión de la agrupación primaria
print("\n\n\n\nNúmero de Gpo.\tMintérminos\t\tExpresión en BCD\n%s"%('='*60))
for i in sorted(grupos.keys()):
    print("%5d:"%i) # Prints group number
    for j in grupos[i]:
        print("\t\t    %-20d%s"%(int(j,2),j)) # Imprime los mintérminos y su representación binaria (BCD)
    print('-'*60)
#Término de la impresión de la agrupación primara

# Proceso para crear las tablas y encontrar los implicantes primos 
while True:
    tmp = grupos.copy()
    grupos,m,marcados,debo_parar = {},0,set(),True
    l = sorted(list(tmp.keys()))
    for i in range(len(l)-1):
        for j in tmp[l[i]]: # Iteración a través del grupo de elementos actual 
            for k in tmp[l[i+1]]: # Iteración a través del siguiente grupo de elementos
                res = diferencias(j,k) # Comparamos los mintérminos
                if res[0]: # Si los mintérminos difieren solamente en un bit
                    try:
                        grupos[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in grupos[m] else None # Imprimimos un guión '-' en el bit que cambia y lo agregamos al grupo correspondiente
                    except KeyError:
                        grupos[m] = [j[:res[1]]+'-'+j[res[1]+1:]] # Si el grupo no existe, crearemos un grupo al principio y pondremos un guión '-' en el cambio de bi, además de agregarlo a un nuevo grupo
                    debo_parar = False
                    marcados.add(j) # Marca el elemento j
                    marcados.add(k) # Marca el elemento k
        m += 1
    desmarcados_local = set(recorta(tmp)).difference(marcados) # Desmarcamos los elemntos de cada tabla
    print(desmarcados_local)
    all_pi = all_pi.union(desmarcados_local) # Agregamos el implicante primo a la lita global.
    print("Elementos desmarcados(Implicantes Primos) de la tabla:",None if len(desmarcados_local)==0 else ', '.join(desmarcados_local)) # Imprimimos los implicantes promos en la tabla actual
    if debo_parar: # Si los mintérminos no pueden ser combinados
        print("\n\nAll Implicantes Primos: ",None if len(all_pi)==0 else ', '.join(all_pi)) # Imprimimos todos los implicantes primos
        break


sz = len(str(mt[-1]))
tabla = {}

for i in all_pi:
    minterminos_mezclados = buscaMinterminos(i)
    for j in minterminos_mezclados:
        try:
            tabla[j].append(i) if i not in tabla[j] else None # Agregamos el mintérmino a la impresión
        except KeyError:
            tabla[j] = [i]
print("\n")

implicantes_unicos = buscar_implicantes_unicos(tabla)
dos_implicantes = buscar_dos_implicantes(tabla)
print(tabla)
print("\n")


#remueveTerminos(tabla,implicantes_unicos)
print("\n Implicantes unicos")
print(implicantes_unicos)
print("\n Dos implicantes")
print(dos_implicantes)
print("\n")

compartidos = set()
for i in dos_implicantes:
    if tabla[i][0] in implicantes_unicos:
        compartidos.add(i)
    elif tabla[i][1] in implicantes_unicos:
        compartidos.add(i)    
print("Compartidos: ", compartidos)

independientes = set(dos_implicantes).difference(compartidos)

complemento = set()
print("Independientes: ",independientes)

quitar = set()
temporal_lista = []
for i in independientes:
    for j in tabla[i]:
        complemento.add(j) 
if len(independientes) > 1:
    for i in compartidos:
        for j in complemento:
            if j in tabla[i]:
                quitar.add(j)
elif len(independientes) == 1:
    temporal_lista = list(compartidos)[-1]
    complemento = complemento.difference(set(tabla[temporal_lista]))


complemento = list(complemento.difference(quitar))

formula_final = complemento+implicantes_unicos
formato_ecuacion = []
for i in range(len(formula_final)):
    formato_ecuacion.append(convertir(formula_final[i]))
#VAMOS A IMPRIMIR EL RESULTADO
print("SOLUCION: ")
for i in range(len(formato_ecuacion)):
    for j in formato_ecuacion[i]:
        print(j, end = '')
    if i < len(formato_ecuacion)-1:    
        print(" + ", end = '')    
print("\n")
# 1 4 6 7 8 9 10 11 15
# 0 1 3 4 6 7 9 10 11 12 15 16 23 24 25 26 27