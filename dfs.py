def DFS_dist_from_node(query_node, adjList):
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
                    DFS_dist_from_node(node,adjList)
                    break
            if all(node in visited for node in adjList[query_node]):
                if len(stack)>0:
                    stack.pop()
                    if len(stack)>0:
                        DFS_dist_from_node(stack[len(stack)-1],adjList)
                    elif len(stack)==0:
                        break
            return visited



if __name__ == "__main__":
    adjList = dict()
    adjList = {1: [2], 2: [1,3,4,5], 3: [2], 4: [2,6,18], 5: [2,7,17], 6: [4,8,16], 7: [5,10,20], 8: [6,9,11], 9: [8,10,14], 10: [7,9,14], 11: [8,12,19], 12: [11,13], 13: [12,14], 14: [10,13,15], 15: [14], 16: [6], 17: [5], 18: [4], 19: [11], 20: [7]}
    visited=[1]
    stack=[1]
    dist = DFS_dist_from_node(1, adjList)
    print "visited node: ", dist
    print "stack: ", stack
