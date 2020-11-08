ddf = dask_cudf.read_parquet('pop5x')
ddf[['northing', 'easting']].mean().compute()
