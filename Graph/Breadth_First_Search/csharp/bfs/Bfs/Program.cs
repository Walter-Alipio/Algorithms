using System.Collections;

Dictionary<string, string[]> graph = [];
graph.Add("you", ["alice", "bob", "claire"]);
graph.Add("bob", ["anuj", "peggy"]);
graph.Add("alice", ["peggy"]);
graph.Add("claire", ["thom", "jonny"]);
graph.Add("anuj", []);
graph.Add("peggy", []);
graph.Add("thom", []);
graph.Add("jonny", []);

bool PersonIsASeller(string name)
{
    return name.Last() == 'm';
}

bool Search(string name)
{
    Queue<string> search_queue = new Queue<string>();
    foreach (var item in graph[name])
    {
        search_queue.Enqueue(item);
    }
    List<string> checkedItems = [];
    while (search_queue.Count > 0)
    {
        var person = search_queue.Dequeue();
        if (!checkedItems.Contains(person))
        {
            if (PersonIsASeller(person))
            {
                System.Console.WriteLine($"{person} is a seller!");
                return true;
            }
            else
            {
                foreach (var item in graph[person])
                {
                    search_queue.Enqueue(item);
                    checkedItems.Add(person);
                }
            }
        }
    }
    return false;
}

Search("you");