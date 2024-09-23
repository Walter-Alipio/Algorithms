from d_algorithm import Dijkstra_algorithm

graph = {}
graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["end"] = 30
graph["b"]["c"] = 1

graph["c"] = {}
graph["c"]["a"] = 1

graph["end"] = {}

infinite = float("inf")

costs = {}
costs["a"] = 10
costs["b"] = infinite
costs["c"] = infinite
costs["end"] = infinite

parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["end"] = None

alg = Dijkstra_algorithm(graph, costs, parents)

result = alg.run()["end"]

print("The fast way to get to end costs:" ,result)

print(alg.parents)
print(alg.costs)