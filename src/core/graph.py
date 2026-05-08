from typing import Dict, List, Optional
from .vertex import Vertex
from .edge import Edge

class Graph:
    """grafo dirigido e ponderado para o problema de roteamento."""
    
    def __init__(self):
        self.vertices: Dict[str, Vertex] = {}
        self.adj: Dict[Vertex, List[Edge]] = {}
    
    def add_vertex(self, label: str) -> Vertex:
        """adiciona um vértice ao grafo."""
        vertex = Vertex(label)
        if vertex.label not in self.vertices:
            self.vertices[vertex.label] = vertex
            self.adj[vertex] = []
        return vertex
    
    def add_edge(self, source_label: str, target_label: str, weight: int) -> None:
        """adiciona uma aresta direcionada com peso."""
        source = self.add_vertex(source_label)
        target = self.add_vertex(target_label)
        
        edge = Edge(source, target, weight)
        self.adj[source].append(edge)
    
    def get_vertices(self) -> List[Vertex]:
        return list(self.vertices.values())
    
    def get_neighbors(self, vertex: Vertex) -> List[Edge]:
        """retorna as arestas saindo de um vértice."""
        return self.adj.get(vertex, [])
    
    def __str__(self):
        result = ["Grafo:"]
        for v in self.get_vertices():
            edges = [str(e) for e in self.get_neighbors(v)]
            result.append(f"  {v}: {edges}")
        return "\n".join(result)