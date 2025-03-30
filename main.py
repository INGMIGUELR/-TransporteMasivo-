import heapq

class TransporteMasivo:
    def __init__(self):
        self.grafo = {}  # Diccionario para almacenar el grafo

    def agregar_ruta(self, origen, destino, costo):
        """Agrega una ruta unidireccional entre dos nodos."""
        if origen not in self.grafo:
            self.grafo[origen] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        
        self.grafo[origen].append((destino, costo))
        self.grafo[destino].append((origen, costo))  # Si es bidireccional

    def dijkstra(self, inicio, destino):
        """Encuentra la ruta más corta desde el nodo inicio hasta destino."""
        cola = [(0, inicio)]
        costos = {nodo: float('inf') for nodo in self.grafo}
        costos[inicio] = 0
        camino = {}

        while cola:
            costo_actual, nodo_actual = heapq.heappop(cola)

            if nodo_actual == destino:
                ruta = []
                while nodo_actual in camino:
                    ruta.append(nodo_actual)
                    nodo_actual = camino[nodo_actual]
                ruta.append(inicio)
                return ruta[::-1], costos[destino]

            for vecino, costo in self.grafo.get(nodo_actual, []):
                nuevo_costo = costo_actual + costo
                if nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    camino[vecino] = nodo_actual
                    heapq.heappush(cola, (nuevo_costo, vecino))

        return None, float('inf')

# Ejemplo de uso
transporte = TransporteMasivo()
transporte.agregar_ruta("A", "B", 2)
transporte.agregar_ruta("A", "C", 5)
transporte.agregar_ruta("B", "C", 1)
transporte.agregar_ruta("B", "D", 3)
transporte.agregar_ruta("C", "D", 2)

inicio, destino = "A", "D"
ruta, costo = transporte.dijkstra(inicio, destino)

if ruta:
    print(f"Mejor ruta de {inicio} a {destino}: {' -> '.join(ruta)} con costo {costo}")
else:
    print(f"No hay ruta disponible de {inicio} a {destino}")