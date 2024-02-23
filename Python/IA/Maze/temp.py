from PIL import Image, ImageDraw

def flood_fill(laberinto, entrada, salida):
    """
    Encuentra una solución al laberinto utilizando el algoritmo Flood Fill.

    Args:
        laberinto: Matriz bidimensional de caracteres que representa el laberinto.
        entrada: Tupla (y, x) que representa la posición de la entrada.
        salida: Tupla (y, x) que representa la posición de la salida.

    Returns:
        True si se encuentra una solución, False en caso contrario.
    """

    # Marcar la entrada como visitada
    laberinto[entrada[0]][entrada[1]] = "V"

    # Pila para almacenar las casillas por explorar
    pila = [entrada]

    while pila:
        # Obtener la última casilla de la pila
        actual = pila.pop()

        # Si es la salida, se ha encontrado una solución
        if actual == salida:
            return True

        # Recorrer los vecinos adyacentes
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            y = actual[0] + dy
            x = actual[1] + dx

            # Validar si el vecino está dentro del laberinto y no está visitado
            if 0 <= y < len(laberinto) and 0 <= x < len(laberinto[0]) and laberinto[y][x] != "#":
                # Marcar el vecino como visitado
                laberinto[y][x] = "V"
                # Agregar el vecino a la pila para su posterior exploración
                pila.append((y, x))

    # No se ha encontrado una solución
    return False
        
def maze_solver(filename):
    cell_size = 50
    cell_border = 2
    
    #Lectura del archivo de texto
    maze = []
    with open(filename,"r") as f:
        for linea in f:
            maze.append(list(linea.strip("\n")))
    
    print(maze)
    #Tamaño laberinto
    width = len(maze[0])
    height = len(maze)

    
    #Tamaño de imagen
    img_width = width*cell_size
    img_height = height*cell_size
    
    color = "black"
    
    #Create a blank canvas
    img = Image.new("RGBA",(img_width,img_height),color)
    draw = ImageDraw.Draw(img)
    
    
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
                salida = (y//cell_size,x//cell_size)
            elif caracter == 'A':
                draw.rectangle([top_left, bottom_right], fill = "red", outline=(0,0,0), width= cell_border)
                entrada = (y//cell_size,x//cell_size)
            elif caracter == ' ':
                draw.rectangle([top_left, bottom_right], fill = "grey", outline=(0,0,0), width= cell_border)
    
    if flood_fill(maze, entrada, salida):
        for fila in maze:
            print("".join(fila))
        else:
            print("No se encontró una solución")

    img.show()

#Poner nombre del archivo de texto
maze_solver("maze1.txt")
