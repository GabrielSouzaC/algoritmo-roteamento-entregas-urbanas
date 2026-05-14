from typing import Dict, List, Tuple, Optional
from ..core.graph import Graph
from ..core.vertex import Vertex

def bellman_ford(graph: Graph, source_label: str, target_label: str) -> Tuple[Optional[List[str]], int]:
    """
    Implementa o algoritmo de Bellman-Ford.
    """
    # Busca os vértices
    source = target = None
    for v in graph.get_vertices():
        if v.label == source_label:
            source = v
        if v.label == target_label:
            target = v
    
    if not source or not target:
        return None, float('inf')

    # Inicialização
    distances: Dict[Vertex, float] = {vertex: float('inf') for vertex in graph.get_vertices()}
    predecessors: Dict[Vertex, Optional[Vertex]] = {vertex: None for vertex in graph.get_vertices()}
    distances[source] = 0

    # Relaxamento |V|-1 vezes
    for _ in range(len(graph.get_vertices()) - 1):
        for vertex in graph.get_vertices():
            if distances[vertex] == float('inf'):
                continue
            for edge in graph.get_neighbors(vertex):
                neighbor = edge.target
                new_distance = distances[vertex] + edge.weight
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = vertex

    # Verificação de ciclo negativo
    for vertex in graph.get_vertices():
        if distances[vertex] == float('inf'):
            continue
        for edge in graph.get_neighbors(vertex):
            if distances[vertex] + edge.weight < distances[edge.target]:
                return None, float('inf')  # Ciclo negativo

    if distances[target] == float('inf'):
        return None, float('inf')

    # Reconstrução do caminho
    path: List[str] = []
    current = target
    while current is not None:
        path.append(current.label)
        current = predecessors[current]
    
    path.reverse()
    return path, int(distances[target])


# Função auxiliar (importante!)
def find_shortest_path_bellman_ford(graph: Graph, source: str, target: str) -> Dict:
    """Retorna resultado formatado (usada no main.py)."""
    path, total_time = bellman_ford(graph, source, target)
    
    if path is None:
        return {
            "success": False,
            "message": f"Não existe caminho entre {source} e {target}",
            "path": None,
            "total_time": None,
            "algorithm": "Bellman-Ford"
        }
    
    return {
        "success": True,
        "path": path,
        "total_time": total_time,
        "message": f"Caminho encontrado com Bellman-Ford (tempo: {total_time} minutos)",
        "algorithm": "Bellman-Ford"
    }