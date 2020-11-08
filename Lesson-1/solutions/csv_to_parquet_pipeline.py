ddf = dask_cudf.read_csv('./data/pop5x_1-07.csv')
ddf = ddf.map_partitions(latlong2osgbgrid_dask)
ddf.to_parquet('pop5x')
