sex_groups = gdf[['sex', 'infected']].groupby(['sex'])
sex_groups.mean()
