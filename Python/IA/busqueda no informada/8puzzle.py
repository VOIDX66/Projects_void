'''
8 puzzle problem, a smaller version of the fifteen puzzle:
http://en.wikipedia.org/wiki/Fifteen_puzzle
States are defined as string representations of the pieces on the puzzle.
Actions denote what piece will be moved to the empty space.

States must allways be inmutable. We will use strings, but internally most of
the time we will convert those strings to lists, which are easier to handle.
For example, the state (string):

'1-2-3
 4-5-6
 7-8-e'

will become (in lists):

[['1', '2', '3'],
 ['4', '5', '6'],
 ['7', '8', 'e']]

'''

from __future__ import print_function

from simpleai.search import astar, SearchProblem
from simpleai.search.viewers import WebViewer
from turtle import Turtle
import time


GOAL = '''1-2-3
4-5-6
7-8-e'''

INITIAL = '''4-1-2
7-e-3
8-5-6'''


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def find_location(rows, element_to_find):
    '''Find the location of a piece in the puzzle.
       Returns a tuple: row, column'''
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


# we create a cache for the goal position of each piece, so we don't have to
# recalculate them every time
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in '12345678e':
    goal_positions[number] = find_location(rows_goal, number)


class EigthPuzzleProblem(SearchProblem):
    def actions(self, state):
        '''Returns a list of the pieces we can move to the empty space.'''
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')

        actions = []
        if row_e > 0:
            actions.append(rows[row_e - 1][col_e])
        if row_e < 2:
            actions.append(rows[row_e + 1][col_e])
        if col_e > 0:
            actions.append(rows[row_e][col_e - 1])
        if col_e < 2:
            actions.append(rows[row_e][col_e + 1])

        return actions

    def result(self, state, action):
        '''Return the resulting state after moving a piece to the empty space.
           (the "action" parameter contains the piece to move)
        '''
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')
        row_n, col_n = find_location(rows, action)

        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]

        return list_to_string(rows)

    def is_goal(self, state):
        '''Returns true if a state is the goal state.'''
        return state == GOAL

    def cost(self, state1, action, state2):
        '''Returns the cost of performing an action. No useful on this problem, i
           but needed.
        '''
        return 1

    def heuristic(self, state):
        '''Returns an *estimation* of the distance from a state to the goal.
           We are using the manhattan distance.
        '''
        rows = string_to_list(state)

        hamming = 0

        for number in '12345678e':
            row_n, col_n = find_location(rows, number)
            row_n_goal, col_n_goal = goal_positions[number]
            if row_n_goal != row_n or col_n_goal != col_n:
                hamming += 1

        return hamming


result = astar(EigthPuzzleProblem(INITIAL))
# if you want to use the visual debugger, use this instead:
#result = astar(EigthPuzzleProblem(INITIAL), viewer=WebViewer())


for action, state in result.path():
    #print('Move number', action)
    #print(state)
    pass

# Crear dos tortugas: una para las casillas y otra para los números
t_casillas = Turtle()
t_numeros = Turtle()

# Configurar la pantalla
t_casillas.screen.title("Animación del 8 Puzzle")
t_casillas.screen.setup(width=400,height=400)
t_casillas.hideturtle()
t_numeros.hideturtle()

# Hacer que el dibujo sea más lento y fluido
t_casillas.speed(3)  # Ajustar la velocidad de la tortuga (1 = más lento, 10 = rápido)
t_numeros.speed(3)   # Ajustar la velocidad de la tortuga de los números

size = 100  # Tamaño de cada casilla
x_start = -size * 1.5  # Coordenada inicial x
y_start = size * 1.5   # Coordenada inicial y

# Función para convertir el formato de cadena en una lista bidimensional
def convertir_a_tablero(cadena):
    filas = cadena.split('\n')  # Dividir la cadena en filas
    tablero = [fila.split('-') for fila in filas]  # Dividir cada fila en columnas
    return tablero

# Función para dibujar una casilla sin cambiar el número
def dibujar_casillas_estaticas(color_fill="lightblue"):
    t_casillas.pencolor("black")  # Color del borde
    t_casillas.fillcolor(color_fill)  # Color de relleno
    for i in range(3):
        for j in range(3):
            x = x_start + j * size
            y = y_start - i * size
            t_casillas.penup()
            t_casillas.goto(x, y)
            t_casillas.pendown()
            t_casillas.begin_fill()
            for _ in range(4):
                t_casillas.forward(size)
                t_casillas.right(90)
            t_casillas.end_fill()

# Función para actualizar los números en las casillas
def actualizar_numeros(tablero, color="black"):
    t_numeros.clear()  # Limpiar solo los números
    t_numeros.pencolor(color)  # Establecer el color de los números
    for i, fila in enumerate(tablero):
        for j, val in enumerate(fila):
            x = x_start + j * size + size / 2
            y = y_start - i * size - size / 2 - 10  # Ajustar y para bajar los números un poco
            t_numeros.penup()
            t_numeros.goto(x, y)
            t_numeros.write(val, align="center", font=("Times New Roman", 30, "normal"))

# Dibujar las casillas estáticas al principio con un color de relleno específico
dibujar_casillas_estaticas(color_fill="lightgreen")  # Puedes cambiar el color de relleno aquí

# Dibujar la animación paso a paso, cambiando solo los números
for movimiento in result.path():
    numero, cadena_tablero = movimiento
    tablero = convertir_a_tablero(cadena_tablero)  # Convertir cadena a tablero
    actualizar_numeros(tablero, color="black")  # Aquí puedes cambiar el color a tu preferencia
    
    if numero:
        print(f"Move number {numero}")  # Imprimir el número del movimiento
    
    time.sleep(1.5)  # Pausa más larga para hacer la animación más lenta y fluida

# Mantener la ventana abierta
t_casillas.screen.mainloop()
