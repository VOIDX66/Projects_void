#Algoritmo de la ruta critica desarrollado por Jaider Rendón
from tkinter import *
from tkinter.ttk import *
import numpy as np

#Algoritmo CPM

def cpm(actividades):
    #Iniciamos las variables
    #Inicio temprano y final tardio se llenan de ceros por la cantidad de actividades
    inicio_cercano = np.zeros(len(actividades)) 
    termino_cercano = np.zeros(len(actividades))
    inicio_lejano = np.zeros(len(actividades))
    termino_lejano = np.zeros(len(actividades))
    ruta_critica = []
    
    #Creamos una matriz de predecesores
    #Si una actividad es predecesora de otra se guarda un True
    predecesores = np.zeros((len(actividades), len(actividades)),dtype = bool)
    cont_actividades = 0
    for actividad, datos in actividades.items():
        for predecesor in datos[1]:  # Supongo que datos[1] contiene los predecesores de la actividad actual
            cont_predecesor = 0
            for elemento in actividades.keys():
                if elemento == predecesor:
                    predecesores[cont_actividades, cont_predecesor] = True
                cont_predecesor += 1
        cont_actividades += 1    
    print(predecesores)
    
    padres = np.zeros((len(actividades), len(actividades)),dtype = bool)
    for i,(padre,valor) in enumerate(actividades.items()):
        for j,(actividad,datos) in enumerate(actividades.items()):
            if padre in datos[1]:
                padres[i][j] = True
                    
    print("\n",padres)

    # Calcular el inicio temprano y final temprano
    for i, (clave, valor) in enumerate(actividades.items()):
        if not any(predecesores[i]):
            inicio_cercano[i] = 0
        else:
            inicio_cercano[i] = max(termino_cercano[j] for j, value in enumerate(predecesores[i]) if value)  # Calcula el inicio temprano

        duracion_actividad = int(valor[0])
        termino_cercano[i] = inicio_cercano[i] + duracion_actividad

    
    #No es predecesor
    no_predecesor = []
    for i in (actividades.keys()):
        es_predecesor = False
        for clave, predecesor in actividades.items():
            if i in predecesor[1]:
                es_predecesor = True
                break
        if not(es_predecesor):
            no_predecesor.append(i)
            
    max_termino_cercano = max(termino_cercano)
    for i in range(len(actividades)):
        clave = list(actividades.keys())[i]  # Obtiene la clave en el índice actual
        valor = int(actividades[clave][0])
        if clave in no_predecesor:
            termino_lejano[i] =  max_termino_cercano
            inicio_lejano[i] = termino_lejano[i] - valor
    
    predecesores[0][0] = True
    # Calcular el inicio lejano y final lejano
    for i in range(len(actividades) - 1, -1, -1):
        clave = list(actividades.keys())[i]  # Obtiene la clave en el índice actual
        valor = int(actividades[clave][0])  # Obtiene el valor correspondiente a la clave
        if clave not in no_predecesor:
            termino_lejano[i] = min(inicio_lejano[j] for j, value in enumerate(padres[i]) if value)
            inicio_lejano[i] = termino_lejano[i] - valor
        
    # Identificar la ruta crítica
    for i,(actividad,datos) in enumerate(actividades.items()):
        if inicio_cercano[i] == inicio_lejano[i] and termino_cercano[i] == termino_lejano[i]:
            ruta_critica.append(actividad)

    # Imprime los resultados de inicio lejano y final lejano
    print("\n")
    for i in range(len(actividades)):
        print(f"Actividad {i+1}: Inicio Cercano = {inicio_cercano[i]}, Termino Cercano = {termino_cercano[i]}, Inicio Lejano = {inicio_lejano[i]}, Termino Lejano = {termino_lejano[i]}")

    # Imprime la ruta crítica
    print(f"Ruta crítica: {ruta_critica}")
    
################################################################

ventana = Tk()
#Titulo de la ventana
ventana.title("Método de la Ruta Crítica")
ventana.geometry('600x300')
ventana.resizable(width=False,height=False)

tareas = dict()
indice = 0

def calcular_ruta_critica():
    if tareas:
        cpm(tareas)
def agregar():
    global indice
    dependencia_lista = dependencia.get().split(',')
    lista_tareas.insert("","end",values=(chr(65+indice),tarea.get(),duracion.get(),dependencia_lista))
    tareas[chr(65+indice)] = (duracion.get(),dependencia_lista)
    global entrada_tarea
    global entrada_duracion
    global entrada_dependencia
    
    entrada_tarea.delete(0,END)
    entrada_duracion.delete(0,END)
    entrada_dependencia.delete(0,END)
    print(tareas)
    indice += 1
    
def borrar():
    global indice
    if lista_tareas.get_children():
        elemento = lista_tareas.get_children()[-1]
        lista_tareas.delete(elemento)
        tareas.popitem()
        indice -=1
        print(tareas)
        
def borrar_todos():
    global indice
    for item in lista_tareas.get_children():
        lista_tareas.delete(item)
        tareas.popitem()
    indice = 0
    print(tareas)
    
etiqueta_texto_t = Label(ventana, text="Ingresar Tarea: ")
etiqueta_texto_t.place(x=50,y=10)
etiqueta_texto_dur = Label(ventana, text="Ingresar Duracion: ")
etiqueta_texto_dur.place(x=200,y=10)
etiqueta_texto_dep = Label(ventana, text="Ingresar Dependencia: ")
etiqueta_texto_dep.place(x=350,y=10)
    
tarea = StringVar()
duracion = StringVar()
dependencia = StringVar()
entrada_tarea = Entry(ventana,textvariable=tarea)
entrada_tarea.place(x=50,y=30)
entrada_duracion = Entry(ventana,textvariable=duracion)
entrada_duracion.place(x=200,y=30)
entrada_dependencia = Entry(ventana,textvariable=dependencia)
entrada_dependencia.place(x=350,y=30)
agregar_tarea = Button(ventana,text="Agregar",command=lambda:agregar())
agregar_tarea.place(x=500,y=25)
etiqueta_lista = Label(ventana,text="Lista de tareas: ")
etiqueta_lista.place(x=50,y=60)

lista_tareas = Treeview(ventana, columns=("","","",""),selectmode=None)
lista_tareas.heading("#1",text="Tarea")
lista_tareas.heading("#2",text="Descripcion")
lista_tareas.heading("#3",text="Duracion")
lista_tareas.heading("#4",text="Dependencia")


lista_tareas.column("#0", stretch=NO)
lista_tareas.column("#1", stretch=NO)
lista_tareas.column("#2", stretch=NO)
lista_tareas.column("#3", stretch=NO)
lista_tareas.column("#4", stretch=NO)
lista_tareas.column("#0",width=0)
lista_tareas.column("#1",minwidth=40,width=40)
lista_tareas.column("#2",minwidth=300,width=300)
lista_tareas.column("#3",minwidth=60,width=60)
lista_tareas.column("#4",minwidth=80,width=80)
lista_tareas.place(width=482,height=100)
lista_tareas.place(x=50, y=80)

#Scrollbar
scroll = Scrollbar(ventana,orient="vertical",command=lista_tareas.yview)
lista_tareas.configure(yscrollcommand=scroll.set)
scroll.pack(side="right",fill="y")


#boton de calcular
boton_calcular = Button(ventana,text="Calcular Ruta Crítica", command=lambda: calcular_ruta_critica())
boton_calcular.place(x=50,y=200)
boton_borrar = Button(ventana, text="Borrar Tarea", command=lambda: borrar())
boton_borrar.place(x=200,y=200)
boton_borrar_todos = Button(ventana, text="Borrar Todos", command=lambda: borrar_todos())
boton_borrar_todos.place(x=300,y=200)
#Mostramos la ventana
ventana.mainloop()