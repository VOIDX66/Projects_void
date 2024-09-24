#Parcial 1 Jaider Alberto Rendon Moreno
#En la linea 157 se pueden cambiar las ciudades
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
def heuristic(a, b):
    #Usando Euclidiana
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

# Costo para Costo Uniforme
def cost_manhattan(a, b):
    #Usando Manhattan
    return abs(a.x - b.x) + abs(a.y - b.y)

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

# Costo Uniforme COSTO ACUMULADO
def costo_uniforme(start_name, goal_name, cities, graph):
    open_list = []
    #Añadimos el nodo incial con el costo de 0
    heapq.heappush(open_list, (0, start_name))
    came_from = {}
    cost_so_far = {}
    
    came_from[start_name] = None
    cost_so_far[start_name] = 0
    
    while open_list:
        current_cost, current = heapq.heappop(open_list)
        
        #Si llegamos al destino detenemos el ciclo
        if current == goal_name:
            break
        
        city_neighbors = neighbors(current, graph)
        
        for next in city_neighbors:
            new_cost = cost_so_far[current] + cost_manhattan(cities[current], cities[next])
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heapq.heappush(open_list, (new_cost, next))
                came_from[next] = current
    
    return came_from, cost_so_far

# Función para dibujar el grafo con ambos caminos: A* y Costo Uniforme
def draw_graph(cities, graph, astar_path, ucs_path):
    fig, ax = plt.subplots()
    
    # Dibujar conexiones entre ciudades
    for city, neighbors in graph.items():
        for neighbor in neighbors:
            x_values = [cities[city].x, cities[neighbor].x]
            y_values = [cities[city].y, cities[neighbor].y]
            ax.plot(x_values, y_values, color='gray', zorder=1)
    
    # Dibujar el camino de Costo Uniforme en verde
    for i in range(len(ucs_path) - 1):
        x_values = [cities[ucs_path[i]].x, cities[ucs_path[i + 1]].x]
        y_values = [cities[ucs_path[i]].y, cities[ucs_path[i + 1]].y]
        ax.plot(x_values, y_values, color='green', linewidth=2, zorder=4, label='Costo Uniforme (Manhattan)' if i == 0 else "")

    # Dibujar el camino de A* en azul
    for i in range(len(astar_path) - 1):
        x_values = [cities[astar_path[i]].x, cities[astar_path[i + 1]].x]
        y_values = [cities[astar_path[i]].y, cities[astar_path[i + 1]].y]
        ax.plot(x_values, y_values, color='blue', linewidth=2, zorder=4, label='A* (Euclidiana)' if i == 0 else "")
    
    # Dibujar las ciudades como puntos
    for city, node in cities.items():
        ax.scatter(node.x, node.y, color='red', zorder=2)
        ax.text(node.x + 2, node.y, city, fontsize=10, zorder=3)
    
    ax.set_aspect('equal')
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    filename = 'ciudades.txt'
    cities = read_citys(filename)
    
    # Grafo de conexiones entre ciudades
    graph = {
        'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
        'Zerind': ['Arad', 'Oradea'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Sibiu': ['Arad', 'Oradea', 'Rimnicu_Vilcea', 'Fagaras'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Dobreta'],
        'Dobreta': ['Mehadia', 'Craiova'],
        'Craiova': ['Dobreta', 'Pitesti', 'Rimnicu_Vilcea'],
        'Rimnicu_Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Pitesti': ['Rimnicu_Vilcea', 'Craiova', 'Bucharest'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu'],
        'Urziceni' : ['Bucharest', 'Vaslui', 'Hirsova'],
        'Hirsova': ['Eforie'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']
    }
    
    #Definimos la ciudad de inicio y la ciudad destino--------------------------------------------------------
    start_city, goal_city = "Arad", "Bucharest"
    #----------------------------------------------------------------------------------------------------------

    # Ejecutar A*
    astar_came_from, astar_cost_so_far = astar(start_city, goal_city, cities, graph)
    
    # Ejecutar Costo Uniforme
    ucs_came_from, ucs_cost_so_far = costo_uniforme(start_city, goal_city, cities, graph)
    
    # Recuperar los caminos
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = []
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path
    
    astar_path = reconstruct_path(astar_came_from, start_city, goal_city)
    ucs_path = reconstruct_path(ucs_came_from, start_city, goal_city)
    
    print("Camino A* (Euclidiana): ", astar_path)
    print("Camino Costo Uniforme (Manhatan): ", ucs_path)
    
    # Dibujar el grafo con ambos caminos
    draw_graph(cities, graph, astar_path, ucs_path)

    #En la linea 157 se pueden cambiar las ciudades
