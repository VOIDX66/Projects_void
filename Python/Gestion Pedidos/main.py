
from pedido import Pedido
from figura import Figura
from tkinter.ttk import *
from tkinter import *


#Lista donde se almacenaran los pedidos
pedidos = []


#Inicio de manejo de interfaz grafica y dimensiones de la pantalla
ventana = Tk()

def AgregarPedido():
    for widget in ventana.winfo_children():
        widget.destroy()
        
    #Titulo Agregar Pedido
    texto_agregar_pedido = Label(ventana, text="Agregar Pedido",font=("Cascadia Code SemiBold", 25),background="#186F65")
    texto_agregar_pedido.place(x=260,y=20)
    
    nombre = StringVar()
    direccion = StringVar()
    celular = StringVar()
    nombre_figura = StringVar()
    tamaño = StringVar()
    precio = StringVar()
    cantidad_yeso = StringVar()
    cantidad_figuras = StringVar()
    # Datos del cliente 
    texto_datos_cliente = Label(ventana, text="Datos del cliente",font=("Cascadia Code SemiBold", 10))
    texto_datos_cliente.place(x=120,y=80)
    
    texto_in_nombre = Label(ventana, text="Nombre Cliente",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_nombre.place(x=120,y=110)
    ingreso_nombre = Entry(ventana, textvariable=nombre)
    ingreso_nombre.place(x=120,y=130)
    
    texto_in_direccion = Label(ventana, text="Direccion",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_direccion.place(x=300,y=110)
    ingreso_direccion = Entry(ventana, textvariable=direccion)
    ingreso_direccion.place(x=300,y=130)
    
    texto_in_celular = Label(ventana, text="Celular",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_celular.place(x=480,y=110)
    ingreso_celular = Entry(ventana, textvariable=celular)
    ingreso_celular.place(x=480,y=130)
    
    #Datos de las figuras
    texto_informacion_figuras = Label(ventana, text="Información Figura",font=("Cascadia Code SemiBold", 10))
    texto_informacion_figuras.place(x=120,y=160)
    
    texto_in_nombre_figura = Label(ventana, text="Nombre Figura",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_nombre_figura.place(x=120,y=190)
    ingreso_nombre_figura = Entry(ventana, textvariable=nombre_figura)
    ingreso_nombre_figura.place(x=120,y=210)
    
    texto_in_tamaño = Label(ventana, text="Tamaño (cm)",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_tamaño.place(x=250,y=190)
    ingreso_tamaño = Entry(ventana, textvariable=nombre_figura, width=15)
    ingreso_tamaño.place(x=250,y=210)
    
    texto_in_precio = Label(ventana, text="Precio",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_precio.place(x=350,y=190)
    ingreso_precio = Entry(ventana, textvariable=precio, width=10)
    ingreso_precio.place(x=350,y=210)
    
    texto_in_cantidad_yeso = Label(ventana, text="Cantidad Yeso und (lb)",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_cantidad_yeso.place(x=420,y=190)
    ingreso_cantidad_yeso = Entry(ventana, textvariable=precio, width=30)
    ingreso_cantidad_yeso.place(x=420,y=210)
    
    texto_in_cantidad_figuras = Label(ventana, text="Cantidad Figuras",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_cantidad_figuras.place(x=610,y=190)
    ingreso_cantidad_figuras = Entry(ventana, textvariable=precio, width=22)
    ingreso_cantidad_figuras.place(x=610,y=210)
    
    texto_lista_figuras = Label(ventana, text="Lista de Figuras",font=("Cascadia Code SemiBold", 10))
    texto_lista_figuras.place(x=120,y=240)
    
    lista_figuras = Treeview(ventana, columns=("","","","",""),selectmode=None)
    lista_figuras.heading("#1",text="Nombre Figura")
    lista_figuras.heading("#2",text="Tamaño (cm)")
    lista_figuras.heading("#3",text="Precio")
    lista_figuras.heading("#4",text="Cantidad Yeso und (lb)")
    lista_figuras.heading("#5",text="Cantidad Figuras")


    lista_figuras.column("#0", stretch=NO)
    lista_figuras.column("#1", stretch=NO)
    lista_figuras.column("#2", stretch=NO)
    lista_figuras.column("#3", stretch=NO)
    lista_figuras.column("#4", stretch=NO)
    lista_figuras.column("#5", stretch=NO)
    lista_figuras.column("#0",width=0)
    lista_figuras.column("#1",minwidth=100,width=100)
    lista_figuras.column("#2",minwidth=120,width=120)
    lista_figuras.column("#3",minwidth=100,width=100)
    lista_figuras.column("#4",minwidth=130,width=130)
    lista_figuras.column("#5",minwidth=120,width=120)
    lista_figuras.place(width=572,height=100)
    lista_figuras.place(x=120, y=270)
    

    #Scrollbar
    scroll = Scrollbar(ventana,orient="vertical",command=lista_figuras.yview)
    lista_figuras.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right",fill="y")


def menu():
    ventana.title("Gestion de Pedidos")
    ventana.configure(background="#186F65")
    ventana.geometry('800x500')
    ventana.resizable(width=False,height=False)

    #Titulo del menú
    texto_menu = Label(ventana, text="Menú Principal",font=("Cascadia Code SemiBold", 25),background="#186F65")
    texto_menu.place(x=260,y=20)

    #Opciones del menu

    bm_agregar_pedido = Button(ventana,text="1. Agregar Pedido",font=("Cascadia Code SemiBold", 12), width=25, background="#ECE3CE", command=lambda: AgregarPedido())
    bm_agregar_pedido.place(x=280,y=100)

    bm_eliminar_pedido = Button(ventana,text="2. Eliminar Pedido",font=("Cascadia Code SemiBold", 12), width=25, background="#ECE3CE", command=lambda: None)
    bm_eliminar_pedido.place(x=280,y=180)

    bm_ver_pedidos = Button(ventana,text="3. Ver Pedidos",font=("Cascadia Code SemiBold", 12), width=25, background="#ECE3CE", command=lambda: None)
    bm_ver_pedidos.place(x=280,y=260)

menu()


ventana.mainloop()
