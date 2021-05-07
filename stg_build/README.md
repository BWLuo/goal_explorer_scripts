# Goal
This script parses helps to build the Static Transition Graph (STG) using Goal-Explorer and
also collects some build statistics such as:
  - Time used in extracting apk resources using Apktool 
  - Time used to build STG 

# Requirements
You need to have installed
  - Android Sdk (Preferably through Android Studio)
  - Java
  - Python3 

# Usage
This will build an STG for each of the apk files in the specified apk directory and create a 
file named `build_stats.txt` in the specified output directory containing the build 
statistics. 

### Example command
```
python3 run.py <apk directory> \
    <output directory> \
    <apktool.jar path> \
    <goalexplorer.jar path> \
    <Android/Sdk path>  
```

### Output file format 
Each line in the file corresponds to build statistics of one apk. The lines follow the format
```
<apk name>, extraction_time=<#number> (s), stg_construct_time=<#number> (s)
```
As indicated, the times are in units of seconds. 
  - Extraction time: time used by apktool.jar to extract apk resource files 
  - STG construct time: time used by goalexplorer.jar to construct the STG 