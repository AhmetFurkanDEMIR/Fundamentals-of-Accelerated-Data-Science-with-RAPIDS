south_idx = cluster_centers.nsmallest(1, 'northing').index[0]
labels_predicted = dkm.predict(ddf)
labels_predicted[labels_predicted==south_idx].compute().shape[0]
