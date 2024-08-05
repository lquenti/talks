import os
import re
import math
import statistics

import matplotlib.pyplot as plt

FOLDER_PATH_V0 = './v0_constgraphsize'
FOLDER_PATH_V1 = './v1_constgraphsize'
MATCH_FOR_STARTING = "elapsed seconds: "

def extract_nodes_and_processes(file_path):
    pattern = r'output_(\d+)_nodes_(\d+)_taskspernode\.txt'
    match = re.search(pattern, file_path)
    if match:
        nodes = int(match.group(1))
        processes = int(match.group(2))
        return (nodes, processes)
    else:
        return None

def get_measurements(file_path):
    measurements = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            if line.startswith(MATCH_FOR_STARTING):
                measurement = float(line.split(":")[1].strip())
                measurements.append(measurement)
    return measurements

def find_matched_files(folder_path):
    files = os.listdir(folder_path)

    matched_files = []
    for file in files:
        file_path = os.path.join(folder_path, file)
        nodes_processes = extract_nodes_and_processes(file)
        if nodes_processes:
            measurements = get_measurements(file_path)
            matched_files.append((nodes_processes, measurements))

    return sorted(matched_files, key=lambda item: item[0][0] * item[0][1])

xs_v0 = find_matched_files(FOLDER_PATH_V0)
xs_v1 = find_matched_files(FOLDER_PATH_V1)

def process_findings(findings):
    ((nodes, processes), measurements) = findings
    total_workers = nodes * processes
    mean = statistics.mean(measurements)
    stdev = statistics.stdev(measurements)
    
    # Assuming prefix length 3
    total_number_of_prefixes = 50*49*48
    prefixes_per_sec_per_worker = total_number_of_prefixes / (mean * total_workers)

    print(f"{nodes}n{processes}p & {total_workers} & {mean:.3f} & {stdev:.3f} & {prefixes_per_sec_per_worker:.3f}\\\\")

# create tables
print("v0")
for x in xs_v0:
    process_findings(x)
print()

print("v1")
for x in xs_v1:
    process_findings(x)

# create plot
def create_plot(xs, label):
    xs = [(nodes*processes, statistics.mean(measurements)) for ((nodes,processes), measurements) in xs]

    # get only the fastest one for each number of worker
    new_xs = {}
    for x in xs:
        (workers, mean) = x
        if workers not in new_xs:
            new_xs[workers] = mean
            continue
        # choose the minimum
        new_xs[workers] = min(new_xs[workers], mean)
    new_xs = [*sorted(new_xs.items(), key=lambda item: item[0])]
    xs, ys = zip(*new_xs)
    plt.plot(xs, ys, label=label)

create_plot(xs_v0, "v0: statically partitioned")
create_plot(xs_v1, "v1: dynamically partitioned")
plt.legend()
plt.xlabel("number of processes")
plt.ylabel('time [s]')
plt.title("Exact Solving MPI (n=50)")
#plt.show()
plt.savefig("exact-mpi.pdf")
