import streamlit as st
from pyvis.network import Network
from streamlit_agraph import agraph, Node, Edge, Config
import networkx as nx

st.title('Graph Streamlit_agraph')


def ego_graph():
    # First create a graph using the Barabasi-Albert model
    n = 2000
    m = 2
    G = nx.generators.barabasi_albert_graph(n, m)

    # Then find the node with the largest degree;
    # This node's egonet will be the focus of this example.
    node_and_degree = G.degree()
    most_connected_node = sorted(G.degree, key=lambda x: x[1], reverse=True)[0]
    degree = G.degree(most_connected_node)

    # Create egonet for the focal node
    hub_ego = nx.ego_graph(G, most_connected_node[0])

    # Now create the equivalent Node and Edge lists
    nodes = [Node(id=i, label=str(i), size=20) for i in hub_ego.nodes]
    edges = [Edge(source=i, target=j, type="CURVE_SMOOTH") for (i, j) in G.edges
             if i in hub_ego.nodes and j in hub_ego.nodes]

    config = Config(width=2500,
                    height=1500,
                    directed=True,
                    nodeHighlightBehavior=True,
                    highlightColor="#F7A7A6",  # or "blue"
                    collapsible=False,
                    node={'labelProperty': 'label'},
                    )

    return agraph(nodes=nodes,
                  edges=edges,
                  config=config)


def gera_grafo():
    nodes = []
    edges = []
    n_size = 40
    img_shape = "circularImage"
    relationship = ""
    _nodes = [["4", "MCID601", n_size, img_shape,
               ""],
              ["5", "CDCD200", n_size, img_shape,
               ""],
              ["1", "VIPD248", n_size, img_shape, ""],
              ["2", "ANCD020", n_size, img_shape, ""],
              ["3", "BICD020", n_size, img_shape, ""]]

    _edges = [["4", relationship, "5"], ["5", relationship, "1"], ["1", relationship, "2"],
              ["1", relationship, "3"], ["2", relationship, "4"]]

    for it in _nodes:
        nodes.append(Node(id=it[0], label=it[1], size=it[2], shape=it[3], image=it[4], color='6B8E23'))

    for ed in _edges:
        edges.append(Edge(source=ed[0], label=ed[1], target=ed[2]))

    config = Config(width=2500,
                    height=1500,
                    directed=True,
                    physics=True,
                    hierarchical=False,
                    font_color='Black'
                    )

    return agraph(nodes=nodes,
                  edges=edges,
                  config=config)


with st.container():
    first, second, third = st.columns(3)
    with st.form('grafo'):
        with first:
            rotina = st.text_input('Rotina', max_chars=8)
        with second:
            grupo = st.text_input('Grupo', max_chars=5)
        with third:
            ambiente = st.selectbox(label='Grupo', options=['BR', 'B2', 'B3', 'HM'], key='grupo')
        submitted = st.form_submit_button("Submit")
        if submitted:
            nt = Network('1000px', '2500px')
            # agraph_obj = gera_grafo()
            agraph_obj = ego_graph()
