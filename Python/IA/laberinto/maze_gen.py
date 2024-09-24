from PIL import Image, ImageDraw
import os

def draw_maze(filename):
    cell_size = 50
    cell_border = 2
    #Lectura del archivo del laberinto
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

    #Colocando las cuadriculas
    for y in range(0, img_height, cell_size):
        for x in range(0, img_width, cell_size):
            top_left = (x,y)
            bottom_right = (x+cell_size-cell_border,y + cell_size - cell_border)
            caracter = maze[y//cell_size][x//cell_size]
            
            if caracter == '1':
                draw.rectangle([top_left, bottom_right], fill = "blue", outline=(0,0,0), width= cell_border)
            elif caracter == '0':
                draw.rectangle([top_left, bottom_right], fill = "grey", outline=(0,0,0), width= cell_border)
    img.show()

draw_maze("maze1.txt")
draw_maze("maze2.txt")
draw_maze("maze3.txt")