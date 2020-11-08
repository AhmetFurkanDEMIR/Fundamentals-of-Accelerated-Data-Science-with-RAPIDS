G_ex = cg.Graph()
G_ex.from_cudf_edgelist(road_edges, source='src_id', destination='dst_id', edge_attr='length_s')
