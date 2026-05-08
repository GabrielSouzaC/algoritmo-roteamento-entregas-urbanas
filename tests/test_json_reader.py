import unittest
from src.io.json_reader import load_graph_from_json

class TestJsonReader(unittest.TestCase):

    def test_carregar_grafo_valido(self):
        """caso base: arquivo JSON válido"""
        graph = load_graph_from_json('data/sample_graph.json')
        self.assertIsNotNone(graph)
        self.assertEqual(len(graph.get_vertices()), 7)
        self.assertGreater(len([e for v in graph.get_vertices() for e in graph.get_neighbors(v)]), 0)

    def test_arquivo_inexistente(self):
        """caso: arquivo não encontrado"""
        with self.assertRaises(FileNotFoundError):
            load_graph_from_json('data/arquivo_que_nao_existe.json')

if __name__ == '__main__':
    unittest.main()