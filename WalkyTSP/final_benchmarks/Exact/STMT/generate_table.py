import json

y_min = 0
y_max = 5*60 # 5min

# TODO load in the data
def load_from_file(path):
    with open(path, 'r') as fp:
        parsed_data = json.load(fp)
    results = parsed_data['results']
    xs = [result["parameters"]["N"] for result in results]
    ys = [result["median"] for result in results]
    return xs,ys

for (algorithm, label) in [
        ("v0", "naive"),
        ("v1", "Fixed Stating Node"),
        ("v2", "Prefix Sum Caching"),
        ("v3", "Naive prune"),
        ("v4", "NN prune"),
        ("v5", "MST prune"),
        ("v6", "MST cache"),
        ("multithreaded", "Multithreaded")
        ]:
    xs,ys = load_from_file(f"./results/results_{algorithm}.json")
    print(f"BEGIN ALGORITHM {label}")
    for i in range(len(xs)):
        print(f"size {xs[i]} = {ys[i]:.3f}")
    print(f"END ALGORITHM {label}")
    print()
