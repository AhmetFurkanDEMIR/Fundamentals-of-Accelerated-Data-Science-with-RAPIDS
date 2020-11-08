exercise_graph = cudf.DataFrame()

exercise_graph['src'] = road_edges['graph_src']
exercise_graph['dst'] = road_edges['graph_dst']
exercise_graph['length_s'] = road_edges['length_s']

print(exercise_graph.shape)
exercise_graph.dtypes
