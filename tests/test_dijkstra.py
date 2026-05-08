import unittest
from src.io.json_reader import load_graph_from_json
from src.algorithms.dijkstra import find_shortest_path
from src.core.graph import Graph   

class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.graph = load_graph_from_json('data/sample_graph.json')

    def test_caminho_minimo_d_para_c6(self):
        """caso base: caminho conhecido"""
        result = find_shortest_path(self.graph, 'D', 'C6')
        self.assertTrue(result['success'])
        self.assertEqual(result['path'], ['D', 'C1', 'C4', 'C6'])
        self.assertEqual(result['total_time'], 27)

    def test_caminho_minimo_d_para_c4(self):
        """outro caminho válido"""
        result = find_shortest_path(self.graph, 'D', 'C4')
        self.assertTrue(result['success'])
        self.assertEqual(result['total_time'], 20)

    def test_caminho_inexistente(self):
        """caso: não existe caminho"""
        result = find_shortest_path(self.graph, 'C6', 'D')
        self.assertFalse(result['success'])
        self.assertIsNone(result['path'])

    def test_grafo_vazio(self):
        """caso: grafo sem arestas"""
        empty_graph = load_graph_from_json('data/sample_graph.json')
        # remove todas as arestas para simular grafo vazio
        empty_graph.adj = {v: [] for v in empty_graph.adj}
        result = find_shortest_path(empty_graph, 'D', 'C6')
        self.assertFalse(result['success'])

    def test_grafo_completo(self):
        """caso: grafo completo - todos os vértices conectados entre si"""
        # cria um grafo pequeno completamente conectado
        complete_graph = Graph()
        vertices = ["A", "B", "C", "D"]
        
        for v in vertices:
            complete_graph.add_vertex(v)
        
        # conecta todos com todos (grafo denso)
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if i != j:
                    complete_graph.add_edge(vertices[i], vertices[j], i + j + 1)
        
        result = find_shortest_path(complete_graph, "A", "D")
        self.assertTrue(result['success'])
        self.assertIsNotNone(result['path'])
        self.assertGreater(result['total_time'], 0)


if __name__ == '__main__':
    unittest.main()