import random
import math
import matplotlib.pyplot as plt
import heapq

class City:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def __str__(self):
        return f"City({self.label}, {self.x}, {self.y})"

def distance(city1, city2):
    return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)

def generate_random_cities(num_cities, x_limit, y_limit):
    letters = [chr(i) for i in range(65, 65 + num_cities)]
    cities = [City(random.uniform(0, x_limit), random.uniform(0, y_limit), letters[i]) for i in range(num_cities)]
    return cities

def shortest_links_first(vertexes):
    """Generates all links between cities, sorted by shortest distance."""
    links = [(A, B, distance(A, B)) for i, A in enumerate(vertexes) for B in vertexes[i+1:]]
    return sorted(links, key=lambda x: x[2])  # Ordenar por distancia

def mst(vertexes):
    """Construye el MST y retorna un diccionario {padre: [hijos]} que representa el árbol y el costo total del MST."""
    tree = {vertexes[0]: []}
    links = shortest_links_first(vertexes)
    mst_edges = []
    while len(tree) < len(vertexes):
        (A, B, dist) = next((A, B, dist) for (A, B, dist) in links if (A in tree) ^ (B in tree))
        if A not in tree: A, B = B, A
        tree[A].append(B)
        tree[B] = []
        mst_edges.append((A, B, dist))
    total_cost = sum(dist for _, _, dist in mst_edges)
    return tree, mst_edges, total_cost

def a_star_tsp(cities):
    """Implementa A* para resolver el TSP usando el costo del MST como heurística."""
    num_cities = len(cities)
    start_city = cities[0]
    open_set = [(0, start_city, [start_city])]

    while open_set:
        current_cost, current_city, path = heapq.heappop(open_set)

        # Si ya visitamos todas las ciudades, regresamos al inicio
        if len(path) == num_cities:
            return path + [start_city], current_cost + distance(current_city, start_city)

        # Ciudades no visitadas
        remaining_cities = [city for city in cities if city not in path]

        # Calculamos el MST solo sobre las ciudades restantes y obtenemos el costo total
        _, _, mst_heuristic = mst(remaining_cities)

        # Calculamos el costo mínimo desde current_city a cualquier ciudad en remaining_cities
        min_cost_to_mst = min(distance(current_city, next_city) for next_city in remaining_cities)

        # La heurística total es la suma del costo del MST y la distancia mínima a cualquier ciudad
        total_heuristic = mst_heuristic + min_cost_to_mst

        for next_city in remaining_cities:
            new_cost = current_cost + distance(current_city, next_city)
            total_cost = new_cost + total_heuristic  # Usar la heurística calculada
            heapq.heappush(open_set, (total_cost, next_city, path + [next_city]))

    return [], float('inf')  # En caso de que no se encuentre una solución

# Función de visualización y demás funciones omitidas por brevedad

# Parámetros de prueba
num_cities = 5
x_limit = 10
y_limit = 10

# Generar ciudades aleatorias
cities = generate_random_cities(num_cities, x_limit, y_limit)

# Resolver el TSP utilizando A* y MST como heurística
tsp_path, total_cost = a_star_tsp(cities)

# Imprimir el recorrido y el costo
print("Recorrido TSP:")
for city in tsp_path:
    print(city.label, end=" -> ")
print("\nCosto total:", total_cost)
