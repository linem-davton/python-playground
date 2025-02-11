import networkx as nx
import matplotlib.pyplot as plt

# Generate a decision tree for the permutation of [1,2,3] using swap-based backtracking


def generate_permutation_tree(nums, index=0, parent=None, graph=None, pos=None, level=0):
    """ Recursively generate a decision tree of permutations with backtracking. """
    if graph is None:
        graph = nx.DiGraph()
        pos = {}

    state = tuple(nums)  # Convert list to tuple for immutability in graph

    if parent is not None:
        graph.add_edge(parent, state)

    pos[state] = (index, -level)

    if index == len(nums):
        return graph, pos

    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]  # Swap (trying a choice)
        generate_permutation_tree(nums, index + 1, state, graph, pos, level + 1)
        nums[index], nums[i] = nums[i], nums[index]  # Swap back (backtracking)

    return graph, pos


# Generate tree for permutations of [1, 2, 3]
nums = [1, 2, 3]
graph, pos = generate_permutation_tree(nums)

# Draw the tree
plt.figure(figsize=(10, 6))
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
plt.title("Decision Tree for Permutations of [1, 2, 3] with Backtracking")
plt.show()
