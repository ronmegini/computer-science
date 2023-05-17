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


def update_mst(graph, mst, removed_edge):
    
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

    # Create new copies of the updated MST
    t1 = updatedMST.copy()
    t2 = updatedMST.copy()

    # Return lists of reachable nodes from each graph
    blueNodes = bfs(t1, firstRemovedVertex)
    redNodes = bfs(t2, secondRemovedVertex)

    # Initialize variables to find the connecting edge between blue & red nodes
    minWeight = float('inf')
    newfirstVertex = None
    newSecondVertex = None 

    for edge in CopyOriginalGraph:
        for vertex in CopyOriginalGraph[edge]:
            firstVertex = edge
            secondVertex = vertex
            weight = CopyOriginalGraph[edge][vertex]
            # Check if one node connects blue & red or the other way
            if (firstVertex in blueNodes and secondVertex in redNodes) or (secondVertex in blueNodes and firstVertex in redNodes):
                # Check if the weight is minimal and update
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
        print("The removed edge leads to a diconnected graph")


def bfs(graph, node):
  # Run BFS algorithm
  visited = []
  queue = []
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

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

    # Ex 1

    print("Original Graph: ")
    print(originalGraph)

    print("MST Tree: ")
    mst = prim(originalGraph, 'A')
    print(mst)

    # Ex 2
    print("Remove not in MST edge (A,C): ")
    print(update_mst(originalGraph, mst, ("A", "C")))

    print("Remove edge (J,E): ")
    print(update_mst(originalGraph, mst, ("J", "E")))
