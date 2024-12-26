import heapq

class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)

def A_Star(graph, start, destination, heuristic):
    openset = MinPriorityQueue()
    openset.push((heuristic.get(start, 0) + 0, 0, start, None))

    gscore = {node: float('inf') for node in graph.node_list}
    predecessors = {node: None for node in graph.node_list}
    gscore[start] = 0

    while len(openset) != 0:
        _, cost_to_node, current, pred = openset.pop()

        if current == destination:
            break

        for neighbor in graph.adjacent_nodes(current):
            weight = graph.w(current, neighbor)
            new_cost = cost_to_node + weight
            if new_cost < gscore[neighbor]:
                gscore[neighbor] = new_cost
                predecessors[neighbor] = current
                estimated_total_cost = new_cost + heuristic.get(neighbor, 0)
                openset.push((estimated_total_cost, new_cost, neighbor, current))

    path = []
    step = destination
    total_distance = gscore[destination]  # Retrieve the total cost from start to destination

    while step != start:
        path.append(step)
        step = predecessors[step]
    path.append(start)
    path.reverse()

    return path, total_distance  # Return the path and the total distance
