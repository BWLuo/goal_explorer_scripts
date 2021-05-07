# Goal
This script parses the Static Transition Graph (STG) files produced by Goal-Explorer and 
produces a file with the statistics
  - Number of screen nodes
  - Number of transitions edges

# Requirements
You need to have installed
- Python3 

# Usage
This will analyze all the STG.xml files within the specified directory then create a file 
named `stg_stats.txt` within the same directory

### Example command
```
python3 run.py <directory> 
```

### Output file format 
Each line in the file corresponds to one of the STGs analyzed. The lines follow the format
```
<apk name>, num_screen_nodes=<# screen nodes>, num_edges=<# transition edges> 
```
