G_ex = cg.Graph()
G_ex.from_cudf_edgelist(speed_graph, source='src', destination='dst', edge_attr='length_s')
