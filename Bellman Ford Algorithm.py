class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def Display(self, dist):
        print("(Vertex)  (Distance from Source)")
        for i in range(self.V):
            print("{0}\t\t\t{1}".format(i, dist[i]))

    def bellman(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        self.Display(dist)

f = Graph(5)
f.add_edge(0, 1, 5)
f.add_edge(0, 2, 4)
f.add_edge(1, 3, 3)
f.add_edge(2, 1, 6)
f.add_edge(3, 2, 2)
f.bellman(0)
