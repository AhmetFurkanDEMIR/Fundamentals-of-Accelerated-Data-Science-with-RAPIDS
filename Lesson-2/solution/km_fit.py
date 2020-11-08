km.fit(gdf)
gdf['cluster'] = km.labels_
km.cluster_centers_
