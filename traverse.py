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
        traverseAll(g)   
        print(g)  

def traverseAll(graph):
    for arc in graph.getArcs():
        arc.walked= False
    for node in graph.getNodes():
        for arc in node.getArcsFrom():
            traverseAsStart(graph,arc)



def walkedSisterArc(start,finish,graph):
    for arc in graph.getArcs():
        if arc.getStart() == finish and arc.getFinish() == start:
            arc.walked = True
            print("Fixed", start,finish, arc)
            break; 
        
def traverseAsStart(graph,start):
    start.walked = True
    walkedSisterArc(start.getStart(),start.getFinish(),graph)
    for 


# Startup code

if __name__ == "__main__":
    traverse()
