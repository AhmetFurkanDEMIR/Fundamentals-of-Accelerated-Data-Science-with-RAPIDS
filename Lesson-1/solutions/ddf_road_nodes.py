road_nodes = dask_cudf.read_csv('./data/road_nodes_1-08.csv', dtype=['str', 'float32', 'float32', 'str']).persist()
road_nodes.head()
