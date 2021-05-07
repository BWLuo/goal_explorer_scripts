# Goal 
This program reads the number of activities in an apk 

# Requirements 
You need to have installed 
  - Java
  - Python3

# Usage 
To run on a single apk use the command 
``` 
java -jar activity_counter.jar <path to apk>
```

To run on a batch of apks use the included script
```
python3 run.py <folder directory> <output directory>
```
This will run the program on all the apks inside the folder directory and output the 
results into a file in the output directory called `activity_count.txt`. Each line of the file will be the 
result for an apk. The lines follow the format 
```
<apk name> <activity count>
```
