import sys
import os

# Adiciona o diretório raiz ao Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.service.route_service import RouteService

def main():
    print("=" * 60)
    print("   ALGORITMO DE ROTEAMENTO PARA ENTREGAS URBANAS")
    print("   Teoria dos Grafos - Finalização do Projeto")
    print("=" * 60)
    
    service = RouteService()
    
    # Carrega o grafo
    if not service.load_graph('data/sample_graph.json'):
        print("❌ Erro ao carregar o grafo.")
        return
    
    print(f"✅ Grafo carregado com sucesso!")
    info = service.get_graph_info()
    print(f"   Vértices: {info['vertices']} | Arestas: {info['edges']}")
    print("-" * 60)
    
    # Loop principal
    while True:
        print("\nDigite a origem e o destino (ou 'sair' para encerrar)")
        origin = input("Origem (ex: D): ").strip().upper()
        
        if origin.lower() in ['sair', 'exit', 'q']:
            print("👋 Encerrando o programa...")
            break
            
        destination = input("Destino (ex: C6): ").strip().upper()
        
        if destination.lower() in ['sair', 'exit', 'q']:
            print("👋 Encerrando o programa...")
            break
        
        result = service.calculate_route(origin, destination)
        
        print("\n" + "-" * 50)
        if result["success"]:
            print("✅ CAMINHO MÍNIMO ENCONTRADO")
            print(f"Caminho: {' → '.join(result['path'])}")
            print(f"Tempo estimado: {result['total_time']} minutos")
            
            # Pergunta se quer visualizar o mapa
            show_viz = input("\nDeseja visualizar o mapa fictício com o caminho destacado? (s/n): ").strip().lower()
            if show_viz in ['s', 'sim', 'y', 'yes']:
                try:
                    from src.visualization.graph_visualizer import GraphVisualizer
                    visualizer = GraphVisualizer()
                    visualizer.draw_graph(
                        service.graph, 
                        result['path'],
                        title=f"Mapa Fictício - Rota {origin} → {destination}"
                    )
                except ImportError:
                    print("❌ Módulo de visualização não encontrado (instale networkx e matplotlib).")
                except Exception as e:
                    print(f"❌ Erro ao gerar visualização: {e}")
        else:
            print("❌ " + result["message"])
        print("-" * 50)

if __name__ == "__main__":
    main()