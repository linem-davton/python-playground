import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
matplotlib.use("Qt5Agg")


def graph_visualization(graph, parent, child, pos, level):
    """ Visualize the graph with the parent-child relationship. """

    if parent is not None:
        graph.add_edge(parent, child)
        print(f"{parent} -> {child}")
    pos[child] = (len(pos) * 2, -level)  # Position of the node in the graph

# Generate a decision tree for the permutation of [1,2,3] using swap-based backtracking


def generate_permutation_tree(vec, index=0, graph=None, pos={}, parent=None, level=0):
    """ Recursively generate a decision tree of permutations with backtracking. """

    state = tuple(vec)  # Convert list to tuple for immutability in graph
    state = str(state) + str(level)  # Add level to state to differentiate nodes
    graph_visualization(graph, parent, state, pos, level)

    if index == len(vec):
        return

    for i in range(index, len(vec)):
        vec[index], vec[i] = vec[i], vec[index]  # Swap (trying a choice)
        generate_permutation_tree(vec, index + 1, graph, pos, state, level + 1)
        vec[index], vec[i] = vec[i], vec[index]  # Swap back (backtracking)

    return


if __name__ == "__main__":
    # Generate tree for permutations of [1, 2, 3]
    vec = [1, 2, 3]
    graph = nx.DiGraph()
    pos = {}
    generate_permutation_tree(vec, graph=graph, pos=pos)

    # Draw the tree
    plt.figure(figsize=(10, 6))
    nx.draw(graph, pos, with_labels=True)
    plt.title("Decision Tree for Permutations of [1, 2, 3] with Backtracking")
    plt.show()
