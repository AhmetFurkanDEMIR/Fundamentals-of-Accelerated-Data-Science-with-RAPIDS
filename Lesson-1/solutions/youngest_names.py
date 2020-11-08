name_groups = gdf[['name', 'age']].groupby('name')

name_ages = name_groups['age'].mean()
name_counts = name_groups['age'].count()

ages_counts = cudf.DataFrame()
ages_counts['mean_age'] = name_ages
ages_counts['count'] = name_counts

ages_counts = ages_counts.sort_values('mean_age')
ages_counts.iloc[:3]
