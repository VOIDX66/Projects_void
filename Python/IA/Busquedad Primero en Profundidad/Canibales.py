class Nodo:
    def __init__(self, valor, padre=None):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.padre = padre