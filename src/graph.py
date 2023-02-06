class Vertex:
    def __init__(self, name):
        self.name = name
        self.distance = float('inf')
        self.prev = None

    def __repr__(self):
        return self.name


class Edge:
    def __init__(self, _from, _to, _cost):
        self._from = _from
        self._to = _to
        self._cost = _cost

class BellmanFord:
    def find_path(self, source, edges, v):
        source.distance = 0

        for i in range(v-1):
            for edge in edges:
                if edge._from.distance + edge._cost < edge._to.distance:
                    edge._to.distance = edge._from.distance + edge._cost
                    edge._to.prev = edge._from

        for edge in edges:
            if edge._from.distance + edge._cost < edge._to.distance:
                print("Graph has a negative cycle")
                return False

        return True

    def trace_path(self, source, destination):
        vertex = destination
        path = []

        while (vertex is not source):
            path.insert(0, vertex)
            vertex = vertex.prev

        path.insert(0, source)

        return path
