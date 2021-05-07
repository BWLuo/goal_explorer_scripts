# Goal 
This program counts the number of call-sites to `URL.openConnection` within the apk.
We count all method invocations to methods named `openConnection` that run on any
reference type that is or is a subclass of
  - `java.net.URL`
  - `java.net.URLConnection`
  - `java.net.HttpURLConnection`

# Requirements 
You need to have installed 
  - Java
  - Python3

# Usage 
To run on a single apk use the command 
``` 
java -jar connection_counter.jar \
    <path to Android/Sdk/platforms> \
    <android.jar version to use> \
    <path to apk>
```
To run on a batch of apks use the included script
```
python3 run.py \
    <folder directory> \
    <output directory> \
    <path to Android/Sdk/platforms> \
    <android.jar version to use>
```
This will run the program on all the apks inside the folder directory and output the 
results into a file in the output directory called `connection_count.txt`. Each line of the file will be the 
result for an apk. The lines follow the format 
```
<apk name> <call-site count>
```
