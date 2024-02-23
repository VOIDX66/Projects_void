from PIL import Image, ImageDraw
import os

class Nodo:
    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.adyacentes = []
        self.visitado = False
        self.raiz = False
        self.meta = False

    def __str__(self):
        return f"({self.y},{self.x})"
    
    def print_adyacentes(self):
        for i in self.adyacentes:
            if i.raiz == True:
                print(f"{i} NODO RAIZ")
            elif i.meta == True:
                print(f"{i} NODO META")
            else:    
                print(i)
    
    def coords(self):
        return (self.y,self.x)
    
def crear_nodos(maze):
    nodos = []
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == " " or maze[y][x] == "A" or maze[y][x] == "B":
                nodo = Nodo(y,x)
                if maze[y][x] == "A":
                    nodo.raiz = True
                elif maze[y][x] == "B":
                    nodo.meta = True    
                for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0 <= y + dy < len(maze) and 0 <= x + dx < len(maze[0]):
                        if maze[y + dy][x + dx] == " ":
                            nodo.adyacentes.append(Nodo(y+dy,x+dx))
                        elif maze[y + dy][x + dx] == "B":
                            temp = Nodo(y+dy,x+dx)
                            temp.meta = True
                            nodo.adyacentes.append(temp)
                            
                nodos.append(nodo)
    return nodos               
    
camino = []
def dfs(nodo_actual, objetivo,ruta,nodos):
    
    for nodo in nodos:
        if nodo_actual.x == nodo.x and nodo_actual.y == nodo.y:
            nodo_actual = nodo
        if objetivo.x == nodo.x and objetivo.y == nodo.y:
            objetivo = nodo
        
    if nodo_actual == objetivo:
        return True
    nodo_actual.visitado = True

    ruta.append(nodo_actual)
    camino.append(nodo_actual.coords())
    
    for x in camino:
        print(x)
    os.system('cls')  # Windows
        
    for adyacente in nodo_actual.adyacentes:
        if not adyacente.visitado:
            adyacente.visitado = True
            if dfs(adyacente, objetivo,ruta,nodos):
                return True
    ruta.pop()
    camino.pop()
    return False 
        
def maze_solver(filename):
    cell_size = 50
    cell_border = 2
    
    #Lectura del archivo de texto
    with open(filename,"r") as f:
        file = f.read()
    
    #Tamaño laberinto
    maze = file.split("\n")
    width = len(maze[0])
    height = len(maze)
    
    #Tamaño de imagen
    img_width = width*cell_size
    img_height = height*cell_size
    
    color = "black"
    
    #Create a blank canvas
    img = Image.new("RGBA",(img_width,img_height),color)
    draw = ImageDraw.Draw(img)
    
    #Resolviendo
    nodos = crear_nodos(maze)
    for i in nodos:
        if i.raiz:
            #print(f"Nodo Raiz : {i} \nAdyacentes: ")
            nodo_inicial = i
        elif i.meta:
            #print(f"Nodo Meta : {i} \nAdyacentes: ")
            nodo_meta = i
        else:
            pass
            #print(f"Nodo : {i} \nAdyacentes: ")
        #i.print_adyacentes()
        
    ruta = []
    qp = []
    solucion = dfs(nodo_inicial, nodo_meta,ruta, nodos)
    if solucion:
        for i in ruta[1:]:
            print(i)
            #qp.append(i.coords())
            
    
    
    #Colocando las cuadriculas
    for y in range(0, img_height, cell_size):
        for x in range(0, img_width, cell_size):
            top_left = (x,y)
            bottom_right = (x+cell_size-cell_border,y + cell_size - cell_border)
            caracter = maze[y//cell_size][x//cell_size]
            
            if caracter == '#':
                draw.rectangle([top_left, bottom_right], fill = "blue", outline=(0,0,0), width= cell_border)
            elif caracter == 'B':
                draw.rectangle([top_left, bottom_right], fill = "green", outline=(0,0,0), width= cell_border)
            elif caracter == 'A':
                draw.rectangle([top_left, bottom_right], fill = "red", outline=(0,0,0), width= cell_border)
            elif caracter == ' ':
                draw.rectangle([top_left, bottom_right], fill = "grey", outline=(0,0,0), width= cell_border)
                
    new_nodos = []
    nueva_ruta = []
    for i in ruta[1:]:            
        (y,x) = i.coords()
        top_left =(x*cell_size,y*cell_size)
        bottom_right = (x*cell_size+cell_size-cell_border,y*cell_size + cell_size - cell_border)
        draw.rectangle([top_left, bottom_right], fill = "white", outline=(0,0,0), width= cell_border)

    #print(qp)
    for y,x in qp:
        num_caminos = 0
        
    
    img.show()


    

#Poner nombre del archivo de texto
maze_solver("maze2.txt")
