class Dijkstra_algorithm:
    done = []
    def __init__(self, graph, costs, parents):
        self.graph = graph
        self.costs = costs
        self.parents = parents
        
    def run(self):
        node = self.find_lowest_in_costs(self.costs)
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.done.append(node)
            node = self.find_lowest_in_costs(self.costs)
        return self.costs


    def find_lowest_in_costs(self, costs):
        lowest_cost = float("inf")
        node_lowest_cost = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in self.done:
                lowest_cost = cost
                node_lowest_cost = node
        return node_lowest_cost
    