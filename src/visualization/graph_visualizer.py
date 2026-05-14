import matplotlib.pyplot as plt
import networkx as nx
import random
from typing import List, Optional
from ..core.graph import Graph

class GraphVisualizer:
    """Visualizador melhorado para grafos de roteamento."""
    
    def __init__(self):
        self.pos = {}
    
    def assign_random_positions(self, graph: Graph, seed: int = 42):
        random.seed(seed)
        self.pos = {}
        for vertex in graph.get_vertices():
            if vertex.label == "D":
                self.pos[vertex.label] = (0, 0)
            else:
                self.pos[vertex.label] = (random.uniform(-20, 20), random.uniform(-15, 15))
    
    def draw_graph(self, graph: Graph, shortest_path: Optional[List[str]] = None, 
                   title: str = "Mapa Fictício - Roteamento de Entregas"):
        
        if not self.pos or len(self.pos) != len(graph.get_vertices()):
            self.assign_random_positions(graph)
        
        G = nx.DiGraph()
        for vertex in graph.get_vertices():
            for edge in graph.get_neighbors(vertex):
                G.add_edge(edge.source.label, edge.target.label, weight=edge.weight)
        
        plt.figure(figsize=(16, 11))
        
        # Arestas normais
        nx.draw_networkx_edges(G, self.pos, edge_color='#B0B0B0', arrows=True, alpha=0.6, width=1.2)
        
        # Caminho mínimo em destaque
        if shortest_path and len(shortest_path) > 1:
            path_edges = list(zip(shortest_path, shortest_path[1:]))
            nx.draw_networkx_edges(G, self.pos, edgelist=path_edges, 
                                 edge_color='red', width=4, arrows=True, alpha=0.95)
            
            # === MOSTRAR PESOS NO CAMINHO MÍNIMO ===
            path_edge_labels = {}
            for u, v in path_edges:
                if G.has_edge(u, v):
                    path_edge_labels[(u, v)] = G[u][v]['weight']
            
            nx.draw_networkx_edge_labels(G, self.pos, edge_labels=path_edge_labels, 
                                       font_size=11, font_color='red', font_weight='bold')
        
        # Nós
        nx.draw_networkx_nodes(G, self.pos, node_size=950, node_color='lightblue', 
                             edgecolors='darkblue', linewidths=2)
        
        # Depósito em destaque
        if "D" in self.pos:
            nx.draw_networkx_nodes(G, self.pos, nodelist=["D"], node_size=1250, 
                                 node_color='orange', edgecolors='red', linewidths=3)
        
        nx.draw_networkx_labels(G, self.pos, font_size=10, font_weight='bold')
        
        # Legenda com caminho e tempo total
        if shortest_path:
            path_str = " → ".join(shortest_path)
            total_time = sum(G[u][v]['weight'] for u, v in zip(shortest_path, shortest_path[1:]) if G.has_edge(u, v))
            plt.figtext(0.5, 0.94, f"Caminho mínimo: {path_str}   |   Tempo total: {total_time} minutos", 
                       ha='center', fontsize=13, bbox=dict(boxstyle="round,pad=0.6", facecolor="wheat"))
        
        plt.title(title, fontsize=16, pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()