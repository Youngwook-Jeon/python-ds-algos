class Graph:
    def __init__(self, gdict=None) -> None:
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            v = queue.pop(0)
            print(v)
            for adjacent_vertex in self.gdict[v]:
                if (adjacent_vertex not in visited):
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)
    
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popped_vertex = stack.pop()
            print(popped_vertex)
            for adjacent_vertex in self.gdict[popped_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)

if __name__ == "__main__":
    custom_dict = { "a": ["b", "c"], "b": ["a", "d", "e"], "c": ["a", "e"], "d": ["b", "e"], "e": ["d", "c"] }
    graph = Graph(custom_dict)
    print(graph.gdict)
    graph.bfs("a")
    print()
    graph.dfs("a")