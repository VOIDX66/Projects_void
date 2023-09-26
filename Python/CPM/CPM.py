#Algoritmo de la ruta critica desarrollado por Jaider Rendón
from tkinter import *
from tkinter.ttk import *

ventana = Tk()
#Titulo de la ventana
ventana.title("Método de la Ruta Crítica")
ventana.geometry('600x300')
ventana.resizable(width=False,height=False)

tareas = dict()
indice = 0
def agregar():
    global indice
    lista_tareas.insert("","end",values=(chr(65+indice),tarea.get(),duracion.get(),dependencia.get()))
    tareas[chr(65+indice)] = (duracion.get(),dependencia.get())
    print(tareas)
    indice += 1
    
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
entrada_duracion = Entry(ventana,textvariable=dependencia)
entrada_duracion.place(x=350,y=30)
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
boton_calcular = Button(ventana,text="Calcular Ruta Crítica")
boton_calcular.place(x=50,y=200)
#Mostramos la ventana
ventana.mainloop()