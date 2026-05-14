import heapq
from typing import Dict, List, Tuple, Optional
from ..core.graph import Graph
from ..core.vertex import Vertex

def dijkstra(graph: Graph, source_label: str, target_label: str) -> Tuple[Optional[List[str]], int]:
    """
    Implementa o algoritmo de Dijkstra para encontrar o caminho de menor tempo.
    """
    # Verifica se os vértices existem
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
    distances[source] = 0
    predecessors: Dict[Vertex, Optional[Vertex]] = {vertex: None for vertex in graph.get_vertices()}
    
    # Fila de prioridade com contador (evita erro de comparação entre Vertex)
    priority_queue: List[Tuple[float, int, Vertex]] = []
    counter = 0
    heapq.heappush(priority_queue, (0, counter, source))
    
    while priority_queue:
        current_distance, _, current = heapq.heappop(priority_queue)
        
        if current_distance > distances[current]:
            continue
        
        for edge in graph.get_neighbors(current):
            neighbor = edge.target
            new_distance = current_distance + edge.weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current
                counter += 1
                heapq.heappush(priority_queue, (new_distance, counter, neighbor))
    
    # Se não encontrou caminho
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


# Função auxiliar usada em todo o projeto
def find_shortest_path(graph: Graph, source: str, target: str) -> Dict:
    """Retorna resultado formatado para uso na interface e service."""
    path, total_time = dijkstra(graph, source, target)
    
    if path is None:
        return {
            "success": False,
            "message": f"Não existe caminho entre {source} e {target}",
            "path": None,
            "total_time": None
        }
    
    return {
        "success": True,
        "path": path,
        "total_time": total_time,
        "message": f"Caminho encontrado com tempo estimado de {total_time} minutos"
    }