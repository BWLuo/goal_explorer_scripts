import os
import sys

# For this script pass in the output folder containing the constructed STGs
dir_path = os.path.dirname(os.path.realpath(__file__))
output_folder = os.path.abspath(sys.argv[1])

# output file for stg statistics
f = open(f"{output_folder}/stg_stats.txt", "w+")
stg_paths = [f"{output_folder}/{file}" for file in os.listdir(output_folder) if file.endswith('stg.xml')]
stg_paths.sort()

# count edges and nodes
for stg_path in stg_paths:
    print(f"Analyzing file {stg_path}")
    file_name = os.path.basename(stg_path)
    app_name = file_name[:-4]

    stg_file = open(stg_path, 'r')
    num_nodes = sum(1 for line in stg_file.readlines() if "<ScreenNode>" in line)
    stg_file.close()

    stg_file = open(stg_path, 'r')
    num_edges = sum(1 for line in stg_file.readlines() if "<TransitionEdge>" in line)
    stg_file.close()

    f.write(f"{app_name}, num_screen_nodes={num_nodes}, num_edges={num_edges}\n")

f.close()
print("DONE")
