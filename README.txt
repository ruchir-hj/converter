About this project
------------------
This project provides a simple utility that converts a CSV file
into a JSON file by applying few normalization rules on the data
records.
This project is tested on unix platform using Python 2.7

Assumptions
-----------
Following are the important assumptions made in this project ->

1.) The input will always be a valid CSV file with records in
one of the following formats ->

Lastname, Firstname, (703)-742-0996, Blue, 10013
Firstname Lastname, Red, 11237, 703 955 0373
Firstname, Lastname, 10013, 646 111 0101, Green

However, it is easy to extend this project to other formats as well,
if in case any other format come in future. It is discussed in more details in "Possible Extensions" section.

2.) A valid Phone number will have 10 digits and does not contain ISD codes. It can however have "-", "(", ")" , " "  characters. It will be
normalized to an appropriate format.
But numbers like +1-xxx-xxx-xxxx are not considered valid as it
contains ISD code. Also since phone numbers are assigned to each individual, special numbers (like 911) are considered invalid.
However, in case if in future ISD codes also come in picture then the code can be extended very easily to handle it. It is discussed in more details in "Possible Extensions" section.

3.) A valid zip code will have five digits in it. This is not true for every country but US zipcodes contain 5 digits. If in future International zip codes with number of digits are also added in input data, then again it is very easy to extend the code to handle it. It is discussed in more details in "Possible Extensions" section.

4.) Only following colors are considered valid as of now ->
'blue', 'green', 'red', 'yellow', 'aqua marine', 'violet', 'orange',
'black', 'brown', 'white', 'pink', 'gray'.
In case, more colors are to be considered  valid, it is very easy to add
more valid colors. It is discussed in more details
in "Possible Extensions" section.

5.) It is assumed that data can remain in memory. Since data is also sorted by this utility, it is assumed that data can remain in memory. If
data cannot remain in memory then again the code can be extended to handle this case. It is discussed in more details in "Possible Extensions" section.

Directory Structure -
--------------------

Following is the directory structure of this project ->

   csvToJsonConverter
         |
         |--------- converter    [This directory contains source code]
         |            |
         |            |-------- csv_to_json.py
         |            |
         |            |-------- constants.py
         |
         |
         |---------- input
         |            |
         |            |
         |            |-------- data.in
         |
         |
         |---------- output       [This direcory contains output file]
         |            |
         |            |-------- output_<timestamp>.json
         |            |
         |
         |----------- tests       [This direcory contains unit tests]
         |             |
         |             |------- test_csv_to_json_converter.py
         |             |
         |
         |----------- run.py      [driver file]
         |
         |----------- README

The file run.py is the driver file.
The file csvToJsonConverter/converter/csv_to_json.py contains main source code.
The file csvToJsonConverter/converter/constants.py contains various constants.
The unit tests are contained in file csvToJsonConverter/tests/test_csv_to_json_converter.py


How to run -
-----------

This project is tested on unix platform using Python 2.7

Running steps ->
1.) cd to project directory -> csvToJsonConverter/

2.) Run the python file run.py from command line interface by giving
complete input filepath as command line argument.
It can be executed in following way ->

python run.py <complete path to input data file>
For e.g. ->
python run.py /Users/ruchirhajela/Downloads/csvToJsonConverter/input/data.in

run.py is the driver file for this utility.

3.) Check the output in directory csvToJsonConverter/output/
The output JSON file is created here with the name ->
output_<current timestamp>.json

4.) If you also want to run unit tests then it can be run in following way ->
cd to csvToJsonConverter/tests
execute -> python test_csv_to_json_converter.py


Design vs Performance -
----------------------
This project is designed in such a way that it is easier to extend it
for different record formats and record fields. As this is a utility which is used to normalize data items and generate JSON, stress is given
more on easier extensibility of project instead of performance.
However, if any item in constants.py becomes bigger it should be converted to set instead of a list. As lookup on a set is much faster than a list, it will keep the performance high.


Possible Extensions -
--------------------

1.) Handling other new formats ->

If any new record format comes in future it is very easy to extend the code to handle it. You have to write another method to normalize this format like _normalize_format_<number> and add condition for this format
in get_normalized_entries method. Rest of the code will remain untouched.

2.) Handling phone numbers with ISD code or different number of digits or
even more different formats of phone numbers ->

If more formats of phone numbers need to be handled in future then the code can be extended very easily in following way ->

* Add valid number of digits in VALID_PHONENUMBER_LENGTHS constant in constants.py
* Add more characters like '+' in INVALID_CHARS_IN_PHONENUMBER in constants.py
* Add condition in _normalize_phonenumber method.
Rest of the code will remain untouched.

3.) Handling International zip codes which can have different number of digits in zip code.

* Add  valid number of digits in a zipcode in VALID_ZIPCODE_LENGTH in constants.py
Rest of the code will remain untouched.

4.) If more colors are needed to be considered valid in future.

* Add those colors in set VALID_COLORS in constants.py
Rest of the code will remain untouched.

5.) What is whole data cannot be in memory.

To handle this there are multiple ways of doing it. There can be a flag in the beginning which can be set by checking current memory and size of input data file. If this flag is set then a different driver should execute the code.
In that case, we will need to write a different driver file, which can keep dumping the data as we read. In the end code needs to be extended to merge the different jsons constructed. Also for sorting, external merge sort needs to happen as whole data cannot be in memory.
If we have access to a distributed system, then the driver can send different chunks of data to different machines and execute this code on different machines for that chunk only. In the end JSONs from different machines should be merged. Again sorting can happen on different machines, but an external merge sort will be required while merging.


Please reach out to me at ruchir.hajela@gmail.com for any questions. Thanks.
