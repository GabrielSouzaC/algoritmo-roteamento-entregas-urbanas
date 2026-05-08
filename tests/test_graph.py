import unittest
from src.core.graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_adicionar_vertice(self):
        """testa adição de vértices"""
        v = self.graph.add_vertex("D")
        self.assertEqual(v.label, "D")
        self.assertIn("D", self.graph.vertices)

    def test_adicionar_aresta(self):
        """testa adição de aresta"""
        self.graph.add_edge("D", "C1", 10)
        self.assertEqual(len(self.graph.get_vertices()), 2)
        
        neighbors = self.graph.get_neighbors(self.graph.vertices["D"])
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0].target.label, "C1")
        self.assertEqual(neighbors[0].weight, 10)

    def test_grafo_dirigido(self):
        """testa que o grafo é dirigido (não adiciona aresta inversa automaticamente)"""
        self.graph.add_edge("D", "C1", 10)
        self.graph.add_edge("C1", "D", 15)
        
        # deve ter aresta D->C1 e C1->D
        d_neighbors = [e.target.label for e in self.graph.get_neighbors(self.graph.vertices["D"])]
        self.assertIn("C1", d_neighbors)
        
        c1_neighbors = [e.target.label for e in self.graph.get_neighbors(self.graph.vertices["C1"])]
        self.assertIn("D", c1_neighbors)

if __name__ == '__main__':
    unittest.main()