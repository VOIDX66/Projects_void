import random
import math
import matplotlib.pyplot as plt

class City:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label  # Nueva propiedad para almacenar la letra de la ciudad

    def __str__(self):
        return f"City({self.label}, {self.x}, {self.y})"

def distance(city1, city2):
    return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)

def generate_random_cities(num_cities, x_limit, y_limit, num_connections):
    # Generar letras para las ciudades
    letters = [chr(i) for i in range(65, 65 + num_cities)]  # Letras A, B, C, ...
    cities = [City(random.uniform(0, x_limit), random.uniform(0, y_limit), letters[i]) for i in range(num_cities)]
    neighbors = {i: [] for i in range(num_cities)}

    # Conectar cada ciudad con varios vecinos cercanos
    for i in range(num_cities):
        # Calcular las distancias a todas las otras ciudades
        distances = [(j, distance(cities[i], cities[j])) for j in range(num_cities) if i != j]
        # Ordenar por distancia
        distances.sort(key=lambda x: x[1])

        # Conectar con un número específico de ciudades cercanas
        for j in range(min(num_connections, len(distances))):
            neighbor_index = distances[j][0]
            if neighbor_index not in neighbors[i]:  # Evitar duplicados
                neighbors[i].append(neighbor_index)
            # Asegurarse de que la conexión sea bidireccional
            if i not in neighbors[neighbor_index]:
                neighbors[neighbor_index].append(i)

    return cities, neighbors

def plot_cities(cities, start_index, end_index, neighbors):
    # Extraer coordenadas de las ciudades
    x_coords = [city.x for city in cities]
    y_coords = [city.y for city in cities]

    # Plotear todas las ciudades
    plt.scatter(x_coords, y_coords, color='blue', label='Cities')

    # Resaltar la ciudad inicial y la ciudad de destino
    plt.scatter(cities[start_index].x, cities[start_index].y, color='green', label='Start City', s=100)
    plt.scatter(cities[end_index].x, cities[end_index].y, color='red', label='End City', s=100)

    # Conectar las ciudades de acuerdo a los vecinos
    for i, city_neighbors in neighbors.items():
        for neighbor in city_neighbors:
            plt.plot([cities[i].x, cities[neighbor].x], 
                     [cities[i].y, cities[neighbor].y], 
                     color='gray', linestyle='--', alpha=0.5)

    # Añadir etiquetas de letras a las ciudades
    for city in cities:
        plt.text(city.x, city.y, city.label, fontsize=12, ha='right')

    # Etiquetas y leyenda
    plt.title('Random Cities for TSP Problem with Bidirectional Connections')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.show()

# Parámetros
num_cities = 5        # Número de ciudades a generar
x_limit = 100         # Límite en el eje X
y_limit = 100         # Límite en el eje Y
start_index = random.randint(0, num_cities - 1)  # Índice de la ciudad inicial
end_index = random.randint(0, num_cities - 1)    # Índice de la ciudad de destino
while start_index == end_index:
    end_index = random.randint(0, num_cities - 1)
num_connections = 3  # Número máximo de conexiones por ciudad

# Generar ciudades aleatorias y sus vecinos
cities, neighbors = generate_random_cities(num_cities, x_limit, y_limit, num_connections)

# Imprimir los vecinos de cada ciudad
for city_index, city_neighbors in neighbors.items():
    print(f"Neighbors of City {cities[city_index].label}: {', '.join(cities[neighbor].label for neighbor in city_neighbors)}")

# Graficar las ciudades
plot_cities(cities, start_index, end_index, neighbors)
