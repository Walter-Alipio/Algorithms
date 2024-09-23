from d_algorithm import Dijkstra_algorithm


graph_A = {}
graph_A["start"] = {}
graph_A["start"]["a"] = 5
graph_A["start"]["b"] = 2

graph_A["a"] = {}
graph_A["a"]["c"] = 4
graph_A["a"]["d"] = 2

graph_A["b"] = {}
graph_A["b"]["a"] = 8
graph_A["b"]["d"] = 7

graph_A["c"] = {}
graph_A["c"]["end"] = 3
graph_A["c"]["d"] = 6

graph_A["d"] = {}
graph_A["d"]["end"] = 1

graph_A["end"] = {}

infinite = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinite
costs["d"] = infinite
costs["end"] = infinite

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["end"] = None

alg = Dijkstra_algorithm(graph_A, costs, parents)

result = alg.run()["end"]

print("The fast way to get to end costs:" ,result)