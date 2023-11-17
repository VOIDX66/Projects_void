#Proyecto Gestion de Pedidos

from pedido import Pedido
from figura import Figura
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

#Lista donde se almacenaran los pedidos
pedidos = []

#Figuras y pedidos quemados
figuras_prueba = []
figuras_prueba2 = []
figura1 = Figura("Guts","10","5000","1","1")
figuras_prueba.append(figura1)
figura2 = Figura("Teemo","5","1000","2","1")
figura3 = Figura("Saitama","10","5000","5","1")
figuras_prueba2.append(figura3)
figuras_prueba.append(figura2)
pedido1= Pedido("Jaider Rendon","Cll 30 #15-52",figuras_prueba,"3137068788","Liquidado")
pedidos.append(pedido1)
pedido2= Pedido("Eduardo Perez","Cll 25 #89_22",figuras_prueba,"310598784","Validado")
pedidos.append(pedido2)
pedido3= Pedido("Carlos Jimenes Zapata","Cr 25 #89B 17",figuras_prueba,"158967")
pedidos.append(pedido3)
pedido4 = Pedido("Jose Jose","Cll 68 B17",figuras_prueba2,"15")
pedidos.append(pedido4)


#Inicio de manejo de interfaz grafica y dimensiones de la pantalla
ventana = Tk()
ventana.geometry('800x500')
ventana.resizable(width=False,height=False)
ventana.configure(background="#186F65")

def LimpiarPantalla():
    for widget in ventana.winfo_children():
        widget.destroy()

def AgregarPedido():
    LimpiarPantalla()
    lista_final_figuras = []
    def agregar_figura():
        if nombre_figura.get() and tamaño.get() and precio.get() and cantidad_yeso.get() and cantidad_figuras.get():
            if tamaño.get().isnumeric():
                if precio.get().isnumeric():
                    if cantidad_yeso.get().isnumeric():
                        if cantidad_figuras.get().isnumeric():
                            lista_figuras.insert("","end",values=(nombre_figura.get(),tamaño.get(),precio.get(),cantidad_yeso.get(),cantidad_figuras.get()))
                            nueva_figura = Figura(nombre_figura.get(),tamaño.get(),precio.get(),cantidad_yeso.get(),cantidad_figuras.get())
                            lista_final_figuras.append(nueva_figura)
                            #Borramos el texto en los campos correspondientes
                            ingreso_nombre_figura.delete(0,END)
                            ingreso_tamaño.delete(0,END)
                            ingreso_precio.delete(0,END)
                            ingreso_cantidad_yeso.delete(0,END)
                            ingreso_cantidad_figuras.delete(0,END)
                        else:
                            messagebox.showerror(title="Error", message="Cantidad de figuras invalida")
                    else:
                        messagebox.showerror(title="Error", message="Cantidad de yeso invalida")
                else:
                    messagebox.showerror(title="Error", message="Precio invalido")
            else:
                messagebox.showerror(title="Error", message="Tamaño invalido")
        else:
            messagebox.showerror(title="Error", message="Por favor ingrese todos los datos de la figura")                                
        
    def borrar_figura():
        #Seleccionamos el elemento al cual damos click en la lista
        figura_eliminar = lista_figuras.focus()
        if figura_eliminar:
            #Obtenemos el elemento como un diccionario
            valores = lista_figuras.item(figura_eliminar)
            #De este seleccionamos los valores del elemeto los que son nombre,tamaño,precio etc y los desempaquetamos en una Nueva figura que usaremos para remover de la lista
            #El desempaquetado se hace con el *
            figura_seleccionada = Figura(*valores["values"])
            
            for figura in lista_final_figuras:
                if str(figura) == str(figura_seleccionada):
                    lista_final_figuras.remove(figura)
                    lista_figuras.delete(figura_eliminar)
     
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
    ingreso_tamaño = Entry(ventana, textvariable=tamaño, width=15)
    ingreso_tamaño.place(x=250,y=210)
    
    texto_in_precio = Label(ventana, text="Precio",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_precio.place(x=350,y=190)
    ingreso_precio = Entry(ventana, textvariable=precio, width=10)
    ingreso_precio.place(x=350,y=210)
    
    texto_in_cantidad_yeso = Label(ventana, text="Cantidad Yeso und (lb)",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_cantidad_yeso.place(x=420,y=190)
    ingreso_cantidad_yeso = Entry(ventana, textvariable=cantidad_yeso, width=30)
    ingreso_cantidad_yeso.place(x=420,y=210)
    
    texto_in_cantidad_figuras = Label(ventana, text="Cantidad Figuras",font=("Cascadia Code SemiBold", 10),background="#186F65")
    texto_in_cantidad_figuras.place(x=610,y=190)
    ingreso_cantidad_figuras = Entry(ventana, textvariable=cantidad_figuras, width=22)
    ingreso_cantidad_figuras.place(x=610,y=210)
    
    boton_agregar_figura = Button(ventana,text="Agregar Figura",font=("Cascadia Code SemiBold", 8), background="#ECE3CE", command=lambda: agregar_figura())
    boton_agregar_figura.place(x=120,y=240)
    
    boton_borrar_figura = Button(ventana,text="Borrar Figura Seleccionada",font=("Cascadia Code SemiBold", 8), background="#ECE3CE", command=lambda: borrar_figura())
    boton_borrar_figura.place(x=230,y=240)
    
    
    texto_lista_figuras = Label(ventana, text="Lista de Figuras",font=("Cascadia Code SemiBold", 10))
    texto_lista_figuras.place(x=120,y=270)
    
    #Visualizamos los datos en un Treeview para un mejor manejo visual
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
    lista_figuras.place(width=586,height=100)
    lista_figuras.place(x=120, y=300)
    
    #Scrollbar para movernos en el Treeview
    scroll = Scrollbar(lista_figuras,orient="vertical",command=lista_figuras.yview)
    lista_figuras.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right",fill="y")

    #Botones Confirmar y cancelar
    def ConfirmacionPedido():
        if nombre.get() and direccion.get() and celular.get():
            respuesta = messagebox.askquestion("¿Quieres continuar?", "¿Desea guardar el pedido?")
            if respuesta == "yes":
                if lista_final_figuras:
                    nuevo_pedido = Pedido(nombre.get(),direccion.get(),lista_final_figuras,celular.get())
                    pedidos.append(nuevo_pedido)
                    messagebox.showinfo(title="Notificacion",message=f"Pedido guardado con exito\nPrecio total: ${nuevo_pedido.obtener_precio_total()}")
                    menu()
                else:
                    messagebox.showerror(title="Error", message="No hay figuras seleccionadas")
        else:
            messagebox.showerror(title="Error", message="Por favor rellene todos los datos del cliente")             

    boton_confirmar = Button(ventana, text="Confirmar",font=("Cascadia Code SemiBold", 10), background="#ECE3CE",command = lambda:ConfirmacionPedido())
    boton_confirmar.place(x=120,y=420)
    
    boton_cancelar = Button(ventana, text="Cancelar",font=("Cascadia Code SemiBold", 10), background="#ECE3CE",command = lambda:menu())
    boton_cancelar.place(x=210,y=420)

def EliminarPedido():
    def VerPedidoBorrar():
        seleccion = lista_pedidos.focus()
        if seleccion:
            pedido_borrar = Toplevel(ventana,width=700,height=400)
            pedido_borrar.resizable(width=False,height=False)
            pedido_borrar.configure(background="#186F65")
            nombre_s,direccion_s,celular_s,precio_s,estado_s = lista_pedidos.item(seleccion)["values"]
            
            for i,pedido in enumerate(pedidos):
                if pedido.nombre == str(nombre_s) and pedido.direccion == str(direccion_s) and pedido.celular == str(celular_s) and pedido.precio_total == precio_s and pedido.estado == estado_s:
                    etiqueta_estado = Label(pedido_borrar, text="Estado del Pedido",font=("Cascadia Code SemiBold", 10))
                    etiqueta_estado.place(x=20,y=10)
                    etiqueta_pendiente = Label(pedido_borrar, text="Pendiente",background="#ECE3CE",font=("Cascadia Code SemiBold", 8))
                    etiqueta_pendiente.place(x=20,y=40)
                    etiqueta_liquidado = Label(pedido_borrar, text="Liquidado",background="#296EA0",font=("Cascadia Code SemiBold", 8))
                    etiqueta_liquidado.place(x=90,y=40)
                    etiqueta_validado = Label(pedido_borrar, text="Validado",background="#36A029",font=("Cascadia Code SemiBold", 8))
                    etiqueta_validado.place(x=160,y=40)
                    texto =Label(pedido_borrar,text=pedido,background = "#296EA0" if pedido.estado == "Liquidado" else "#36A029" if pedido.estado == "Validado" else "#ECE3CE")
                    texto.place(x=20,y=70)
                    
                    texto_lista_figuras = Label(pedido_borrar, text="Lista de Figuras",font=("Cascadia Code SemiBold", 10))
                    texto_lista_figuras.place(x=20,y=100)
                    
                    #Visualizamos los datos en un Treeview para un mejor manejo visual
                    lista_figuras = Treeview(pedido_borrar, columns=("","","","",""),selectmode=None)
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
                    lista_figuras.place(width=586,height=150)
                    lista_figuras.place(x=20, y=130)
                    
                    #Scrollbar para movernos en el Treeview
                    scroll = Scrollbar(lista_figuras,orient="vertical",command=lista_figuras.yview)
                    lista_figuras.configure(yscrollcommand=scroll.set)
                    scroll.pack(side="right",fill="y")
                    
                    for figura in pedido.figuras:
                        lista_figuras.insert("","end",values=(figura.nombre_figura,figura.tamaño,figura.precio,figura.cantidad_yeso,figura.cantidad_unidades))

                    def ConfimacionBorrarPedido():
                        respuesta = messagebox.askquestion("¿Quieres continuar?", "¿Desea eliminar el pedido?")
                        if respuesta == "yes":
                            Pedido.eliminar_pedido(pedido,pedidos)
                            messagebox.showinfo(title="Notificacion",message=f"Pedido eliminado con exito")
                            EliminarPedido()
                        else:
                            pedido_borrar.focus()
                    
                    boton_pedido_borrar = Button(pedido_borrar, text="Eliminar Pedido",font=("Cascadia Code SemiBold", 10), command=lambda:ConfimacionBorrarPedido())
                    boton_pedido_borrar.place(x=20,y=300)
                    
                    boton_cancelar = Button(pedido_borrar, text="Cancelar",font=("Cascadia Code SemiBold", 10), command=lambda:EliminarPedido())
                    boton_cancelar.place(x=160,y=300)
                    
                    break
            
            pedido_borrar.mainloop()
        else:
            messagebox.showerror(title="Error", message="No hay pedido seleccionado")
        
    LimpiarPantalla()
    #Titulo Eliminar Pedido
    texto_eliminar_pedido = Label(ventana, text="Eliminar Pedido",font=("Cascadia Code SemiBold", 25),background="#186F65")
    texto_eliminar_pedido.place(x=260,y=20)
    
    texto_lista_pedidos = Label(ventana, text="Lista de Pedidos",font=("Cascadia Code SemiBold", 10))
    texto_lista_pedidos.place(x=120,y=80)
    
    #Visualizamos los datos en un Treeview para un mejor manejo visual
    lista_pedidos = Treeview(ventana, columns=("","","","",""),selectmode=None)
    lista_pedidos.heading("#1",text="Nombre")
    lista_pedidos.heading("#2",text="Direccion")
    lista_pedidos.heading("#3",text="Celular")
    lista_pedidos.heading("#4",text="Precio")
    lista_pedidos.heading("#5",text="Estado")
    
    lista_pedidos.column("#0", stretch=NO)
    lista_pedidos.column("#1", stretch=NO)
    lista_pedidos.column("#2", stretch=NO)
    lista_pedidos.column("#3", stretch=NO)
    lista_pedidos.column("#4", stretch=NO)
    lista_pedidos.column("#5", stretch=NO)
    lista_pedidos.column("#0",width=0)
    lista_pedidos.column("#1",minwidth=100,width=100)
    lista_pedidos.column("#2",minwidth=120,width=120)
    lista_pedidos.column("#3",minwidth=100,width=100)
    lista_pedidos.column("#4",minwidth=130,width=130)
    lista_pedidos.column("#5",minwidth=130,width=130)
    lista_pedidos.place(width=600,height=300)
    lista_pedidos.place(x=120, y=110)
    
    #Scrollbar para movernos en el Treeview
    scroll = Scrollbar(lista_pedidos,orient="vertical",command=lista_pedidos.yview)
    lista_pedidos.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right",fill="y")
    
    if pedidos:
        for pedido in pedidos:
            lista_pedidos.insert("","end",values=(pedido.nombre,pedido.direccion,pedido.celular,pedido.precio_total,pedido.estado))
        
        
        #Boton para ver pedido seleccionado
        boton_ver_pedido = Button(ventana, text="Ver pedido seleccionado",font=("Cascadia Code SemiBold", 10), command=lambda:VerPedidoBorrar())
        boton_ver_pedido.place(x=120,y=420)
        
        boton_cancelar = Button(ventana, text="Cancelar",font=("Cascadia Code SemiBold", 10), command=lambda:menu())
        boton_cancelar.place(x=320,y=420)
            
    else:
        messagebox.showerror(title="Error", message="No hay pedidos en la base de datos")
        menu()        
            
def VerPedidos():
    def VerPedido():
        seleccion = lista_pedidos.focus()
        if seleccion:
            pedido_ver = Toplevel(ventana,width=700,height=400)
            pedido_ver.resizable(width=False,height=False)
            pedido_ver.configure(background="#186F65")
            nombre_s,direccion_s,celular_s,precio_s,estado_s = lista_pedidos.item(seleccion)["values"]
            
            for pedido in pedidos:
                if pedido.nombre == str(nombre_s) and pedido.direccion == str(direccion_s) and pedido.celular == str(celular_s) and pedido.precio_total == precio_s and pedido.estado == estado_s:
                    etiqueta_estado = Label(pedido_ver, text="Estado del Pedido",font=("Cascadia Code SemiBold", 10))
                    etiqueta_estado.place(x=20,y=10)
                    etiqueta_pendiente = Label(pedido_ver, text="Pendiente",background="#ECE3CE",font=("Cascadia Code SemiBold", 8))
                    etiqueta_pendiente.place(x=20,y=40)
                    etiqueta_liquidado = Label(pedido_ver, text="Liquidado",background="#296EA0",font=("Cascadia Code SemiBold", 8))
                    etiqueta_liquidado.place(x=90,y=40)
                    etiqueta_validado = Label(pedido_ver, text="Validado",background="#36A029",font=("Cascadia Code SemiBold", 8))
                    etiqueta_validado.place(x=160,y=40)
                    texto =Label(pedido_ver,text=pedido,background = "#296EA0" if pedido.estado == "Liquidado" else "#36A029" if pedido.estado == "Validado" else "#ECE3CE")
                    texto.place(x=20,y=70)
                    
                    texto_lista_figuras = Label(pedido_ver, text="Lista de Figuras",font=("Cascadia Code SemiBold", 10))
                    texto_lista_figuras.place(x=20,y=100)
                    
                    #Visualizamos los datos en un Treeview para un mejor manejo visual
                    lista_figuras = Treeview(pedido_ver, columns=("","","","",""),selectmode=None)
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
                    lista_figuras.place(width=586,height=150)
                    lista_figuras.place(x=20, y=130)
                    
                    #Scrollbar para movernos en el Treeview
                    scroll = Scrollbar(lista_figuras,orient="vertical",command=lista_figuras.yview)
                    lista_figuras.configure(yscrollcommand=scroll.set)
                    scroll.pack(side="right",fill="y")
                    
                    for figura in pedido.figuras:
                        lista_figuras.insert("","end",values=(figura.nombre_figura,figura.tamaño,figura.precio,figura.cantidad_yeso,figura.cantidad_unidades))

                    def Modificar_pedido():
                        LimpiarPantalla()
                        lista_final_figuras = []
                        def agregar_figura():
                            
                            if nombre_figura.get() and tamaño.get() and precio.get() and cantidad_yeso.get() and cantidad_figuras.get():
                                if tamaño.get().isnumeric():
                                    if precio.get().isnumeric():
                                        if cantidad_yeso.get().isnumeric():
                                            if cantidad_figuras.get().isnumeric():
                                                lista_figuras.insert("","end",values=(nombre_figura.get(),tamaño.get(),precio.get(),cantidad_yeso.get(),cantidad_figuras.get()))
                                                nueva_figura = Figura(nombre_figura.get(),tamaño.get(),precio.get(),cantidad_yeso.get(),cantidad_figuras.get())
                                                lista_final_figuras.append(nueva_figura)
                                                #Borramos el texto en los campos correspondientes
                                                ingreso_nombre_figura.delete(0,END)
                                                ingreso_tamaño.delete(0,END)
                                                ingreso_precio.delete(0,END)
                                                ingreso_cantidad_yeso.delete(0,END)
                                                ingreso_cantidad_figuras.delete(0,END)
                                            else:
                                                messagebox.showerror(title="Error", message="Cantidad de figuras invalida")
                                        else:
                                            messagebox.showerror(title="Error", message="Cantidad de yeso invalida")
                                    else:
                                        messagebox.showerror(title="Error", message="Precio invalido")
                                else:
                                    messagebox.showerror(title="Error", message="Tamaño invalido")
                            else:
                                messagebox.showerror(title="Error", message="Por favor ingrese todos los datos de la figura") 
                            
                        def borrar_figura():
                            #Seleccionamos el elemento al cual damos click en la lista
                            figura_eliminar = lista_figuras.focus()
                            if figura_eliminar:
                                #Obtenemos el elemento como un diccionario
                                valores = lista_figuras.item(figura_eliminar)
                                #De este seleccionamos los valores del elemeto los que son nombre,tamaño,precio etc y los desempaquetamos en una Nueva figura que usaremos para remover de la lista
                                #El desempaquetado se hace con el *
                                figura_seleccionada = Figura(*valores["values"])
                                
                                for figura in lista_final_figuras:
                                    if str(figura) == str(figura_seleccionada):
                                        lista_final_figuras.remove(figura)
                                        lista_figuras.delete(figura_eliminar)
                        
                        #Titulo Agregar Pedido
                        texto_agregar_pedido = Label(ventana, text="Modificar Pedido",font=("Cascadia Code SemiBold", 25),background="#186F65")
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
                        ingreso_nombre.insert(0,pedido.nombre)
                        ingreso_nombre.place(x=120,y=130)
                        
                        texto_in_direccion = Label(ventana, text="Direccion",font=("Cascadia Code SemiBold", 10),background="#186F65")
                        texto_in_direccion.place(x=300,y=110)
                        ingreso_direccion = Entry(ventana, textvariable=direccion)
                        ingreso_direccion.insert(0,pedido.direccion)
                        ingreso_direccion.place(x=300,y=130)
                        
                        texto_in_celular = Label(ventana, text="Celular",font=("Cascadia Code SemiBold", 10),background="#186F65")
                        texto_in_celular.place(x=480,y=110)
                        ingreso_celular = Entry(ventana, textvariable=celular)
                        ingreso_celular.insert(0,pedido.celular)
                        ingreso_celular.place(x=480,y=130)
                        
                        texto_in_celular = Label(ventana, text="Estado",font=("Cascadia Code SemiBold", 10),background="#186F65")
                        texto_in_celular.place(x=650,y=110)
                        estado_pedido = Combobox(ventana, text="HI", values=["Pendiente","Liquidado","Validado"],state="readonly")
                        estado_pedido.set(pedido.estado)
                        estado_pedido.place(x=650,y=130)
                        
                        #Datos de las figuras
                        texto_informacion_figuras = Label(ventana, text="Información Figura",font=("Cascadia Code SemiBold", 10))
                        texto_informacion_figuras.place(x=120,y=160)
                        
                        texto_in_nombre_figura = Label(ventana, text="Nombre Figura",font=("Cascadia Code SemiBold", 10),background="#186F65")
                        texto_in_nombre_figura.place(x=120,y=190)
                        ingreso_nombre_figura = Entry(ventana, textvariable=nombre_figura)
                        ingreso_nombre_figura.place(x=120,y=210)
                        
                        texto_in_tamaño = Label(ventana, text="Tamaño (cm)",font=("Cascadia Code SemiBold", 10),background="#186F65")
                        texto_in_tamaño.place(x=250,y=190)
                        ingreso_tamaño = Entry(ventana, textvariable=tamaño, width=15)
                        ingreso_tamaño.place(x=250,y=210)
                        
                        texto_in_precio = Label(ventana, text="Precio",font=("Cascadia Code SemiBold", 10),background="#186F65")
                        texto_in_precio.place(x=350,y=190)
                        ingreso_precio = Entry(ventana, textvariable=precio, width=10)
                        ingreso_precio.place(x=350,y=210)
                        
                        texto_in_cantidad_yeso = Label(ventana, text="Cantidad Yeso und (lb)",font=("Cascadia Code SemiBold", 10),background="#186F65")
                        texto_in_cantidad_yeso.place(x=420,y=190)
                        ingreso_cantidad_yeso = Entry(ventana, textvariable=cantidad_yeso, width=30)
                        ingreso_cantidad_yeso.place(x=420,y=210)
                        
                        texto_in_cantidad_figuras = Label(ventana, text="Cantidad Figuras",font=("Cascadia Code SemiBold", 10),background="#186F65")
                        texto_in_cantidad_figuras.place(x=610,y=190)
                        ingreso_cantidad_figuras = Entry(ventana, textvariable=cantidad_figuras, width=22)
                        ingreso_cantidad_figuras.place(x=610,y=210)
                        
                        boton_agregar_figura = Button(ventana,text="Agregar Figura",font=("Cascadia Code SemiBold", 8), background="#ECE3CE", command=lambda: agregar_figura())
                        boton_agregar_figura.place(x=120,y=240)
                        
                        boton_borrar_figura = Button(ventana,text="Borrar Figura Seleccionada",font=("Cascadia Code SemiBold", 8), background="#ECE3CE", command=lambda: borrar_figura())
                        boton_borrar_figura.place(x=230,y=240)
                        
                        def CargarFiguraSeleccionada():
                            seleccion = lista_figuras.focus()
                            if seleccion:
                                valores = lista_figuras.item(seleccion)["values"]
                                ingreso_nombre_figura.delete(0,END)
                                ingreso_tamaño.delete(0,END)
                                ingreso_precio.delete(0,END)
                                ingreso_cantidad_yeso.delete(0,END)
                                ingreso_cantidad_figuras.delete(0,END)
                                ingreso_nombre_figura.insert(0,valores[0])
                                ingreso_tamaño.insert(0,valores[1])
                                ingreso_precio.insert(0,valores[2])
                                ingreso_cantidad_yeso.insert(0,valores[3])
                                ingreso_cantidad_figuras.insert(0,valores[4])
                                
                                def EditarFiguraSeleccionada():
                                    figura_seleccionada = Figura(*valores)
                                    for figura in lista_final_figuras:
                                        if str(figura) == str(figura_seleccionada):
                                            if nombre_figura.get() and tamaño.get() and precio.get() and cantidad_yeso.get() and cantidad_figuras.get():
                                                if tamaño.get().isnumeric():
                                                    if precio.get().isnumeric():
                                                        if cantidad_yeso.get().isnumeric():
                                                            if cantidad_figuras.get().isnumeric():
                                                                figura.modificar_figura(ingreso_nombre_figura.get(),ingreso_tamaño.get(),ingreso_precio.get(),ingreso_cantidad_yeso.get(),ingreso_cantidad_figuras.get())
                                                                ingreso_nombre_figura.delete(0,END)
                                                                ingreso_tamaño.delete(0,END)
                                                                ingreso_precio.delete(0,END)
                                                                ingreso_cantidad_yeso.delete(0,END)
                                                                ingreso_cantidad_figuras.delete(0,END)
                                                                
                                                                for item in lista_figuras.get_children():
                                                                    lista_figuras.delete(item)
                                                                
                                                                for figura in pedido.figuras:
                                                                    lista_figuras.insert("","end",values=(figura.nombre_figura,figura.tamaño,figura.precio,figura.cantidad_yeso,figura.cantidad_unidades))
                                                            else:
                                                                messagebox.showerror(title="Error", message="Cantidad de figuras invalida")
                                                        else:
                                                            messagebox.showerror(title="Error", message="Cantidad de yeso invalida")
                                                    else:
                                                        messagebox.showerror(title="Error", message="Precio invalido")
                                                else:
                                                    messagebox.showerror(title="Error", message="Tamaño invalido")
                                            else:
                                                messagebox.showerror(title="Error", message="Por favor ingrese todos los datos de la figura")         
                                
                                boton_editar_figura = Button(ventana,text="Editar Figura Seleccionada",font=("Cascadia Code SemiBold", 8), background="#ECE3CE", command=lambda: EditarFiguraSeleccionada())
                                boton_editar_figura.place(x=590,y=240)
                        
                        boton_cargar_figura = Button(ventana,text="Cargar Figura Seleccionada",font=("Cascadia Code SemiBold", 8), background="#ECE3CE", command=lambda: CargarFiguraSeleccionada())
                        boton_cargar_figura.place(x=410,y=240)
                        
                        texto_lista_figuras = Label(ventana, text="Lista de Figuras",font=("Cascadia Code SemiBold", 10))
                        texto_lista_figuras.place(x=120,y=270)
                        
                        
                        #Visualizamos los datos en un Treeview para un mejor manejo visual
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
                        lista_figuras.place(width=586,height=100)
                        lista_figuras.place(x=120, y=300)
                        
                        #Scrollbar para movernos en el Treeview
                        scroll = Scrollbar(lista_figuras,orient="vertical",command=lista_figuras.yview)
                        lista_figuras.configure(yscrollcommand=scroll.set)
                        scroll.pack(side="right",fill="y")

                        for figura in pedido.figuras:
                            lista_figuras.insert("","end",values=(figura.nombre_figura,figura.tamaño,figura.precio,figura.cantidad_yeso,figura.cantidad_unidades))
                            lista_final_figuras.append(figura)
                        
                        #Botones Confirmar y cancelar
                        def ConfirmacionModificarPedido():
                            if nombre.get() and direccion.get() and celular.get():
                                respuesta = messagebox.askquestion("¿Quieres continuar?", "¿Desea guardar el pedido?")
                                if respuesta == "yes":
                                    if lista_final_figuras:
                                        pedido.modificar_pedido(nombre.get(), direccion.get(),lista_final_figuras,celular.get(),estado_pedido.get())
                                        messagebox.showinfo(title="Notificacion",message=f"Pedido guardado con exito\nPrecio total: ${pedido.obtener_precio_total()}")
                                        VerPedidos()
                                    else:
                                        messagebox.showerror(title="Error", message="No hay figuras seleccionadas")
                            else:
                                messagebox.showerror(title="Error", message="Por favor rellene todos los datos del cliente")             

                        boton_confirmar = Button(ventana, text="Confirmar",font=("Cascadia Code SemiBold", 10), background="#ECE3CE",command = lambda:ConfirmacionModificarPedido())
                        boton_confirmar.place(x=120,y=420)
                        
                        boton_cancelar = Button(ventana, text="Cancelar",font=("Cascadia Code SemiBold", 10), background="#ECE3CE",command = lambda:VerPedidos())
                        boton_cancelar.place(x=210,y=420)
                    
                    boton_pedido_modificar = Button(pedido_ver, text="Modificar Pedido",font=("Cascadia Code SemiBold", 10), command=lambda:Modificar_pedido())
                    boton_pedido_modificar.place(x=20,y=300)
                    
                    def Liquidar():
                        respuesta = messagebox.askquestion("¿Quieres continuar?", f"¿Desea liquidar el pedido?\nPrecio total: ${pedido.precio_total}")
                        if respuesta == "yes":
                            pedido.liquidar_pedido()
                            messagebox.showinfo(title="Notificacion",message=f"Pedido liquidado con exito")
                            VerPedidos()
                        else:
                            pedido_ver.focus()
                    
                    boton_liquidar = Button(pedido_ver, text="Liquidar",font=("Cascadia Code SemiBold", 10), command=lambda:Liquidar(), state = "disabled" if pedido.estado == "Liquidado" or pedido.estado == "Validado" else "normal")
                    boton_liquidar.place(x=170,y=300)
                    
                    def Validar():
                        respuesta = messagebox.askquestion("¿Quieres continuar?", "¿Desea validar el pedido?")
                        
                        if respuesta == "yes":
                            pedido.validar_pedido()
                            messagebox.showinfo(title="Notificacion",message=f"Pedido validado con exito")
                            VerPedidos()
                        else:
                            pedido_ver.focus()    
                             
                    boton_validar = Button(pedido_ver, text="Validar",font=("Cascadia Code SemiBold", 10), command=lambda:Validar(), state = "disabled" if pedido.estado == "Validado" or pedido.estado == "Pendiente" else "normal")
                    boton_validar.place(x=250,y=300)
                    
                    boton_cancelar = Button(pedido_ver, text="Cancelar",font=("Cascadia Code SemiBold", 10), command=lambda:VerPedidos())
                    boton_cancelar.place(x=322,y=300)
                    
                    break
            
            pedido_ver.mainloop()
        else:
            messagebox.showerror(title="Error", message="No hay pedido seleccionado")
        
    LimpiarPantalla()
    #Titulo Ver Pedidos
    texto_eliminar_pedido = Label(ventana, text="Ver Pedidos",font=("Cascadia Code SemiBold", 25),background="#186F65")
    texto_eliminar_pedido.place(x=260,y=20)
    
    texto_lista_pedidos = Label(ventana, text="Lista de Pedidos",font=("Cascadia Code SemiBold", 10))
    texto_lista_pedidos.place(x=120,y=80)
    
    #Visualizamos los datos en un Treeview para un mejor manejo visual
    lista_pedidos = Treeview(ventana, columns=("","","","",""),selectmode=None)
    lista_pedidos.heading("#1",text="Nombre")
    lista_pedidos.heading("#2",text="Direccion")
    lista_pedidos.heading("#3",text="Celular")
    lista_pedidos.heading("#4",text="Precio")
    lista_pedidos.heading("#5",text="Estado")
    
    lista_pedidos.column("#0", stretch=NO)
    lista_pedidos.column("#1", stretch=NO)
    lista_pedidos.column("#2", stretch=NO)
    lista_pedidos.column("#3", stretch=NO)
    lista_pedidos.column("#4", stretch=NO)
    lista_pedidos.column("#5", stretch=NO)
    lista_pedidos.column("#0",width=0)
    lista_pedidos.column("#1",minwidth=100,width=100)
    lista_pedidos.column("#2",minwidth=120,width=120)
    lista_pedidos.column("#3",minwidth=100,width=100)
    lista_pedidos.column("#4",minwidth=130,width=130)
    lista_pedidos.column("#5",minwidth=130,width=130)
    lista_pedidos.place(width=600,height=300)
    lista_pedidos.place(x=120, y=110)
    
    #Scrollbar para movernos en el Treeview
    scroll = Scrollbar(lista_pedidos,orient="vertical",command=lista_pedidos.yview)
    lista_pedidos.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right",fill="y")
    
    if pedidos:
        for pedido in pedidos:
            lista_pedidos.insert("","end",values=(pedido.nombre,pedido.direccion,pedido.celular,pedido.precio_total,pedido.estado))
        
        
        #Boton para ver pedido seleccionado
        boton_ver_pedido = Button(ventana, text="Ver pedido seleccionado",font=("Cascadia Code SemiBold", 10), command=lambda:VerPedido())
        boton_ver_pedido.place(x=120,y=420)
        
        boton_cancelar = Button(ventana, text="Cancelar",font=("Cascadia Code SemiBold", 10), command=lambda:menu())
        boton_cancelar.place(x=320,y=420)
            
    else:
        messagebox.showerror(title="Error", message="No hay pedidos en la base de datos")
        menu()         
    
def menu():
    #print(pedidos)
    LimpiarPantalla()
    ventana.title("Gestion de Pedidos")
    #Titulo del menú
    texto_menu = Label(ventana, text="Menú Principal",font=("Cascadia Code SemiBold", 25),background="#186F65")
    texto_menu.place(x=260,y=20)

    #Opciones del menu

    bm_agregar_pedido = Button(ventana,text="1. Agregar Pedido",font=("Cascadia Code SemiBold", 12), width=25, background="#ECE3CE", command=lambda: AgregarPedido())
    bm_agregar_pedido.place(x=280,y=100)

    bm_eliminar_pedido = Button(ventana,text="2. Eliminar Pedido",font=("Cascadia Code SemiBold", 12), width=25, background="#ECE3CE", command=lambda: EliminarPedido())
    bm_eliminar_pedido.place(x=280,y=180)

    bm_ver_pedidos = Button(ventana,text="3. Ver Pedidos",font=("Cascadia Code SemiBold", 12), width=25, background="#ECE3CE", command=lambda: VerPedidos())
    bm_ver_pedidos.place(x=280,y=260)

menu()
ventana.mainloop()
