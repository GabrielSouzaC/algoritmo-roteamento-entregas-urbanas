import heapq
from typing import Dict, List, Tuple, Optional
from ..core.graph import Graph
from ..core.vertex import Vertex

def dijkstra(graph: Graph, source_label: str, target_label: str) -> Tuple[Optional[List[str]], int]:
    """
    implementa o algoritmo de Dijkstra para encontrar o caminho de menor tempo
    entre origem e destino em um grafo dirigido e ponderado.
    
    retorna:
        - tuple: (lista com o caminho de vértices, tempo total)
        - se não houver caminho: (None, float('inf'))
    """
    # verifica se os vértices existem
    source = None
    target = None
    for v in graph.get_vertices():
        if v.label == source_label:
            source = v
        if v.label == target_label:
            target = v
    
    if not source or not target:
        return None, float('inf')
    
    # inicialização
    distances: Dict[Vertex, int] = {vertex: float('inf') for vertex in graph.get_vertices()}
    distances[source] = 0
    predecessors: Dict[Vertex, Optional[Vertex]] = {vertex: None for vertex in graph.get_vertices()}
    
    # fila de prioridade (min-heap)
    priority_queue: List[Tuple[int, Vertex]] = [(0, source)]
    
    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        
        # se já encontramos um caminho melhor, ignora
        if current_distance > distances[current]:
            continue
        
        # relaxa as arestas dos vizinhos
        for edge in graph.get_neighbors(current):
            neighbor = edge.target
            new_distance = current_distance + edge.weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    # reconstrução do caminho
    if distances[target] == float('inf'):
        return None, float('inf')
    
    # monta o caminho do target até o source
    path: List[str] = []
    current = target
    while current is not None:
        path.append(current.label)
        current = predecessors[current]
    
    path.reverse()  # inverte para ficar da origem ao destino
    
    return path, distances[target]


# função auxiliar para facilitar uso
def find_shortest_path(graph: Graph, source: str, target: str) -> Dict:
    """Retorna resultado formatado para uso na interface/service."""
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