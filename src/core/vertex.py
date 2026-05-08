class Vertex:
    """representa um vértice no grafo (ex: 'D' para Depósito ou 'C1' para Cliente)."""
    
    def __init__(self, label: str):
        self.label = label.strip().upper()  # normaliza o rótulo
    
    def __str__(self):
        return self.label
    
    def __repr__(self):
        return f"Vertex({self.label})"
    
    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.label == other.label
        if isinstance(other, str):
            return self.label == other.strip().upper()
        return False
    
    def __hash__(self):
        return hash(self.label)