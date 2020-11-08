sunderland_residents = gdf.loc[gdf['county'] == 'Sunderland']
northmost_sunderland_lat = sunderland_residents['lat'].max()
counties_with_pop_north_of = gdf.loc[gdf['lat'] > northmost_sunderland_lat]['county'].unique()
