## Traversal
This program implements a test to find paths that traverse each edge exactly once. PS3 396
To run part 1 of homework, use `py traversal.py` then test with a text file such as Bridges.txt (should not have a Eurlean path). 

## Code review
In terms of functionality, it would be helpful to have an easier way of assessing arcs that are representing the same undirected path. 
As it stands right now, reading in an undirected graph from a text file creates two separate arc objects to represent going from A to B and from B to A.
This can be relatively confusing when one wants to count a specific arc as visited. One way to remedy this would be to store some attribute that 
designated "related" arcs that allows them to point to each other.

Another difficulty I saw was with looking to construct arcs by name. Since arcs are stored by name as "NODE1 -> NODE2", it can be difficult to look
up an arc based on its components. It might be easier if these values were stored as a tuple that could be indexed using node names so one might be able to 
find or delete an arc which meets the requirements one sets for its endpoints.

In general, the `graph.py` documentation and functionality made enough sense to pick up for this assignment, and I liked the way I was able
 to quickly iterate through the neighbors of a node as needed. The print out for the graph felt like it communicated information quite well.
