from .vertex import Vertex

class Edge:
    """representa uma aresta direcionada e ponderada."""
    
    def __init__(self, source: Vertex, target: Vertex, weight: int):
        self.source = source
        self.target = target
        self.weight = int(weight)  # tempo estimado em minutos
    
    def __str__(self):
        return f"{self.source} -> {self.target} (peso: {self.weight})"
    
    def __repr__(self):
        return f"Edge({self.source}, {self.target}, {self.weight})"