from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom" ] = []
graph["jonny"] = []

def person_is_a_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    checked = []
    while search_queue :
        person = search_queue.popleft()
        if not person in checked:
            if person_is_a_seller(person):
                print(person + " is a mangos seller!")
                return True
            else:
                search_queue += graph[person]
                checked.append(person)
    return False

search("you")