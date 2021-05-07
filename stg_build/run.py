import os
import subprocess
import sys
import time

# Pass in the folder containing the apks and the output folder
apk_folder = os.path.abspath(sys.argv[1])
output_folder = os.path.abspath(sys.argv[2])
apktool_path = os.path.abspath(sys.argv[3])
goal_explorer_path = os.path.abspath(sys.argv[4])
sdk_path = os.path.abspath(sys.argv[5])

print(f"Running on files within directory {apk_folder}")
print(f"Output directory: {output_folder}")

apk_paths = [f"{apk_folder}/{f}" for f in os.listdir(apk_folder)]

# output file for build statistics
f = open(f"{output_folder}/build_stats.txt", "w+")

# Run apktool to extract all the android res files to the output directory first
for path in apk_paths:
    if path.endswith('.apk'):
        print("\n\n")
        print("*** Extracting APK Resources ***")
        print(f"File: {path}")

        # run apktool to extract to an output directory first
        file_name = os.path.basename(path)
        app_name = file_name[:-4]

        apktool_out_dir = f"{output_folder}/{app_name}"
        print(f"Extracting APK resource files to {apktool_out_dir}")

        # run the apktool stored in backstage to extract all the android resources
        ex_cmd = ['java', '-jar', apktool_path, '-s', '-f', 'd', path, '-o', apktool_out_dir]
        ex_start = time.time()
        p = subprocess.Popen(ex_cmd, stdout=subprocess.PIPE)
        for line in p.stdout:
            print(line)
        p.wait()
        ex_end = time.time()
        ex_time = ex_end - ex_start

        # Run goal-explorer to generate STG in the output directory as well
        print("\n\n")
        print("*** Constructing STG ***")

        # run goal-explorer to construct stg
        ge_cmd = ['java', '-Xmx64g',
                  '-jar', goal_explorer_path, 'ge',
                  '--input', path,
                  '--api', '30',
                  '--sdk', sdk_path,
                  '--output', output_folder,
                  '-d']

        ge_start = time.time()
        p = subprocess.Popen(ge_cmd, stdout=subprocess.PIPE)
        for line in p.stdout:
            print(line)
        p.wait()
        ge_end = time.time()
        ge_time = ge_end - ge_start

        # write to stats file
        f.write(f"{app_name}, extraction_time={ex_time} (s), stg_construct_time={ge_time} (s)\n")

f.close()
print('Complete')
