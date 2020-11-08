ddf = ddf.map_partitions(convert_to_grid, meta=meta_dtypes)
ddf = ddf.persist() # optional

# `ddf` now contains `easting` and `northing` columns that we can use as we would with any other Dask dataframe.
print(ddf['easting'].mean().compute())
