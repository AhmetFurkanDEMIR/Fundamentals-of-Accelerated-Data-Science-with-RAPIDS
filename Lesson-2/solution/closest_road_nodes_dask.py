distances, indices = dask_knn.kneighbors(road_nodes[['north', 'east']], k=1)
distances.persist()
indices.persist()
