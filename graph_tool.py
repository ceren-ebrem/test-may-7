class Graph:
    """
    A class to represent a graph.
    The graph is represented using an adjacency list.
    """
    def __init__(self):
        """
        Initializes an empty graph.
        The adjacency list is a dictionary where keys are nodes
        and values are lists of adjacent nodes.
        """
        self._adjacency_list = {}

    def add_node(self, node):
        """
        Adds a node to the graph.

        Args:
            node: The node to be added.
        """
        if node not in self._adjacency_list:
            self._adjacency_list[node] = []

    def add_edge(self, node1, node2, directed=False):
        """
        Adds an edge between node1 and node2.

        Args:
            node1: The first node.
            node2: The second node.
            directed: If True, the edge is directed (from node1 to node2).
                      If False, the edge is undirected.
        """
        self.add_node(node1)  # Ensure node1 exists
        self.add_node(node2)  # Ensure node2 exists

        self._adjacency_list[node1].append(node2)

        if not directed:
            self._adjacency_list[node2].append(node1)

    def get_nodes(self):
        """
        Returns a list of all nodes in the graph.
        """
        return list(self._adjacency_list.keys())

    def get_neighbors(self, node):
        """
        Returns the neighbors of a given node.

        Args:
            node: The node whose neighbors are to be returned.

        Returns:
            A list of neighbors, or None if the node is not in the graph.
        """
        return self._adjacency_list.get(node)

    def __str__(self):
        """
        Returns a string representation of the graph (adjacency list).
        """
        output = []
        for node, neighbors in self._adjacency_list.items():
            output.append(f"{node}: {', '.join(map(str, neighbors))}")
        return '\n'.join(output)

if __name__ == '__main__':
    # Example Usage
    my_graph = Graph()

    # Add nodes
    my_graph.add_node("A")
    my_graph.add_node("B")
    my_graph.add_node("C")
    my_graph.add_node("D")

    # Add edges
    my_graph.add_edge("A", "B")
    my_graph.add_edge("A", "C")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("C", "D", directed=True)
    my_graph.add_edge("D", "A") # Creates a cycle if undirected, adds to D's list if directed

    print("Nodes:", my_graph.get_nodes())
    print("\nGraph Structure (Adjacency List):")
    print(my_graph)

    print("\nNeighbors of C:", my_graph.get_neighbors("C"))
    print("Neighbors of A:", my_graph.get_neighbors("A"))

    # Example of a directed graph
    directed_graph = Graph()
    directed_graph.add_edge(1, 2, directed=True)
    directed_graph.add_edge(1, 3, directed=True)
    directed_graph.add_edge(2, 3, directed=True)
    directed_graph.add_edge(3, 1, directed=True) # Cycle

    print("\nDirected Graph Structure:")
    print(directed_graph) 