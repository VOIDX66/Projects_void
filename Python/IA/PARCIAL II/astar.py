import random
import math
import heapq
import time

# Clase City
class City:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def __lt__(self, other):  # Define less than for City objects
        return (self.x, self.y) < (other.x, other.y)

    def __str__(self):
        return f"City({self.label}, {self.x}, {self.y})"

    def __hash__(self):
        return ord(self.label)  # Usamos el label como hash (basado en su valor ASCII)

    def __eq__(self, other):
        return self.label == other.label  # Comparar ciudades por su label

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Función para generar ciudades aleatorias
def generate_random_cities(num_cities, x_limit, y_limit):
    letters = [chr(i) for i in range(65, 65 + num_cities)]  # Etiquetas de las ciudades ('A', 'B', ...)
    cities = [City(random.randint(0, x_limit), random.randint(0, y_limit), letters[i]) for i in range(num_cities)]
    return cities

# Heurística basada en el MST
def mst_heuristic(cities, visited):
    unvisited = [city for city in cities if city not in visited]
    if len(unvisited) == 0:
        return 0

    total_cost = 0
    selected_city = visited[-1]  # Empezamos desde la última ciudad visitada
    while unvisited:
        min_dist = float('inf')
        next_city = None
        for city in unvisited:
            dist = selected_city.distance(city)
            if dist < min_dist:
                min_dist = dist
                next_city = city

        total_cost += min_dist
        unvisited.remove(next_city)
        selected_city = next_city

    return total_cost

# Inicialización de feromonas (ACO)
def initialize_pheromones(num_cities):
    pheromones = {city.label: {other.label: 1 for other in cities if other != city} for city in cities}
    return pheromones

# Actualización de feromonas (ACO)
def update_pheromones(pheromones, all_paths, rho, cities):
    # Actualizar feromonas de acuerdo a los caminos encontrados
    for city in pheromones:
        for neighbor in pheromones[city]:
            pheromones[city][neighbor] *= (1 - rho)

    for path, cost in all_paths:
        pheromone_deposit = 1 / cost
        for i in range(len(path) - 1):
            current_city = path[i]
            next_city = path[i + 1]

            # Usamos los labels de las ciudades como índices en lugar de objetos City
            pheromones[current_city.label][next_city.label] += pheromone_deposit
            pheromones[next_city.label][current_city.label] += pheromone_deposit  # Camino bidireccional

# A* con heurística MST y ACO combinada
def a_star_tsp(cities, num_ants=10, alpha=1, beta=2, rho=0.1, max_iter=100):
    num_cities = len(cities)
    pheromones = initialize_pheromones(num_cities)

    def a_star_search(start_city, pheromones, alpha, beta):
        open_set = []
        heapq.heappush(open_set, (0 + mst_heuristic(cities, [start_city]), 0, start_city, [start_city], [start_city]))

        while open_set:
            _, g, current_city, visited, path = heapq.heappop(open_set)

            if len(visited) == num_cities:
                return path + [cities[0]], g + current_city.distance(start_city)  # Regresar a la ciudad de inicio

            for neighbor in cities:
                if neighbor not in visited:
                    new_visited = visited.copy()
                    new_visited.append(neighbor)  # Añadir la ciudad al recorrido (cambiar de set a list)
                    new_path = path.copy()
                    new_path.append(neighbor)

                    new_g = g + current_city.distance(neighbor)
                    mst_h = mst_heuristic(cities, new_visited)
                    aco_h = mst_heuristic(cities, new_visited)  # Combinamos MST y ACO aquí

                    # Usamos una combinación de ambas heurísticas para guiar A*
                    h = mst_h + aco_h

                    # Añadimos al open set
                    heapq.heappush(open_set, (new_g + h, new_g, neighbor, new_visited, new_path))

        return None, float('inf')  # Si no se encuentra un camino

    best_path = None
    best_cost = float('inf')

    start_city = cities[0]  # Comenzamos siempre con la ciudad A (primer ciudad)

    for _ in range(max_iter):
        all_paths = []
        for _ in range(num_ants):
            path, cost = a_star_search(start_city, pheromones, alpha, beta)

            if path and cost < best_cost:
                best_path = path
                best_cost = cost

            if path:
                all_paths.append((path, cost))

        update_pheromones(pheromones, all_paths, rho, cities)

    return best_path, best_cost

# Ejemplo de uso
cities = generate_random_cities(20, 100, 100)
start_time = time.time()
best_path, best_cost = a_star_tsp(cities)
end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time)
print("Mejor camino encontrado:", [city.label for city in best_path])
print("Costo:", best_cost)
