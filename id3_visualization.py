# for tree visualization
from id3 import id3
import pandas as pd
from graphviz import Digraph


def build_graph(tree, graph=None, parent=None, edge_label="", node_id=None):
    if graph is None:
        graph = Digraph(format='png')
        graph.attr('node', shape='box', style='filled', color='lightblue2')

    # Generate a unique ID for this node
    if node_id is None:
        node_id = str(id(tree))

    if not isinstance(tree, dict):
        # Leaf node
        leaf_id = str(id(tree))
        graph.node(leaf_id, label=str(tree), shape='ellipse', style='filled', color='lightgreen')
        if parent:
            graph.edge(parent, leaf_id, label=edge_label)
        return graph

    # It's a decision node
    for attribute, branches in tree.items():
        graph.node(node_id, label=str(attribute), shape='box', style='filled', color='lightblue2')
        if parent:
            graph.edge(parent, node_id, label=edge_label)

        for value, subtree in branches.items():
            # Each child gets a unique node ID
            child_id = str(id(subtree))
            build_graph(subtree, graph, parent=node_id, edge_label=str(value), node_id=child_id)

    return graph


# Load the dataset from CSV file
df = pd.read_csv("dataset.csv")

# Build the decision tree using ID3 algorithm
tree_result = id3(df, list(df.columns), 'lenses')

# Visualize the decision tree
graph = build_graph(tree_result)
print("Decision Tree:", tree_result)
graph.render('decision_tree', format="svg", view=True)