import os
import re
import subprocess
import sys
import time


# Script to run the activity_counter.jar on a directory of apks
# Takes in the apk_folder dir and creates an activity_count.txt file in the output dir
dir_path = os.path.dirname(os.path.realpath(__file__))

apk_dir = os.path.abspath(sys.argv[1])          # apk folder
out_dir = os.path.abspath(sys.argv[2])          # output folder

res_file = f"{out_dir}/activity_count.txt"

print(f"Running on files within directory {apk_dir}")
print(f"Output file: {res_file}")

# output file for results
res = open(res_file, "w+")

# run our java program on all the apks in sequences
for apk in os.listdir(apk_dir):
    apk_path = f"{apk_dir}/{apk}"

    if os.path.isfile(apk_path) and apk_path.endswith('.apk'):
        print("\n\n")
        print("*** Analyzing Next File ***")
        print(f"File: {apk_path}")

        # run the activity_counter.jar
        cmd = ['java', '-jar', f"{dir_path}/activity_counter.jar", apk_path]

        start = time.time()
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        p.wait()
        end = time.time()
        print(f"Analysis took {end-start} seconds")

        # parse the last line of stdout for the result
        activity_count = str(p.stdout.readlines()[-1])
        print(activity_count)
        # parsing output
        activity_count = re.sub('[^0-9]', '', activity_count)

        app_name = apk[:-4]
        res.write(f"{app_name} {activity_count}\n")

res.close()
