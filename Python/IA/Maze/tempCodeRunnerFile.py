for y in range(0, img_height, cell_size):
        for x in range(0, img_width, cell_size):
            top_left = (x,y)
            bottom_right = (x+cell_size-cell_border,y + cell_size - cell_border)
            caracter = maze[y//cell_size][x//cell_size]
            
            if caracter == '#':
                draw.rectangle([top_left, bottom_right], fill = "blue", outline=(0,0,0), width= cell_border)
            elif caracter == 'B':
                draw.rectangle([top_left, bottom_right], fill = "green", outline=(0,0,0), width= cell_border)
                salida = (x//cell_size,y//cell_size)
            elif caracter == 'A':
                draw.rectangle([top_left, bottom_right], fill = "red", outline=(0,0,0), width= cell_border)
                entrada = (x//cell_size,y//cell_size)
            elif caracter == ' ':
                draw.rectangle([top_left, bottom_right], fill = "grey", outline=(0,0,0), width= cell_border)