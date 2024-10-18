import matplotlib.pyplot as plt
import numpy as np
import random
import vrplib

from copy import deepcopy
from dataclasses import dataclass
from rich import print

@dataclass
class Problem:
  pass  

@dataclass
class City:
  name: str
  loc: complex
  demand: float

  def __repr__(self):
    return self.name

  def distance(self, city):
    if isinstance(city, City):
        return abs(self.loc - city.loc)

  @property
  def x(self):
    return self.loc.real

  @property
  def y(self):
    return self.loc.imag

def color():
  return random.choice('bgrcmyk')

def tour_length(tour):
  # Calcula la distancia total entre ciudades en el recorrido.
  return sum(tour[i].distance(tour[i-1]) for i in range(len(tour)))

def plot_vrp(tour):
  plt.clf()
  for route in tour:
    plot_tour(route)
  plt.show()

def plot_tour(tour):
  start = tour[0]
  # Dibuja el recorrido de las ciudades, marcando el punto de inicio.
  plot_lines(tour + [tour[0]], '%so-' % color())
  plot_lines([start], 'rs')

def plot_lines(points, style='bo-'):
  # Dibuja líneas entre puntos y etiqueta las ciudades.
  plt.plot([p.x for p in points], [p.y for p in points], style)
  for p in points:
      plt.text(p.x, p.y, p.name)
  plt.axis('scaled'); plt.axis('off')

def init_model(fname):
  # Inicializa el modelo leyendo los datos de la instancia y la solución.
  data = vrplib.read_instance(fname + '.vrp')
  sol = vrplib.read_solution(fname + '.sol')

  depot = data['depot'][0]
  x0 = data['node_coord'][depot][0]
  y0 = data['node_coord'][depot][1]

  # Crea la lista de ciudades excluyendo el depósito.
  cities = [City(str(c + 1), complex(data['node_coord'][c][0], data['node_coord'][c][1]), data['demand'][c])
            for c in range(data['dimension']) if c != depot]

  routes = []
  # Construye las rutas a partir de la solución óptima leída.
  for route in sol['routes']:
      tour = [City(str(depot + 1), complex(x0, y0), 0)]
      for c in route:
          tour.append(City(str(c + 1), complex(data['node_coord'][c][0], data['node_coord'][c][1]), data['demand'][c]))
      routes.append(tour)

  # Almacena la información del problema.
  prob = Problem()
  prob.name = data['name']
  prob.veh = len(sol['routes'])
  prob.cap = data['capacity']
  prob.optm = sol['cost']
  prob.depot = City(str(depot + 1), complex(x0, y0), 0)
  prob.cities = cities

  return prob, routes

def random_solution(prob):
  # Genera una solución aleatoria respetando la capacidad del vehículo.
  cap = prob.cap
  vehs = range(prob.veh)
  tours = [[prob.depot] for _ in range(prob.veh)]
    
  for city in prob.cities:
      row = random.choice(vehs)
      while calculate_demand(tours[row]) + city.demand > cap:
          row = random.choice(vehs)
      tours[row].append(city)

  return tours

def create_neighbor(tours):
  # Crea un nuevo vecindario intercambiando ciudades entre dos rutas.
  n = len(tours)
  r1, r2 = np.random.randint(0, n, size=2)

  # Decide cuántas ciudades intercambiar (hasta 5 como máximo).
  num_cities = np.random.randint(1, min(len(tours[r1]), len(tours[r2]), 5))
  indices1 = np.random.choice(range(1, len(tours[r1])), size=num_cities, replace=False)
  indices2 = np.random.choice(range(1, len(tours[r2])), size=num_cities, replace=False)

  new_tours = deepcopy(tours)

  for idx1, idx2 in zip(indices1, indices2):
      # Intercambia las ciudades seleccionadas.
      new_tours[r1][idx1], new_tours[r2][idx2] = new_tours[r2][idx2], new_tours[r1][idx1]

  return new_tours

def calculate_cost(tours):
  # Suma los costos de todas las rutas.
  return sum(tour_length(route) for route in tours)

def calculate_demand(tour):
  # Calcula la demanda total de una ruta.
  return sum(tour[i].demand for i in range(len(tour)))

vrp = 'data/A-n32-k5'

prob, opt = init_model(vrp)
plot_vrp(opt)

# Parámetros del algoritmo Simulated Annealing

T0 = 500           # Temperatura inicial
r = 0.995           # Tasa de enfriamiento
Ts = 1              # Temperatura final
iter = 50#200          # Número de iteraciones por cada nivel de temperatura

# Generar una solución inicial aleatoria
route = random_solution(prob)
cost = calculate_cost(route)

T = T0

min_cost = cost
min_route = route

cost_array = []

# Ejecución del algoritmo Simulated Annealing
while T > Ts:
  for _ in range(iter):
      new_route = create_neighbor(route)
      new_cost = calculate_cost(new_route)
      delta = new_cost - cost

      # Aceptar la nueva solución si es mejor o con probabilidad si es peor.
      if delta < 0 or np.random.rand() < np.exp(-delta / T):
          cost = new_cost
          route = deepcopy(new_route)

  cost_array.append(cost)

  if cost < min_cost:
      min_cost = cost
      min_route = route

  # Verifica si la solución actual está dentro del 10% del óptimo.
  if (min_cost - prob.optm) / prob.optm <= 0.1:
      print("Solución dentro del porcentaje óptimo.")
      break

  T *= r  # Enfriamiento de la temperatura

# Resultado final
print(min_route)
print(f'Costo final: {min_cost:.2f}, dentro de {100 * (min_cost - prob.optm) / prob.optm:.2f}% (óptimo = {prob.optm})')
plot_vrp(min_route)
