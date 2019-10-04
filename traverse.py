# File: traverse.py

"""
This program implements a test to find paths that traverse each edge exactly once
"""

from graph import Graph

def traverse():
    '''
    Reads ina a graph from a text files and parses for eurlean paths
    '''
    g = Graph()
    while True:
        filename = input("Enter name of graph file: ")
        if filename == "":
            break
        if filename.find(".") == -1:
            filename += ".txt"
        g.clear()
        g.load(filename)   
        available = g.getArcs()
        nodes = g.getNodes()
        if checkIfEuler(g) == False:
            print("No such path exists")
        for starting_point in available:
            newList=available.copy()
            traverseAll(g, newList,starting_point, [])  

def checkIfEuler(graph):
    '''
    Uses the notion "A graph has an Euler path if and only 
    if there are at most two vertices with odd degree." to
    return an error in cases of no path.
    '''
    i=0
    for node in graph.getNodes():
        if len(node.getArcsFrom())%2 == 1:
            i+=1
    if i >= 3:
        return False
    else:
        return True


def removeFullArc(graph,arc,unvisited):
    '''
    Removes the full undirected arc from a given list
    '''
    rev = removeReverseArc(graph,arc,unvisited)
    unvisited.remove(arc)


def removeReverseArc(graph,arc,unvisited):
    '''
    Removes an arc going the opposing direction of the input
    (helper for removing an undirected arc)
    '''
    for rev in unvisited:
        if rev.getStart() == arc.getFinish() and rev.getFinish() == arc.getStart():
            unvisited.remove(rev)
            break;

def traverseAll(graph,unvisited,start, path):
    '''
    Creates a list of unvisited arcs and recursively calls itself
    on a smaller list of unvisited. If it doesn't have any more
    arcs that meet the condition of having a matching end point 
    for the next arc to start from, it moves on.
    '''
    removeFullArc(graph,start,unvisited)
    if unvisited == []:
        if path[-1].getFinish() == start.getStart():
            path.append(start)
            print(path)
            return path
        else:
            return []
    #Checks if the last item's endpoint is the same as your start point's beginnign
    if path == [] or path[-1].getFinish() == start.getStart():
        path.append(start)
        for neighbor in start.getFinish().getArcsFrom():
            if neighbor in unvisited:
                newList=unvisited.copy()
                # print(neighbor, newList)
                traverseAll(graph, newList, neighbor,path)
    else:
        return False
    
# Startup code

if __name__ == "__main__":
    traverse()
