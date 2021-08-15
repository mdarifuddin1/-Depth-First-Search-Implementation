Adj_list = {
    "A":["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D" : [],
    "E" : ["F"],
    "F" : []
}

color = {} # there are 3 color here white ,gray and blue
parent= {}
trav_time = {} # start and ending

dfs_traversal_output = []

for node in Adj_list.keys():
    color[node] = "white"
    parent[node] = None
    trav_time [node] = [-1, -1]
time = 0
def dfs_util(u) :
    global time
    color [u] = "Gray"
    trav_time [u] [0] = time
    dfs_traversal_output.append(u)
    time +=1
    for v in Adj_list[u]:
        if color[v] == "white":
            parent[v] = u
            dfs_util(v)
    color[u] = "Blue"
    trav_time[u][1] = time
    time +=1

dfs_util("A")
print(dfs_traversal_output)
print(parent)
print(trav_time)

for node in Adj_list.keys():
    print(node, "->", trav_time[node])

    


