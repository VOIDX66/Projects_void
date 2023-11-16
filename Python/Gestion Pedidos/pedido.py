class Pedido:
    def __init__(self, nombre, direccion , figuras, celular, estado = "Pendiente"):
        self.nombre = nombre
        self.direccion = direccion
        self.figuras = figuras
        self.celular = celular
        self.estado = estado
        acumulado = 0
        for i in figuras:
            acumulado += int(i.obtener_precio())
        self.precio_total = acumulado    
    
    def __str__(self):        
        return f"Nombre : {self.nombre}, Direccion : {self.direccion}, Cantidad de figuras : {len(self.figuras)}, Precio total : {self.precio_total}, Estado : {self.estado}"
    
    def obtener_precio_total(self):
        return self.precio_total
    
    @staticmethod
    def eliminar_pedido(pedido_s,pedidos):
        for i,pedido in enumerate(pedidos):
            if pedido == pedido_s:
                pedidos.pop(i)
                
    def modificar_pedido(self,nombre,direccion,figuras,celular,estado):
        self.nombre = nombre
        self.direccion = direccion
        self.figuras = figuras
        self.celular = celular
        self.estado = estado
        acumulado = 0
        for i in figuras:
            acumulado += int(i.obtener_precio())
        self.precio_total = acumulado  
    
    def liquidar_pedido(self):
        self.estado = "Liquidado"
        
    def validar_pedido(self):
        self.estado = "Pendiente"
    