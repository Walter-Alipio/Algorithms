from d_algorithm import Dijkstra_algorithm


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

alg = Dijkstra_algorithm(graph, costs, parents)

result = alg.run()

print("The fast way to get to end costs:" ,result["end"])


