import json
import numpy as np
import matplotlib.pyplot as plt

y_min = 0
y_max = 5 * 60  # 5min


# TODO load in the data
def load_from_file(path):
    with open(path, "r") as fp:
        parsed_data = json.load(fp)
    results = parsed_data["results"]
    xs = [result["parameters"]["N"] for result in results]
    ys = [result["median"] for result in results]
    return xs, ys


for algorithm, label in [
    ("v0", "naive"),
    ("v1", "Fixed Stating Node"),
    ("v2", "Prefix Sum Caching"),
    ("v3", "Naive prune"),
    ("v4", "NN prune"),
    ("v5", "MST prune"),
    ("v6", "MST cache"),
    ("multithreaded", "Multithreaded"),
]:
    xs, ys = load_from_file(f"./results/results_{algorithm}.json")
    plt.plot(xs, ys, label=label)


plt.ylim(y_min, y_max)
plt.xlabel("Graph Size (number of vertices)")
plt.ylabel("time [s]")
plt.title("Exact Solver Single Node Performance")
ax = plt.gca()
ax.set_ylim((1e-1, 1e2))
plt.yscale("log")
ax.set_xticks(np.round(np.linspace(0, 50, 11), 2))
ax.set_xlim((0.0, 50.0))
plt.legend(fontsize="small")
# plt.show()
plt.savefig("exact-stmt.pdf")
