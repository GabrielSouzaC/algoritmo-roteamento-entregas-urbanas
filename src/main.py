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
        print("\n" + "="*50)
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
                
                print("Gerando grafo aleatório...")
                graph = generate_random_graph(num_vertices=num_v, density=density)
                save_graph_to_json(graph, 'data/generated_graphs/grafo_aleatorio_temp.json')
                service.graph = graph  # carrega diretamente
                print("✅ Grafo aleatório gerado e carregado!")
            except Exception as e:
                print(f"❌ Erro ao gerar grafo: {e}")
                continue
        else:
            # Carrega o grafo fixo
            if not service.load_graph('data/sample_graph.json'):
                print("❌ Erro ao carregar grafo fixo.")
                continue
            print("✅ Grafo fixo carregado!")

        info = service.get_graph_info()
        print(f"   Vértices: {info['vertices']} | Arestas: {info['edges']}")
        
        # Loop de consultas
        while True:
            print("\n" + "-"*60)
            origin = input("Origem (ex: D) ou 'voltar': ").strip().upper()
            
            if origin in ['VOLTAR', 'SAIR', '0']:
                break
                
            destination = input("Destino (ex: C10): ").strip().upper()
            
            result = service.calculate_route(origin, destination)
            
            print("\n" + "-" * 50)
            if result["success"]:
                print("✅ CAMINHO MÍNIMO ENCONTRADO")
                print(f"Caminho: {' → '.join(result['path'])}")
                print(f"Tempo estimado: {result['total_time']} minutos")
                
                show_viz = input("\nVisualizar no mapa fictício? (s/n): ").strip().lower()
                if show_viz in ['s', 'sim', 'y']:
                    try:
                        from src.visualization.graph_visualizer import GraphVisualizer
                        visualizer = GraphVisualizer()
                        visualizer.draw_graph(service.graph, result['path'])
                    except Exception as e:
                        print(f"Erro na visualização: {e}")
            else:
                print("❌ " + result["message"])
            print("-" * 50)

if __name__ == "__main__":
    main()