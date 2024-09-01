
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

infinite = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinite

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

done = []

def dijkstra_alg():
    node = find_lowest_in_costs(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        done.append(node)
        node = find_lowest_in_costs(costs)


def find_lowest_in_costs(costs):
    lowest_cost = float("inf")
    node_lowest_cost = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in done:
            lowest_cost = cost
            node_lowest_cost = node
    return node_lowest_cost

dijkstra_alg()

print(costs)


