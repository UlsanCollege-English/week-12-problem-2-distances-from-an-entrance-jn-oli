from collections import deque

def bfs_distances(graph, start):
    # If start node is not in graph at all → return empty dict
    if start not in graph:
        return {}

    dist = {start: 0}
    q = deque([start])

    while q:
        node = q.popleft()
        d = dist[node]

        for nei in graph.get(node, []):
            if nei not in dist:      # do not revisit
                dist[nei] = d + 1
                q.append(nei)

    return dist
