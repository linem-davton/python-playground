import networkx as nx
import matplotlib.pyplot as plt


def coin_change_graph(N, coins):
    G = nx.DiGraph()
    queue = [(0, [])]

    while queue:
        current_sum, path = queue.pop(0)
        node_label = f"{path} (Sum: {current_sum})"
        G.add_node(node_label)

        for coin in coins:
            next_sum = current_sum + coin
            if next_sum <= N:
                new_path = path + [coin]
                child_label = f"{new_path} (Sum: {next_sum})"
                G.add_edge(node_label, child_label, label=f"+{coin}")
                queue.append((next_sum, new_path))

    return G


def draw_graph(G):
    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")  # Use graphviz 'dot' layout for tree structure
    labels = nx.get_edge_attributes(G, 'label')
    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_size=2500, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=9)
    plt.title("Coin Change Graph")
    plt.show()


if __name__ == "__main__":
    N = 5
    coins = [1, 2, 3]
    G = coin_change_graph(N, coins)
    draw_graph(G)
