distances, indices = knn.kneighbors(hospitals[['easting', 'northing']], 3) # order has to match the knn fit order (east, north)
