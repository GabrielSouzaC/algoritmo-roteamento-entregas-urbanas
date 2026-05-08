import json
from typing import Dict, Any
from ..core.graph import Graph

def load_graph_from_json(file_path: str) -> Graph:
    """
    carrega um grafo a partir de um arquivo JSON.
    formato esperado conforme definido na E2.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data: Dict[str, Any] = json.load(f)
        
        graph = Graph()
        
        # adiciona vértices (mesmo que não sejam usados diretamente, garantimos que existam)
        if "vertices" in data:
            for v in data["vertices"]:
                graph.add_vertex(v)
        
        # adiciona arestas
        if "arestas" in data:
            for edge_data in data["arestas"]:
                origem = edge_data.get("origem")
                destino = edge_data.get("destino")
                peso = edge_data.get("peso")
                
                if origem and destino and peso is not None:
                    graph.add_edge(origem, destino, peso)
        
        return graph
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Arquivo JSON inválido: {file_path}")
    except Exception as e:
        raise Exception(f"Erro ao carregar grafo: {str(e)}")