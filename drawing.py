import matplotlib.pyplot as plt
import networkx as nx 

G = nx.Graph()

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8), (7, 9), (9, 10), (9, 11)]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.nx_agraph.graphviz_layout(G, prog='dot')


options = {
    'node_size': 1500,              # размер кружка
    'node_color': 'MediumBlue',     # цвет кружка
    'edgecolors': 'black',          # цвет границ  кружка
    'linewidths': 2,                # толщина границ кружка
    'edge_color':'MidnightBlue',    # цвет соединяющих линий
    'width': 2,                     # толщина соединяющих линий
    'font_size': 14,                # размер текста внутри кружко
    'font_color': 'white',          # цвет текста внутри кружков
}                                   # ^имена цветов: (https://colorscheme.ru/html-colors.html)

nx.draw(G, pos, with_labels=True, **options)

plt.show()