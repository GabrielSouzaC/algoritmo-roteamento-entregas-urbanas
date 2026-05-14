# src/main.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.service.route_service import RouteService
from src.io.graph_generator import generate_random_graph, save_graph_to_json

def main():
    print("=" * 70)
    print("   ALGORITMO DE ROTEAMENTO PARA ENTREGAS URBANAS")
    print("   Teoria dos Grafos - Versão Final")
    print("=" * 70)
    
    service = RouteService()
    
    while True:
        print("\n" + "="*60)
        print("Escolha o tipo de grafo:")
        print("1 - Grafo fixo (sample_graph.json)")
        print("2 - Gerar novo grafo aleatório")
        print("0 - Sair")
        opcao = input("\nDigite a opção (1/2/0): ").strip()

        if opcao == "0":
            print("👋 Encerrando o programa...")
            break

        if opcao == "2":
            try:
                num_v = int(input("Número de vértices (20-50): ") or "25")
                density = float(input("Densidade (0.2-0.6): ") or "0.35")
                graph = generate_random_graph(num_vertices=num_v, density=density)
                save_graph_to_json(graph, 'data/generated_graphs/grafo_aleatorio_temp.json')
                service.graph = graph
                print("✅ Grafo aleatório gerado!")
            except Exception as e:
                print(f"❌ Erro: {e}")
                continue
        else:
            if not service.load_graph('data/sample_graph.json'):
                print("❌ Erro ao carregar grafo fixo.")
                continue
            print("✅ Grafo fixo carregado!")

        info = service.get_graph_info()
        print(f"   Vértices: {info['vertices']} | Arestas: {info['edges']}")

        # Escolha do algoritmo
        print("\nEscolha o algoritmo:")
        print("1 - Dijkstra (recomendado)")
        print("2 - Bellman-Ford (comparação)")
        alg_choice = input("Digite (1/2): ").strip()

        use_bellman = alg_choice == "2"

        # Loop de rotas
        while True:
            print("\n" + "-"*60)
            origin = input("Origem (ex: D) ou 'voltar': ").strip().upper()
            if origin in ['VOLTAR', 'SAIR', '0']:
                break
                
            destination = input("Destino (ex: C15): ").strip().upper()

            if use_bellman:
                from src.algorithms.bellman_ford import find_shortest_path_bellman_ford
                result = find_shortest_path_bellman_ford(service.graph, origin, destination)
            else:
                result = service.calculate_route(origin, destination)

            print("\n" + "-" * 55)
            if result["success"]:
                print(f"✅ CAMINHO MÍNIMO ENCONTRADO ({result.get('algorithm', 'Dijkstra')})")
                print(f"Caminho: {' → '.join(result['path'])}")
                print(f"Tempo estimado: {result['total_time']} minutos")
                
                if input("\nVisualizar no mapa fictício? (s/n): ").strip().lower() in ['s', 'sim', 'y']:
                    try:
                        from src.visualization.graph_visualizer import GraphVisualizer
                        visualizer = GraphVisualizer()
                        visualizer.draw_graph(service.graph, result['path'])
                    except Exception as e:
                        print(f"Erro na visualização: {e}")
            else:
                print("❌ " + result["message"])
            print("-" * 55)

if __name__ == "__main__":
    main()