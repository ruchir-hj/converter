"""
project : csv to json Converter
This is the driver file to run the utility

How to run:
From command line:
python run.py <complete input file path>
"""


import sys
import os

sys.path.insert(0, os.path.abspath('converter'))

from csv_to_json_converter import *

if __name__ == '__main__':
    if len(sys.argv) < 2:
        result = "please pass input filepath as command line argument"
    else:
        converterObject = Converter(str(sys.argv[1]))
        result = converterObject.convert_to_json()

    print (result)
