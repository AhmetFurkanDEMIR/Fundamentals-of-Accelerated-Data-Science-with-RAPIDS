rev_gdf = cudf.DataFrame()

rev_gdf['src'] = exercise_graph['dst']
rev_gdf['dst'] = exercise_graph['src']
rev_gdf['length_s'] = exercise_graph['length_s']

exercise_graph = cudf.concat([exercise_graph, rev_gdf], 
                              ignore_index=True)

print(exercise_graph.shape)

exercise_graph.drop_duplicates(subset=['src', 'dst'], inplace=True)
print(exercise_graph.shape)

# The maximum graph_id is the number of nodes - 1
print(exercise_graph[['src', 'dst']].max().max() == road_nodes['node_id'].unique().shape[0] - 1)

# The minimum graph_id is 0 
print(exercise_graph[['src', 'dst']].min().min() == 0)

# The ID dtypes are int32s
print(exercise_graph[['src', 'dst']].dtypes == 'int32')
