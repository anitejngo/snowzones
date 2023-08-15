### snowzones


Scripts that populate snow zones from Snow load zones 2023-02-07 file sheets.


## how to use:

easy way:

update csvData files with changes (dont change the names of files)

run (it will run scripts in correct order):

```
python runall.py
```



Every script starts with snowload and ends with sheet code (for example SH01)

Paste latest csv data from google-sheet to corresponding csv file and run the script with that name.

for example:

```
open sheet SH (01) on google sheets
export its data to csv
copy all data from that csv to file: csvData/SH01.csv
run the script snowloadSH01.py
```


Script will go over all zipcodes in the file _zipcode_city_dc_snowload.csv
try to find its snowload zone in the csvData/SH01.csv via DC and populate it.

After doing this you can use statistic.py script to see the current state for example:

```
python statistic.py 
Cities with snowload data: 4109
Cities without snowload data: 4061
Cities with comment data: 1083
Cities without comment data: 7087
Cities with note data: 1625
Cities without note data: 6545

```
 
You can use validation.py script to get info about "DC" for example:

```
python validation.py

than it will ask you for a string for example you type in 010 to check all dc that start with 010

if it does not find any zipcodes without snowzone in regions that start like that it will print a message
if it does find it will store them in _no_snow_result.csv
```

