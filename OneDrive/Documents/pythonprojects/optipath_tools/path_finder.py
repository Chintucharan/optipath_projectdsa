import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    seen = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node in seen:
            continue
        seen.add(node)
        path = path + [node]

        if node == end:
            return cost, path

        for neighbor, weight in graph.get(node, []):
            if neighbor not in seen:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return float('inf'), []
