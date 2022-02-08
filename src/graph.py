import matplotlib.pyplot as plt
import networkx as nx

G = nx.read_gml('../data/color_map.gml', label = 'id')
color_map = nx.get_node_attributes(G, "color").values()
nx.draw(G, node_color = color_map, node_size = 400, width = 1.3)
plt.show()
