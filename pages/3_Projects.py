import networkx as nx
import streamlit as st
from pyvis.network import Network

st.title('Grafos interativos')
nx_graph = nx.DiGraph()
nx_graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 2), (4, 6)])
nx_graph.nodes[1]['title'] = 'Number 1'
node_size = 50
nx_graph.add_node(1, size=node_size, title='1', group=2, label='1')
nx_graph.add_node(2, size=node_size, title='2', group=2, label='2')
nx_graph.add_node(4, size=node_size, title='4', group=1, label='4')
nx_graph.add_node(3, size=node_size, title='3', group=2, label='3')
nx_graph.add_node(5, size=node_size, title='5', group=2, label='5')
nx_graph.add_node(6, size=node_size, title='6', group=1, label='6')

nt = Network('1000px', '2500px')
nt.toggle_physics(True)
nt.from_nx(nx_graph)
nt.show('nx.html')
