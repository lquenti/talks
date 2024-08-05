fn iterative_solver<T>(graph_matrix: &T) -> Solution
where
    T: AdjacencyMatrix,
{
    let n = graph_matrix.dim();
    let mut best_permutation: Path = (0..n).collect();
    let mut best_cost = f64::INFINITY;

    let mut curr = best_permutation.clone();
    while next_permutation(&mut curr[1..]) {
        let cost = graph_matrix.evaluate_circle(&curr);
        if cost < best_cost {
            best_cost = cost;
            best_permutation = curr.clone();
        }
    }
    (best_cost, best_permutation)
}
