import heapq

INF = float('inf')

def dijkstraList(graph, root):
    numVertices = len(graph)
    distList = {node: INF for node in range(0, numVertices)}
    predecessorMap = {node: -1 for node in range(0, numVertices)}
    #visitedSet = [0] * numVertices -> Don't need because we using heap

    distList[root] = 0
    minHeap = [(0, root)] #tuple (distance, vertex)

    while minHeap:
        distToRoot, currentNode = heapq.heappop(minHeap)

        #If the current distance is larger than recorded distance skip
        #This is because heapq can have multiple entries for the same node
        #Each time you find a shorter path, you push, old entries don't disappear
        if distToRoot > distList[currentNode]:
            continue #Basically this line is to ensure that you never process the same node twice

        for vertex, weight in graph.get(currentNode, []):
            #If current path shorter, then update
            if distList[currentNode] + weight < distList[vertex]:
                distList[vertex] = distList[currentNode] + weight
                predecessorMap[vertex] = currentNode
                heapq.heappush(minHeap, (distList[vertex], vertex))

    return distList, predecessorMap


#Sample test
def test_dijkstra_list():
    graph = {
        0: [(1, 10), (2, 5), (3, 3)],
        1: [(0, 10), (3, 1)],
        2: [(0, 5), (3, 2)],
        3: [(0, 3), (1, 1), (2, 2), (4, 6)],
        4: [(3, 6)]
    }

    root = 0
    distList, predecessorMap = dijkstraList(graph, root)

    print("Shortest distances from node", root, ":", distList)
    print("Predecessors:", predecessorMap)

test_dijkstra_list()
