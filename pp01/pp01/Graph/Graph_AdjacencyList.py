from collections import deque
import sys


class Vertex:
    """
    An example implementation of a Vertex or Node of a graph.
    """
    def __init__(self, key):
        """
        Creates a new Vertex.
        """
        self._neighbors = []
        self._key = key

    def add_neighbor(self, neighbor_vertex, weight):
        self._neighbors.append((neighbor_vertex, weight))

    def get_connections(self):
        return self._neighbors

    def get_key(self):
        return self._key

    def get_weight(self, to_vertex):
        for neighbor in self._neighbors:
            if to_vertex == neighbor[0].get_key():
                return neighbor[1]

    def get_outdegree(self):
        return len(self._neighbors)

    def is_neighbor(self, vertex):
        for neighbor in self._neighbors:
            if neighbor[0] == vertex:
                return True
        return False


class Graph:
    """
    An example implementation of Directed Graph ADT.
    """
    def __init__(self):
        """
        Creates a new, empty Graph.
        """
        self._vertices = {}

    def add_vertex(self, vertex):
        """
        Adds a new vertex into the graph.
        :param vertex: The Vertex to be added into the Graph.
        :return: None.
        """
        v = Vertex(vertex)
        self._vertices[vertex] = v

    def add_edge(self, from_vertex, to_vertex, weight):
        """
        Add a directed edge between two vertices
        :param from_vertex: Starting vertex of the edge
        :param to_vertex: Where the edge ends.
        :param weight: weight of the edge
        :return: None
        """
        if from_vertex not in self._vertices:
            self.add_vertex(from_vertex)

        if to_vertex not in self._vertices:
            self.add_vertex(to_vertex)

        self._vertices[from_vertex].add_neighbor(self._vertices[to_vertex], weight)

    def get_vertices(self):
        """
        Get all the vertices of the directed Graph.
        :return: List of vertices of the graph.
        """
        vertices = list(self._vertices.keys())
        vertices.sort()
        return vertices

    def get_edges(self):
        """
        Get all the edges of the directed graph.
        :return: List of edges of the graph.
        """
        edges = []
        for vertex in self._vertices:
            neighbors = self._vertices[vertex].get_connections()
            for neighbor in neighbors:
                edges.append((vertex, neighbor[0].get_key(), self._vertices[vertex].get_weight(neighbor[0].get_key())))

        return edges

    def get_vertex(self, vertex_key):
        return self._vertices.get(vertex_key)

    def get_outdegree(self):
        outdegree = []
        for vertex,V in self._vertices.items():
            outdegree.append((vertex, V.get_outdegree()))
        return outdegree

    def get_indegree(self):
        indegree = []
        for vertex, V in self._vertices.items():
            indeg = 0
            for V2 in self._vertices.values():
                if V2.is_neighbor(V):
                    indeg += 1
            indegree.append((vertex, indeg))
        return indegree

    def bfs(self, start_vertex):
        startVertex = self.get_vertex(start_vertex)

        if startVertex is None:
            raise Exception("Vertex {0} is not found in graph".format(start_vertex))

        visited = {}
        traversed = []

        q = deque()
        q.append(startVertex)

        while len(q):
            v = q.popleft()
            # print(v)
            key = v.get_key()
            # print(key)
            # print(visited)
            if visited.get(key) is None:

                visited[key] = True
                traversed.append(key)
                # print(visited)
                for neighbor in v.get_connections():
                    # print(neighbor)
                    if visited.get(neighbor[0].get_key()) is None:
                        q.append(neighbor[0])
                    # print(q)

        return traversed

    def dfs(self, start_vertex):
        startVertex = self.get_vertex(start_vertex)

        if startVertex is None:
            raise Exception("Vertex {0} is not found in graph".format(start_vertex))

        visited = {}
        traversed = []

        q = []
        q.append(startVertex)

        while len(q):
            v = q.pop()
            key = v.get_key()
            # print(key)
            # print(visited)
            if visited.get(key) is None:
                visited[key] = True
                traversed.append(key)

                for neighbor in v.get_connections():
                    if visited.get(neighbor[0].get_key()) is None:
                        q.append(neighbor[0])
                # print(q)
        return traversed

    @staticmethod
    def _min_distance(fringe, distance):
        min = sys.maxsize
        min_vertex = None

        for node in fringe:
            # print(node)
            if distance[node.get_key()][0] < min:
                min = distance[node.get_key()][0]
                min_vertex = node

        return min_vertex

    def dijkstra(self, source, dest):
        startVertex = self.get_vertex(source)
        distance = dict()
        distance[source] = (0,source)
        visited = {}
        fringe = [startVertex]

        while len(fringe):
            print("1-----",distance, )
            # print(fringe, "-----1")
            current_vertex = self._min_distance(fringe, distance)
            current_vertex_key = current_vertex.get_key()
            print("#",current_vertex_key)
            fringe.remove(current_vertex)
            visited[current_vertex_key] = True
            print( "2-----", fringe,)

            for neighbor in current_vertex.get_connections():
                neighbor_vertex = neighbor[0]
                neighbor_weight = neighbor[1]
                neighbor_vertex_key = neighbor_vertex.get_key()
                print( "----3-----", "current_vertex={0}/ neighbor={1} /neighbor weight={2}".format(current_vertex_key, neighbor_vertex_key, neighbor_weight))
                if neighbor_vertex not in fringe and visited.get(neighbor_vertex_key) is None:
                    print( "----3.1-----", "neighbor do not exist in fringe and not visited = {0}".format(neighbor_vertex_key))
                    fringe.append(neighbor_vertex)
                print( "----4-----", "current_vertex={0} neighbor = {1} with possible weight={2}".format(current_vertex_key, neighbor_vertex_key, distance[current_vertex_key][0] +neighbor_weight))
                if (distance.get(neighbor_vertex_key) is None) or (distance[neighbor_vertex_key][0] > distance[current_vertex_key][0] +neighbor_weight):
                    print( "----4.1-----","neighbor {0}- weight changed to= {1}".format(neighbor_vertex_key, distance[current_vertex_key][0] +neighbor_weight))
                    distance[neighbor_vertex_key] = (distance[current_vertex_key][0] +neighbor_weight, current_vertex_key)
            print("#########################")
        sp = []
        x = dest

        while x != source:
            sp.append(x)
            x = distance[x][1]
        sp.append(x)

        shortest_path = []
        while len(sp):
            shortest_path.append(sp.pop())

        return shortest_path, distance[dest][0]


if __name__ == "__main__":

    """
    graph = {
        "0" : [("1", 5), ("2", 3)],
        "1" : [("3", 3)],
        "2" : [("1", 1), ("3", 2), ("4", 6)],
        "3" : [],
        "4" : ["3", 1]
    }
    """

    g = Graph()

    for v in range(5):
        g.add_vertex(v)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 1, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 6)
    g.add_edge(4, 3, 1)

    print(g.get_vertices())
    print(g.get_edges())
    print(g.get_outdegree())
    print(g.get_indegree())
    print(g.bfs(0))
    print(g.dfs(0))
    print("############################")
    print(g.dijkstra(0,3))