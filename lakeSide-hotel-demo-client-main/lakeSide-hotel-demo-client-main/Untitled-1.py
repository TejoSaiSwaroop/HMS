def kosaraju(n, edges):
    def fill_order(v, visited, stack):
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                fill_order(i, visited, stack)
        stack = stack.append(v)

    def transpose_graph():
        for i in range(n):
            for j in graph[i]:
                transpose[j].append(i)

    def dfs(v, visited):
        visited[v] = True
        component.append(v)
        for i in transpose[v]:
            if not visited[i]:
                dfs(i, visited)

    graph = [[] for _ in range(n)]
    transpose = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)

    stack = []
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            fill_order(i, visited, stack)

    transpose_graph()

    visited = [False] * n
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs(v, visited)
            print(" ".join(map(str, component)))

# Input processing
n = int(input("Enter the number of edges: "))
edges = []
for _ in range(n):
    a, b = map(int, input().split())
    edges.append((a, b))

kosaraju(n, edges)