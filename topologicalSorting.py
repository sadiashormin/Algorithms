def topologicalSorting(query_node, adjList):
    print "visited node: ", visited
    print "stack: ", stack
    #visited.append(query_node)
    while len(stack)>=0:
        if adjList[query_node]:
            print ""
            for node in adjList[query_node]:
                if node not in visited:
                    visited.append(node)
                    stack.append(node)
                    topologicalSorting(node,adjList)
                    break
            if all(node in visited for node in adjList[query_node]):
                if len(stack)>0:
                    sortedList.append(stack[len(stack)-1])
                    print "sorted:" , sortedList
                    stack.pop()
                    if len(stack)>0:
                        topologicalSorting(stack[len(stack)-1],adjList)
                    elif len(stack)==0:
                        break
        else:
            sortedList.append(stack[len(stack)-1])
            print "sorted:" , sortedList
            stack.pop()
            if len(stack)>0:
                topologicalSorting(stack[len(stack)-1],adjList)

        return sortedList
def printList(dist):
    for node in range(len(dist)):
        if node==len(dist)-1:
            print aplhaList[dist[node]],
        else:
            print aplhaList[dist[node]], "-->" , 

if __name__ == "__main__":
    adjList = dict()
    adjList = {0: [1,2], 1: [4,6], 2: [5], 3: [0,2,5], 4: [], 5: [], 6: [4,5]}
    aplhaList=['a','b','c','d','e','f','g']
    visited=[0]
    stack=[0]
    sortedList=[]
    dist = topologicalSorting(0, adjList)
    printList(dist)


    #print "visited node: ", dist
    #print "stack: ", stack
