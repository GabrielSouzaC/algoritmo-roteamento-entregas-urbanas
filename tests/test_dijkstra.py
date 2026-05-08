import unittest
from src.io.json_reader import load_graph_from_json
from src.algorithms.dijkstra import find_shortest_path, dijkstra

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

if __name__ == '__main__':
    unittest.main()