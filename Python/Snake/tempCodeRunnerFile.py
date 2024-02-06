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
    print(new_head)    
    snake_body.insert(0, new_head)
    
    if new_head == food:
        generate_food()
    else:
        del snake_body[-1]
            
    generate_snake()