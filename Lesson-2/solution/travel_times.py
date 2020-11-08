# We chose to start with a highly connected node again, but you could have chosen any.
# If you have time, see what the SSSP visualization looks like starting from nodes at different extreme coordinates,
# or one of the end nodes of an especially long edge, or even one of the nodes unreachable from the main road network.
ex_deg = G_ex.degree()
ex_node = ex_deg.nlargest(1, 'degree')

%time ex_dist = cg.sssp(G_ex, ex_node['vertex'][0])

# limiting to those nodes that were connected (within ~4.3 billion seconds; .sssp uses the max int value for unconnected nodes)
print(ex_dist.head())
ex_dist['distance'].loc[ex_dist['distance'] < 2**32].describe()[1:]
