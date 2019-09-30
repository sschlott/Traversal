# File: traverse.py

"""
This program implements a test to find paths that traverse each edge exactly once
"""

from graph import Graph

def traverse():
    """Tests the Hopcroft-Tarjan algorithm for finding articulation points."""
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
        traverseAll(g, available,available[0], [])   

def removeFullArc(graph,arc,unvisited):
    # newList = unvisited.copy()
    rev = removeReverseArc(graph,arc,unvisited)
    unvisited.remove(arc)


def removeReverseArc(graph,arc,unvisited):
    for rev in unvisited:
        if rev.getStart() == arc.getFinish() and rev.getFinish() == arc.getStart():
            unvisited.remove(rev)
            break;

def traverseAll(graph,unvisited,start, path):
    if path == []:
        path.append(start)
    elif path[-1].getFinish() == start.getStart():
        path.append(start)
    else: 
        print("wah",path,start)
        return []
    if unvisited == []:
        print("found a good path", path)
        return path

    removeFullArc(graph,start,unvisited)
    newList=unvisited.copy()
    for neighbor in start.getFinish().getArcsFrom():
        if neighbor in unvisited:
            traverseAll(graph, newList, neighbor,path)

        




# Startup code

if __name__ == "__main__":
    traverse()
