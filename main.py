# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Edmonds-Karp Algorithm
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

newlabels = {}


def max_flow(c, s, t, n):
    f = [[0] * n for i in range(n)]
    path = bfs(c, f, s, t)
    #  print path

    while path != None:
        flow = min(c[u][v] - f[u][v] for u, v in path)
        for u, v in path:
            f[u][v] += flow
            f[v][u] -= flow
            a = (u, v)
            z=list(newlabels[a].keys())[0]
            newlabels[a][z]+=flow
            print(f"{u},{v} : {newlabels[a]}")
        print("XD")
        path = bfs(c, f, s, t)

    return sum(f[s][i] for i in range(n))


# find path by using BFS
def bfs(c, f, s, t):
    queue = [s]
    paths = {s: []}
    u = 0
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(c)):
            if (c[u][v] - f[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == t:
                    return paths[v]
                queue.append(v)
    print(paths[u])
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # make a capacity graph
    # node   s   o   p   q   r   t
    C = [[0, 3, 3, 0, 0, 0,,],  # s
         [0, 0, 2, 3, 0, 0,,],  # o
         [0, 0, 0, 0, 2, 0,,],  # p
         [0, 0, 0, 0, 4, 2,,],  # q
         [0, 0, 0, 0, 0, 2,,],  # r
         [0, 0, 0, 0, 0, 2,,],
         [0, 0, 0, 0, 0, 2,,],
         [0, 0, 0, 0, 0, 3,,]]  # t

    start = 0  # A
    end = 5  # F
    A = np.matrix(C)
    n = len(C)
    G = nx.DiGraph(A)
    labels = nx.get_edge_attributes(G, "weight")
    for i in labels:
        newlabels[i] = {labels[i]:0}
    max_flow_value = max_flow(C, start, end, n)
    print("Edmonds-Karp algorithm")
    print("max_flow_value is: ", max_flow_value)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=newlabels)
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
