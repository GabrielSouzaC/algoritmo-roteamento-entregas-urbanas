import sys
import os

# adiciona o diretório raiz ao Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.service.route_service import RouteService

def main():
    print("=" * 60)
    print("   ALGORITMO DE ROTEAMENTO PARA ENTREGAS URBANAS")
    print("   Teoria dos Grafos - MVP (E3)")
    print("=" * 60)
    
    service = RouteService()
    
    # carrega o grafo
    if not service.load_graph('data/sample_graph.json'):
        print("❌ Erro ao carregar o grafo.")
        return
    
    print(f"✅ Grafo carregado com sucesso!")
    info = service.get_graph_info()
    print(f"   Vértices: {info['vertices']} | Arestas: {info['edges']}")
    print("-" * 60)
    
    # loop simples para múltiplas consultas
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
        
        print("\n" + "-" * 40)
        if result["success"]:
            print("✅ CAMINHO MÍNIMO ENCONTRADO")
            print(f"Caminho: {' → '.join(result['path'])}")
            print(f"Tempo estimado: {result['total_time']} minutos")
        else:
            print("❌ " + result["message"])
        print("-" * 40)

if __name__ == "__main__":
    main()