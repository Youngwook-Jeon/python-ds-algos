class TravellingSalesmanProblem:

    def __init__(self, graph) -> None:
        self.graph = graph
        # number of V vertices in the G(V,E)
        self.n = len(graph)
        self.visited = [False for _ in range(self.n)]
        # we start with the first vertex
        self.visited[0] = True
        # collect all the hamiltonian cycles
        self.hamiltonian_cycles = []
        # track what nodes are included in the cycle
        self.path = [0 for _ in range(self.n)]
    
    # whether including the given node is valid
    def is_valid(self, vertex, actual_position):
        # whether the given vertex has already been visited
        if self.visited[vertex]:
            return False
        
        # whether is there a connection between the vertices
        if self.graph[actual_position][vertex] == 0:
            return False
        
        return True
    
    def tsp(self, actual_position, counter, cost):
        # we have considered all the nodes i the G(V, E) graph
        # and the last node can be connected to the first one (form a cycle)
        if counter == self.n and self.graph[actual_position][0]:
            self.path.append(0)
            print(self.path)
            self.hamiltonian_cycles.append(cost + self.graph[actual_position][0])
            self.path.pop()
            return
        
        # consider all the nodes in the G(V, E) graph
        for i in range(self.n):
            # check whether we can include the node with index i to the path (cycle)
            if self.is_valid(i, actual_position):
                self.visited[i] = True
                self.path[counter] = i

                # we call the func recursively
                self.tsp(i, counter + 1, cost + self.graph[actual_position][i])

                # BACKTRACK
                self.visited[i] = False

if __name__ == '__main__':
    g = [[0, 1, 0, 2, 0], [1, 0, 1, 0, 2], [0, 1, 0, 3, 1], [2, 0, 3, 0, 1], [0, 2, 1, 1, 0]]
    tsp = TravellingSalesmanProblem(g)
    tsp.tsp(0, 1, 0)
    print(tsp.hamiltonian_cycles)