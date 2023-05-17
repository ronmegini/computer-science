def prim(graph, root):

    nodes = list(graph.keys())
    nodes.remove(root)

    visited = [root]
    # Dict of list
    path = {}
    next = None

    while nodes:
        # Set distance to infinity
        distance = float('inf')
        for visitedVertex in visited:
            for neighborVertex in graph[visitedVertex]:
                if neighborVertex in visited or visitedVertex == neighborVertex:
                    continue
                if graph[visitedVertex][neighborVertex] < distance:
                    distance = graph[visitedVertex][neighborVertex]
                    pre = visitedVertex
                    next = neighborVertex

        # Format the code in a dict of vertex and neighbors
        if pre in path.keys():
            path[pre] += [next]
        else:
            path[pre] = [next]
        if next in path.keys():
            path[next] += [pre]
        else:
            path[next] = [pre]
        visited.append(next)
        nodes.remove(next)

    return path


def removeEdgeMST(graph, mst, removed_edge):
    
    # If removed edge not in the MST tree - return the same graph
    firstRemovedVertex, secondRemovedVertex = removed_edge
    if secondRemovedVertex not in mst[firstRemovedVertex]:
        return mst

    # Create new graph without the edge
    updatedMST = mst.copy()
    updatedMST[firstRemovedVertex].remove(secondRemovedVertex)
    updatedMST[secondRemovedVertex].remove(firstRemovedVertex)

    CopyOriginalGraph = originalGraph.copy()

    if len(CopyOriginalGraph[firstRemovedVertex]) == 1:
        CopyOriginalGraph.pop(firstRemovedVertex)
    else:
        CopyOriginalGraph[firstRemovedVertex].pop(secondRemovedVertex)

    if len(CopyOriginalGraph[secondRemovedVertex]) == 1:
        CopyOriginalGraph.pop(secondRemovedVertex)
    else:
        CopyOriginalGraph[secondRemovedVertex].pop(firstRemovedVertex)

    # Copy sub trees
    T1 = updatedMST.copy()
    T2 = updatedMST.copy()

    # Use bfs to get reachable nodes
    blueNodes = bfs(T1, firstRemovedVertex)
    redNodes = bfs(T2, secondRemovedVertex)

    # Set the minimum weight to infinity
    minWeight = float('inf')

    newfirstVertex = None
    newSecondVertex = None 

    # Inerate over all the edges in the graph
    for edge in CopyOriginalGraph:
        for vertex in CopyOriginalGraph[edge]:
            firstVertex = edge
            secondVertex = vertex
            weight = CopyOriginalGraph[edge][vertex]
            # Is there any connected edge between blue and red vertexes
            if (firstVertex in blueNodes and secondVertex in redNodes) or (secondVertex in blueNodes and firstVertex in redNodes):
                if weight < minWeight:
                    newfirstVertex = firstVertex
                    newSecondVertex = secondVertex
                    minWeight = weight

    # Check if the graph is connected
    if newfirstVertex and newSecondVertex:
        updatedMST[newfirstVertex].append(newSecondVertex)
        updatedMST[newSecondVertex].append(newfirstVertex)

        return updatedMST
    else:
        print("Alert - Disconnected Graph")


def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    return visited

if __name__ == '__main__':

    originalGraph = {
        "A": {"B": 12, "C": 23, "D": 5},
        "B": {"A": 12, "F": 7},
        "C": {"A": 23, "D": 18, "E": 17},
        "D": {"A": 5, "C": 18, "G": 9, "F": 10},
        "E": {"C": 17, "I": 16, "J": 14},
        "F": {"B": 7, "L": 20, "D": 10},
        "G": {"D": 9, "H": 4, "J": 3},
        "H": {"G": 4, "L": 8},
        "I": {"E": 16, "K": 7},
        "J": {"G": 3, "E": 14},
        "K": {"I": 7, "L": 12},
        "L": {"K": 12, "H": 8, "F": 20}
    }

    graph = {
        "A": {"B": 12, "C": 23, "D": 5},
        "B": {"A": 12, "F": 7, "M": 9},
        "C": {"A": 23, "D": 18, "E": 17},
        "D": {"A": 5, "C": 18, "G": 9, "F": 10},
        "E": {"C": 17, "I": 16, "J": 14, "R": 3},
        "F": {"B": 7, "L": 20, "D": 10},
        "G": {"D": 9, "H": 4, "J": 3},
        "H": {"G": 4, "L": 8},
        "I": {"E": 16, "K": 7},
        "J": {"G": 3, "E": 14},
        "K": {"I": 7, "L": 12},
        "L": {"K": 12, "H": 8, "F": 20},
        "M": {"B": 9, "N": 13},
        "N": {"M": 13, "O": 11},
        "O": {"N": 11, "P": 6},
        "P": {"O": 6, "Q": 15},
        "Q": {"P": 15, "R": 19},
        "R": {"Q": 19, "S": 2, "E": 3},
        "S": {"R": 2, "T": 21},
        "T": {"S": 21, "U": 1},
        "U": {"T": 1, "V": 22},
        "V": {"U": 22, "W": 24},
        "W": {"V": 24, "X": 25},
        "X": {"W": 25, "Y": 26},
        "Y": {"X": 26, "Z": 27},
        "Z": {"Y": 27}
    }

    # Ex 1
    print("Original Graph: ")
    print(graph)
    print("MST Tree: ")
    mst = prim(graph, 'A')
    print(mst)

    # Ex 2
    print("Remove not in MST edge (A,C): ")
    print(removeEdgeMST(graph, mst, ("A", "C")))
    print("Remove edge (J,E): ")
    print(removeEdgeMST(graph, mst, ("J", "E")))
