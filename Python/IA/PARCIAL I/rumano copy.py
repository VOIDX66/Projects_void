import heapq
import math
import matplotlib.pyplot as plt

# Creación de nodos con coordenadas x, y
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Leemos los datos de las ciudades del archivo de texto
def read_cities(filename):
    cities = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            city_name = data[0]
            x, y = float(data[1]), float(data[2])
            cities[city_name] = Node(x, y)
    return cities

# Definimos la heurística para nuestro algoritmo A*
def heuristic(city_name, goal_name, heuristics):
    return heuristics.get(city_name, 0)

def cost_manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def neighbors(node, graph):
    return graph.get(node, [])

# Implementación de A* con heurística
def astar(start_name, goal_name, cities, graph, heuristics):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start_name, goal_name, heuristics), 0, start_name))
    came_from = {}
    cost_so_far = {}
    
    came_from[start_name] = None
    cost_so_far[start_name] = 0
    
    while open_list:
        _, current_cost, current = heapq.heappop(open_list)
        
        if current == goal_name:
            break
        
        city_neighbors = neighbors(current, graph)
        
        for next in city_neighbors:
            new_cost = cost_so_far.get(current, 0) + cost_manhattan(cities[current], cities[next])
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal_name, heuristics)
                heapq.heappush(open_list, (priority, new_cost, next))
                came_from[next] = current
    
    return came_from, cost_so_far

# Costo Uniforme
def costo_uniforme(start_name, goal_name, cities, graph):
    open_list = []
    heapq.heappush(open_list, (0, start_name))
    came_from = {}
    cost_so_far = {}
    
    came_from[start_name] = None
    cost_so_far[start_name] = 0
    
    while open_list:
        current_cost, current = heapq.heappop(open_list)
        
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
    
    for city, neighbors in graph.items():
        for neighbor in neighbors:
            x_values = [cities[city].x, cities[neighbor].x]
            y_values = [cities[city].y, cities[neighbor].y]
            ax.plot(x_values, y_values, color='gray', zorder=1)
    
    for i in range(len(ucs_path) - 1):
        x_values = [cities[ucs_path[i]].x, cities[ucs_path[i + 1]].x]
        y_values = [cities[ucs_path[i]].y, cities[ucs_path[i + 1]].y]
        ax.plot(x_values, y_values, color='green', linewidth=2, zorder=4, label='Costo Uniforme (Manhattan)' if i == 0 else "")

    for i in range(len(astar_path) - 1):
        x_values = [cities[astar_path[i]].x, cities[astar_path[i + 1]].x]
        y_values = [cities[astar_path[i]].y, cities[astar_path[i + 1]].y]
        ax.plot(x_values, y_values, color='blue', linewidth=2, zorder=4, label='A* (Euclidiana)' if i == 0 else "")
    
    for city, node in cities.items():
        ax.scatter(node.x, node.y, color='red', zorder=2)
        ax.text(node.x + 2, node.y, city, fontsize=10, zorder=3)
    
    ax.set_aspect('equal')
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    filename = 'ciudades.txt'
    cities = read_cities(filename)
    
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

    heuristics = {
        'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Dobreta': 242,
        'Eforie': 161,
        'Fagaras': 178,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 98,
        'Rimnicu_Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374
    }

    start_city, goal_city = "Arad", "Bucharest"
    
    astar_came_from, astar_cost_so_far = astar(start_city, goal_city, cities, graph, heuristics)
    ucs_came_from, ucs_cost_so_far = costo_uniforme(start_city, goal_city, cities, graph)
    
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
    print("Camino Costo Uniforme (Manhattan): ", ucs_path)
    
    draw_graph(cities, graph, astar_path, ucs_path)
