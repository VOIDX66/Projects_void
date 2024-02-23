import random
from tkinter import *
from tkinter import messagebox
#Constants
SEGMENT_SIZE = 5
DElAY = 100

#Variables
direction = "Right"
snake_body = [(20,15),(25,15),(30,15)]
coord_walls = []
food = (50,50)
collision_cont = 0
state = True

# Screen
screen = Tk()
screen.title("Snake Game")
screen.configure(width=500, height=500)

WIDTH_CANVAS = 500
HEIGHT_CANVAS = 500

canvas = Canvas(screen, width=WIDTH_CANVAS, height=HEIGHT_CANVAS)
canvas.pack()

def generate_segment(x,y,color):
    canvas.create_rectangle(x * SEGMENT_SIZE, y * SEGMENT_SIZE, ((x + 5) * SEGMENT_SIZE), ((y + 5) * SEGMENT_SIZE), fill= color)

def generate_random():
    num1 = random.randint(5,90)
    while num1 % SEGMENT_SIZE != 0:
        num1 = random.randint(5,90)
    num2 = random.randint(5,90)
    while num2 % SEGMENT_SIZE != 0:
        num2 = random.randint(5,90)
        
    coord = (num1,num2)
    return coord

def generate_food():
    global food
    coord = generate_random()
    while coord in snake_body:
        coord = generate_random()
    x,y = coord
    food = (x,y)

def generate_snake():
    canvas.delete("all")
    for x, y in snake_body:
        generate_segment(x,y,"green")
    generate_segment(food[0],food[1],"red")
    
    #Walls
    for x in range(0,WIDTH_CANVAS//SEGMENT_SIZE,5):
        generate_segment(0,x,"brown")
        generate_segment(95,x,"brown")
        temp = (0,x)
        coord_walls.append(temp)
        temp = (95,x)
        coord_walls.append(temp)
    for y in range(5,HEIGHT_CANVAS//SEGMENT_SIZE,5): 
        generate_segment(y,0,"brown")
        generate_segment(y,95,"brown")
        temp = (y,0)
        coord_walls.append(temp)
        temp = (y,95)
        coord_walls.append(temp)
        
    #Other walls
    generate_segment(20,20,"brown")
    temp = (20,20)
    coord_walls.append(temp)
    
    generate_segment(80,20,"brown")
    temp = (80,20)
    coord_walls.append(temp)
    
    generate_segment(20,80,"brown")
    temp = (20,80)
    coord_walls.append(temp)
    
    generate_segment(80,80,"brown")
    temp = (80,80)
    coord_walls.append(temp)
    
        
def snake_move():
    global direction, snake_body, coord_walls, collision_cont, state

    cx,cy = snake_body[0]
    s_up = (cx,cy-SEGMENT_SIZE)
    s_down =(cx,cy+SEGMENT_SIZE) 
    s_right =(cx+SEGMENT_SIZE,cy)
    s_left = (cx-SEGMENT_SIZE,cy)
    
    if direction == "Up":
        if s_up in coord_walls and s_right not in coord_walls and s_left not in coord_walls:
            if s_right == food:
                direction = "Right"
            elif s_left == food:
                direction = "Left"
            else:
                if s_right in snake_body:
                    direction = "Left"
                elif s_left in snake_body:
                    direction = "Right"
                else:           
                    directions = ("Right", "Left")
                    direction = random.choice(directions)
            
        elif s_up in coord_walls and s_right in coord_walls and s_left not in coord_walls:
            direction = "Left"
            
        elif s_up in coord_walls and s_right not in coord_walls and s_left in coord_walls:
            direction = "Right"
            
        elif s_up not in coord_walls and s_left in coord_walls and s_right not in coord_walls:
            if s_up == food:
                direction = "Up"
            elif s_right == food:
                direction = "Right"
            else:
                if s_up in snake_body:
                    direction = "Right"
                elif s_right in snake_body:
                    direction = "Up"
                else:           
                    directions = ("Up", "Right")
                    direction = random.choice(directions)
        
        elif s_up not in coord_walls and s_left not in coord_walls and s_right in coord_walls:
            if s_up == food:
                direction = "Up"
            elif s_left == food:
                direction = "Left"
            else:
                if s_up in snake_body:
                    direction = "Left"
                elif s_left in snake_body:
                    direction = "Up"
                else:            
                    directions = ("Up", "Left")
                    direction = random.choice(directions)
        
        elif s_up not in coord_walls and s_left not in coord_walls and s_right not in coord_walls:
            if s_up == food:
                direction = "Up"
            elif s_right == food:
                direction = "Right"
            elif s_left == food:
                direction = "Left"
            else:
                if s_up in snake_body:
                    if s_right in snake_body:
                        direction = "Left"
                    elif s_left in snake_body:
                        direction = "Right"
                    else:
                        directions = ("Right","Left")
                        direction = random.choice(directions)
                else:
                    if s_right in snake_body:
                        direction = "Left"
                    elif s_left in snake_body:
                        direction = "Right"
                    else:
                        directions = ("Up","Right","Left")
                        direction = random.choice(directions)
            
    elif direction == "Down":        
        if s_down in coord_walls and s_right not in coord_walls and s_left not in coord_walls:
            if s_right == food:
                direction = "Right"
            elif s_left == food:
                direction = "Left"
            else:
                if s_right in snake_body:
                    direction = "Left"
                elif s_left in snake_body:
                    direction = "Right"
                else:        
                    directions = ("Right", "Left")
                    direction = random.choice(directions)
            
        elif s_down in coord_walls and s_right in coord_walls and s_left not in coord_walls:
            direction = "Left"
            
        elif s_down in coord_walls and s_right not in coord_walls and s_left in coord_walls:
            direction = "Right"
            
        elif s_down not in coord_walls and s_left in coord_walls and s_right not in coord_walls:
            if s_down == food:
                direction = "Down"
            elif s_right == food:
                direction = "Right"
            else:
                if s_down in snake_body:
                    direction = "Right"
                elif s_right in snake_body:
                    direction = "Down"
                else:        
                    directions = ("Down", "Right")
                    direction = random.choice(directions)
        
        elif s_down not in coord_walls and s_left not in coord_walls and s_right in coord_walls:
            if s_down == food:
                direction = "Down"
            elif s_left == food:
                direction = "Left"
            else:
                if s_down in snake_body:
                    direction = "Left"
                elif s_left in snake_body:
                    direction = "Down"
                else:            
                    directions = ("Down", "Left")
                    direction = random.choice(directions)
        
        elif s_down not in coord_walls and s_left not in coord_walls and s_right not in coord_walls:
            if s_down == food:
                direction = "Down"
            elif s_right == food:
                direction = "Right"
            elif s_left == food:
                direction = "Left"
            else:
                if s_down in snake_body:
                    if s_right in snake_body:
                        direction = "Left"
                    elif s_left in snake_body:
                        direction = "Right"
                    else:
                        directions = ("Right","Left")
                        direction = random.choice(directions)
                else:
                    if s_right in snake_body:
                        direction = "Left"
                    elif s_left in snake_body:
                        direction = "Right"
                    else:        
                        directions = ("Down", "Right","Left")
                        direction = random.choice(directions)
            
    elif direction == "Right":
        if s_right in coord_walls and s_up not in coord_walls and s_down not in coord_walls:
            if s_right == food:
                direction = "Right"
            elif s_down == food:
                direction = "Down"
            else:
                if s_up in snake_body:
                    direction = "Down"
                elif s_down in snake_body:    
                    direction = "Up"
                else:    
                    directions = ("Up", "Down")
                    direction = random.choice(directions)
            
        elif s_right in coord_walls and s_up not in coord_walls and s_down in coord_walls:
            direction = "Up"
            
        elif s_right in coord_walls and s_up in coord_walls and s_down not in coord_walls:
            direction ="Down"
        
        elif s_right not in coord_walls and s_up in coord_walls and s_down not in coord_walls:
            if s_right == food:
                direction = "Right"
            elif s_down == food:
                direction = "Down"
            else:
                if s_right in snake_body:
                    direction = "Down"
                elif s_down in snake_body:
                    direction = "Right"
                else:    
                    directions = ("Right", "Down")
                    direction = random.choice(directions)
        
        elif s_right not in coord_walls and s_up not in coord_walls and s_down in coord_walls:
            if s_right == food:
                direction = "Right"
            elif s_up == food:
                direction = "Up"
            else:
                if s_right in snake_body:
                    direction = "Up"
                elif s_up in snake_body:
                    direction = "Right"
                else:    
                    directions = ("Right", "Up")
                    direction = random.choice(directions)
        
        elif s_right not in coord_walls and s_up not in coord_walls and s_down not in coord_walls:
            if s_right == food:
                direction = "Right"
            elif s_up == food:
                direction = "Up"
            elif s_down == food:
                direction = "Down"
            else:
                if s_right in snake_body:
                    if s_up in snake_body:
                        direction = "Down"
                    elif s_down in snake_body:
                        direction = "Up"
                    else:
                        directions = ("Up","Down")
                        direction = random.choice(directions)
                else:
                    if s_up in snake_body:
                        direction = "Down"
                    elif s_down in snake_body:
                        direction = "Up"
                    else:
                        directions = ("Right","Up","Down")
                        direction = random.choice(directions)  
            
    elif direction == "Left":
        if s_left in coord_walls and s_up not in coord_walls and s_down not in coord_walls:
            if s_left == food:
                direction = "Left"
            elif s_down == food:
                direction = "Down"
            else:
                if s_up in snake_body:
                    direction = "Down"
                elif s_down in snake_body:
                    direction = "Up"
                else:    
                    directions = ("Up", "Down")
                    direction = random.choice(directions)
            
        elif s_left in coord_walls and s_up not in coord_walls and s_down in coord_walls:
            direction = "Up"
            
        elif s_left in coord_walls and s_up in coord_walls and s_down not in coord_walls:
            direction ="Down"

        elif s_left not in coord_walls and s_up not in coord_walls and s_down in coord_walls:
            if s_left == food:
                direction = "Left"
            elif s_up == food:
                direction = "Up"
            else:
                if s_left in snake_body:
                    direction = "Up"
                elif s_up in snake_body:
                    direction = "Left"
                else:              
                    directions = ("Left", "Up")
                    direction = random.choice(directions)
        
        elif s_left not in coord_walls and s_up in coord_walls and s_down not in coord_walls:
            if s_left == food:
                direction = food
            elif s_down == food:
                direction = "Down"
            else:
                if s_left in snake_body:
                    direction = "Down"
                elif s_down in snake_body:
                    direction = "Left"
                else:        
                    directions = ("Left", "Down")
                    direction = random.choice(directions)
        
        elif s_left not in coord_walls and s_up not in coord_walls and s_down not in coord_walls:
            if s_left == food:
                direction = "Left"
            elif s_up == food:
                direction = "Up"
            elif s_down == food:
                direction = "Down"
            else:
                if s_left in snake_body:
                    if s_up in snake_body:
                        direction = "Down"
                    elif s_down in snake_body:
                        direction = "Up"
                    else:
                        directions = ("Up", "Down")
                        direction = random.choice(directions)
                else:
                    if s_up in snake_body:
                        direction = "Down"
                    elif s_down in snake_body:
                        direction = "Up"
                    else:
                        directions = ("Left", "Up", "Down")
                        direction = random.choice(directions)                                
            
    for segement in snake_body[:1]:
        if segement in coord_walls:
            coord_walls.remove(segement)
        
    head_x, head_y = snake_body[0]
    new_head = None
    
    if direction == "Right":
        new_head = (head_x + 5, head_y)
    elif direction == "Left":
        new_head = (head_x - 5, head_y)
    elif direction == "Up":
        new_head = (head_x, head_y - 5)
    elif direction == "Down":
        new_head = (head_x, head_y + 5)
    
    for segment in snake_body[1:]:
        if segment == new_head:
            collision_cont+=1
            print(collision_cont)
            print(direction)
            #if collision_cont > 1:
            #    messagebox.showinfo(title="GAME OVER", message="You lose!!!")
            #    screen.quit()
            #    state = False
            #    break
    
    for brick in coord_walls:
        if brick == new_head:
            messagebox.showinfo(title="GAME OVER", message="You lose!!!")
            screen.quit()
            state = False
            break
       
    snake_body.insert(0, new_head)
    
    if new_head == food:
        generate_food()
    else:
        del snake_body[-1] 
    generate_snake()

def change_direction(new_direction):
    global direction
    
    if new_direction == "Right" and direction != "Left":
        direction = new_direction
    elif new_direction == "Left" and direction != "Right":
        direction = new_direction
    elif new_direction == "Up" and direction != "Down":
        direction = new_direction
    elif new_direction == "Down" and direction != "Up":
        direction = new_direction
    
def refresh_game():
    if state == True:
        snake_move()
        screen.after(DElAY, refresh_game)
        
#Events
screen.bind("<KeyPress>", lambda event: change_direction(event.keysym))

generate_snake()
refresh_game()       
screen.mainloop()