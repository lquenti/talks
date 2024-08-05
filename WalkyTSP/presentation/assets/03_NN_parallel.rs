n_random_numbers(0, graph_matrix.dim(), n)
    .into_par_iter()
    .map(|k| single_nearest_neighbour(graph_matrix, k))
    .min_by_key(|&(distance, _)| OrderedFloat(distance))
    .unwrap()

