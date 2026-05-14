# src/io/graph_generator.py
import json
import random
from typing import Dict, Any
from ..core.graph import Graph

def generate_random_graph(num_vertices: int = 25, density: float = 0.4, 
                         min_weight: int = 1, max_weight: int = 30) -> Graph:
    """
    Gera um grafo aleatório dirigido e ponderado.
    
    Parâmetros:
        num_vertices: quantidade de vértices (20 a 50 recomendado)
        density: densidade do grafo (0.2 a 0.6)
        min_weight / max_weight: faixa de tempo estimado
    """
    if not (20 <= num_vertices <= 50):
        num_vertices = random.randint(20, 50)
    
    graph = Graph()
    
    # Criar vértices: D + C1, C2, ..., Cn
    vertices = ["D"]
    for i in range(1, num_vertices):
        vertices.append(f"C{i}")
    
    for v in vertices:
        graph.add_vertex(v)
    
    # Gerar arestas aleatórias
    possible_edges = 0
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j:  # não permite self-loop
                possible_edges += 1
                
                # Decide se cria a aresta baseado na density
                if random.random() < density:
                    weight = random.randint(min_weight, max_weight)
                    graph.add_edge(vertices[i], vertices[j], weight)
    
    return graph


def save_graph_to_json(graph: Graph, file_path: str) -> bool:
    """Salva o grafo gerado no formato JSON."""
    try:
        data: Dict[str, Any] = {
            "vertices": [v.label for v in graph.get_vertices()],
            "arestas": []
        }
        
        for vertex in graph.get_vertices():
            for edge in graph.get_neighbors(vertex):
                data["arestas"].append({
                    "origem": edge.source.label,
                    "destino": edge.target.label,
                    "peso": edge.weight
                })
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Grafo gerado com sucesso: {len(data['vertices'])} vértices e {len(data['arestas'])} arestas")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao salvar grafo: {e}")
        return False