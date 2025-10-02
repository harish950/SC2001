#Define a constant for distance list
INF = float('inf')

#Parameters: graph is the adj matrix and root is the index of the start node in the matrix
def dijkstraMatrix(graph, root):

    #Initialization
    numVertices = len(graph) #num of elems in the adj matrix will give num of vertices
    distList = {node: INF for node in range(0, numVertices)}
    predecessorMap = {node: None for node in range(0, numVertices)}
    visitedSet = [0] * numVertices #S list

    distList[root] = 0 #distance to itself is 0
   
   #pick one vertex per iteration until all are processed
    for _ in range(numVertices):
        #in the first iteration, choose an arbitrary vertex for shortest dist
        minDist = INF
        currentNode = -1

        for vertex in range(numVertices):
            if visitedSet[vertex] == 0 and distList[vertex] < minDist:
                #if the node is not marked as visited
                #and distance from root is less than minDist
                minDist = distList[vertex]
                currentNode = vertex

        if currentNode == -1: #if current node is still -1 it means that there's no vertex left
            break

        visitedSet[currentNode] = 1 #Mark as processed

        for ver in range(numVertices):
            #if there exists an edge and ver has not yet been processed
            if graph[currentNode][ver] != 0 and visitedSet[ver] == 0:
                #if dist from current path to ver is less than from root, update
                if distList[currentNode] + graph[currentNode][ver] < distList[ver]:
                    distList[ver] = distList[currentNode] + graph[currentNode][ver]
                    predecessorMap[ver] = currentNode

    return distList, predecessorMap


#Sample test
def test_dijkstra():
    graph = [
        [0, 10, 5, 3, 0],
        [10, 0, 0, 1, 0],
        [5, 0, 0, 2, 0],
        [3, 1, 2, 0, 6],
        [0, 0, 0, 6, 0]
    ]

    root = 0
    distList, predecessorMap = dijkstraMatrix(graph, root)

    print("Shortest distances from node", root, ":", distList)
    print("Predecessors:", predecessorMap)

test_dijkstra()

