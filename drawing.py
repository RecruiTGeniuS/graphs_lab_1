import matplotlib.pyplot as plt
import networkx as nx 



with open('trees.txt', 'r') as trees_file:
    t_nodes = trees_file.readline().split()
    t_left = trees_file.readline().split()
    t_right = trees_file.readline().split()

print(t_left)
    
    
G = nx.Graph()

nodes = []
left = []
right = []

edges = []

    
    

for i in range(len(t_nodes)):
    nodes.append(int(t_nodes[i]))
    left.append(int(t_left[i]))
    right.append(int(t_right[i]))

print(nodes)
print(left)
print(right)

reversed_nodes = set()
    

for i in range(len(nodes)):
    if right[i] == 0:
        edges.append((nodes[i], nodes[i] * -1))
        reversed_nodes.add(nodes[i] * -1)
    elif right[i] != 0:
        edges.append((nodes[i], right[i]))

    if left[i] == 0:
        edges.append((nodes[i], nodes[i] * -1))
        reversed_nodes.add(nodes[i] * -1)
    elif left[i] != 0:
        edges.append((nodes[i], left[i]))
    

print(edges)
print(reversed_nodes)

# создать map по reversed и перекрасить все узлы с -1 в белый, а также их ветки





# nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8), (7, 9), (9, 10), (9, 11)]
# edges.append((11,12)) # это как добавлять
# # (корень1, левый[значение]), (корень1, правый[значение])

G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.nx_agraph.graphviz_layout(G, prog='dot')


options = {
    'node_size': 1400,              # размер кружков
    'node_color': 'MediumBlue',     # цвет кружков
    'edgecolors': 'black',          # цвет границ  кружков
    'linewidths': 0,                # толщина границ кружков
    'edge_color':'MidnightBlue',    # цвет соединяющих линий
    'width': 1,                     # толщина соединяющих линий
    'font_size': 8,                 # размер текста внутри кружков
    'font_color': 'white',          # цвет текста внутри кружков
}                                   # ^имена цветов: (https://colorscheme.ru/html-colors.html)

nx.draw(G, pos, with_labels=True, **options)

plt.show()