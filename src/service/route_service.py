from ..io.json_reader import load_graph_from_json
from ..algorithms.dijkstra import find_shortest_path
from typing import Dict, Optional

class RouteService:
    """camada de serviço que orquestra o fluxo principal do sistema."""
    
    def __init__(self):
        self.graph = None
    
    def load_graph(self, file_path: str) -> bool:
        """carrega o grafo a partir de um arquivo JSON."""
        try:
            self.graph = load_graph_from_json(file_path)
            return True
        except Exception as e:
            print(f"Erro ao carregar grafo: {e}")
            return False
    
    def calculate_route(self, origin: str, destination: str) -> Dict:
        """calcula a rota de menor tempo entre origem e destino."""
        if not self.graph:
            return {
                "success": False,
                "message": "Nenhum grafo carregado. Carregue um arquivo JSON primeiro."
            }
        
        return find_shortest_path(self.graph, origin, destination)
    
    def get_graph_info(self) -> Dict:
        """retorna informações básicas do grafo carregado."""
        if not self.graph:
            return {"vertices": 0, "edges": 0}
        
        vertices = len(self.graph.get_vertices())
        edges = sum(len(self.graph.get_neighbors(v)) for v in self.graph.get_vertices())
        return {"vertices": vertices, "edges": edges}