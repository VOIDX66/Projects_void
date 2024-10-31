import heapq #Uso de colas de prioridad
import math #Para ejecutar correctamente las operaciones de costo e heuristica
import matplotlib.pyplot as plt # Usada para graficar

#Creacion de nodos con coordenadas x, y
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Leemos los datos de las ciudades del archivo de texto
def read_citys(filename):
    cities = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            city_name = data[0]
            x, y = float(data[1]), float(data[2])
            cities[city_name] = Node(x, y)
    return cities

#Definimos la euristica para nuestro algoritmo A* 
'''
METER AQUI EL ARBOL DE EXPANSION MINIMA
'''
def heuristic(a, b):
    #Usando Euclidiana
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def neighbors(node, graph):
    return graph[node]

# Implementación de A* NOS VASAMOS EN LA HEURISTICA
def astar(start_name, goal_name, cities, graph):
    open_list = []
    #Añadimos el nodo inicial, con la prioridad basada en la heurisica
    heapq.heappush(open_list, (0 + heuristic(cities[start_name], cities[goal_name]), 0, start_name))
    came_from = {} #Diccionario para rastrear el camino
    cost_so_far = {} #Diccionario para rastrear costo acumulado a cada nodo
    
    came_from[start_name] = None #El nodo inicial no tiene un prodecesor
    cost_so_far[start_name] = 0 #El costo para llegar al nodo inicial es 0 (esta sobre si mismo)
    
    while open_list:
        _, current_cost, current = heapq.heappop(open_list)
        
        #Si llegamos al destino detenemos el ciclo
        if current == goal_name:
            break
        
        #Obtenemos las ciudades vecinas de cada nodo
        city_neighbors = neighbors(current, graph)
        
        for next in city_neighbors:
            new_cost = cost_so_far[current] + heuristic(cities[current], cities[next])

            # Si el vecino no ha sido visitado o encontramos un costo menor, actualizamos
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # Calcula la prioridad como el costo total estimado (costo acumulado + heurística)s
                priority = new_cost + heuristic(cities[next], cities[goal_name])
                heapq.heappush(open_list, (priority, new_cost, next))
                came_from[next] = current # Se registra el predecesor del vecino
    
    return came_from, cost_so_far
