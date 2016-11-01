"""
project : csv to json Converter
Converts CSV file to a JSON file
by applying normalization rules.
"""

import json
import datetime
import os
from constants import *


class Converter(object):

    def __init__(self, input_csv_file_path):
        """
        Args: complete file path for input csv file
        """
        self.input_csv_file_path = input_csv_file_path



    def convert_to_json(self):
        """
        converts input csv file to output json file
        Returns: string containing path of output json file
        output json file: output_<current timestamp>.json
        """

        line_number = 0
        errors = []
        entries = []
        json_dict = {}

        try:
            f = open(self.input_csv_file_path)
            for line in f:
                line_list = line.split(',')
                line_list = self.format_line_list(line_list)


                current_entry_dict = self.get_normalized_entries(line_list)


                if "" in current_entry_dict.values():
                    errors.append(line_number)
                else:
                    entries.append(current_entry_dict)

                line_number += 1

            f.close()

            entries = self.sort_entries(entries)
            json_dict = {"entries" : entries, "errors" : errors}

            output_file_path = self._generate_output_file_path()
            output_file_obj = open(output_file_path, 'w+')
            output_file_obj.write(self.form_json(json_dict))
            output_file_obj.close()

            return "output json file: " + output_file_path

        except IOError:
            return "Error: cannot find file for reading or writing data"

        except EOFError:
            return "Error: EOF reached"


    def form_json(self, json_dict):
        """
        Form json string
        Return: str
        """
        return json.dumps(json_dict,
                          sort_keys=True,
                          indent=2)

    def sort_entries(self, entries):
        """
        sort the entries dictionary as per sort group
        currently sorting is done on group lastname, firstname
        Return:
            dictionary
        """
        for sort_group_member in reversed(SORT_GROUP):
            entries = sorted(entries, key=lambda k: k[sort_group_member])
        return entries

    def format_line_list(self, line_list):
        if not line_list:
            return line_list

        for i in range(0, len(line_list)):
            line_list[i] = line_list[i].strip()

        return line_list

    def _generate_output_file_path(self):
        filedir = os.path.dirname(os.path.realpath('__file__'))
        output_file = "output_" + str(datetime.datetime.now().isoformat()) + ".json"
        output_file_path = os.path.join(filedir, 'output/' + output_file)

        return output_file_path


    def get_normalized_entries(self, line_list):
        """
        Normalizes each entry in list
        Returns: dictionary of normalized items
                 with keys as "color", "firstname", "lastname",
                 "phonenumber", "zipcode"
                 If any entry is invalid, the value for that
                 entry is an empty string ""
        """

        if len(line_list) not in VALID_RECORD_LENGTH:
            return {"color" : "",
                    "firstname" : "",
                    "lastname" : "",
                    "phonenumber" : "",
                    "zipcode" : ""}

        # conditions for different formats
        if len(line_list) == 4:
            return self._normalize_format_1(line_list)

        elif len(line_list) == 5 and line_list[-1] in VALID_COLORS:
            return self._normalize_format_2(line_list)

        # add conditions here if more formats are added in future

        else:
            return self._normalize_format_3(line_list)




    def _normalize_format_1(self, line_list):
        """
        normalize the format:
        ['James Murphy', 'yellow', '83880', '018 154 6474']
        Returns: dictionary with keys as "color", "firstname", "lastname",
                 "phonenumber", "zipcode"
                 If any entry is invalid, the value for that
                 entry is an empty string
        """
        entry_dictionary = {}
        entry_dictionary["color"] = self._normalize_color(line_list[1])
        entry_dictionary["zipcode"] = self._normalize_zipcode(line_list[2])
        entry_dictionary["phonenumber"] = self._normalize_phonenumber(line_list[3])

        name = line_list[0].split(' ')

        if len(name) < 2:
            entry_dictionary["firstname"] = "" # invalid entry
            entry_dictionary["lastname"]  = "" # invalid entry
        else:
            entry_dictionary["lastname"] = self._normalize_lastname(name[-1]) # last item
            entry_dictionary["firstname"]  = self._normalize_firstname(' '.join(name[:len(name) - 1]))

        return entry_dictionary

    def _normalize_format_2(self, line_list):
        """
        normalize the format:
        ['Booker T.', 'Washington', '87360', '373 781 7380', 'yellow']
        Returns: dictionary with keys as "color", "firstname", "lastname",
                 "phonenumber", "zipcode"
                 If any entry is invalid, the value for that
                 entry is an empty string
        """
        entry_dictionary = {}

        entry_dictionary["color"] = self._normalize_color(line_list[4])
        entry_dictionary["zipcode"] = self._normalize_zipcode(line_list[2])
        entry_dictionary["phonenumber"] = self._normalize_phonenumber(line_list[3])
        entry_dictionary["lastname"] = self._normalize_lastname(line_list[1])
        entry_dictionary["firstname"]  = self._normalize_firstname(line_list[0])

        return entry_dictionary


    def _normalize_format_3(self, line_list):
        """
        normalize the format:
        ['Chandler', 'Kerri', '(623)-668-9293', 'pink', '12313']
        Returns: dictionary with keys as "color", "firstname", "lastname",
                 "phonenumber", "zipcode"
                 If any entry is invalid, the value for that
                 entry is an empty string ""
        """

        entry_dictionary = {}

        entry_dictionary["color"] = self._normalize_color(line_list[3])
        entry_dictionary["zipcode"] = self._normalize_zipcode(line_list[4])
        entry_dictionary["phonenumber"] = self._normalize_phonenumber(line_list[2])
        entry_dictionary["lastname"] = self._normalize_lastname(line_list[0])
        entry_dictionary["firstname"]  = self._normalize_firstname(line_list[1])

        return entry_dictionary


    def _normalize_color(self, color):
        if color.lower() in VALID_COLORS:
            return color.lower()
        return ""


    def _normalize_zipcode(self, zipcode):
        if len(zipcode) not in VALID_ZIPCODE_LENGTH:
            return ""

        for num in zipcode:
            if not num.isdigit():
                return ""

        return zipcode


    def _normalize_phonenumber(self, phonenumber):
        for invalid_char in INVALID_CHARS_IN_PHONENUMBER:
            phonenumber = phonenumber.replace(invalid_char, '')

        if len(phonenumber) not in VALID_PHONENUMBER_LENGTHS:
            return ""

        for num in phonenumber:
            if not num.isdigit():
                return ""

        normalized_phonenumber = ""
        for i in range(0, len(phonenumber)):
            if i == 2 or i == 5:
                normalized_phonenumber += phonenumber[i]
                normalized_phonenumber += "-"
            else:
                normalized_phonenumber += phonenumber[i]

        return normalized_phonenumber


    def _normalize_lastname(self, lastname):
        if not lastname:
            return ""

        if lastname.isalpha():
            return lastname.capitalize()
        else:
            return ""

    def _normalize_firstname(self, firstname):
        firstname_lst = firstname.split(" ")

        if len(firstname_lst) == 1:
            if firstname_lst[0].isalpha():
                return firstname_lst[0].capitalize()
            else:
                return ""

        else:
            # handle the case for "Booker T."
            normalized_firstname = ""
            for name_part in firstname_lst:
                if name_part.isalpha() or '.' in name_part or '' in name_part:
                    normalized_firstname += name_part.capitalize() + ' '
                else:
                    return ""

        return normalized_firstname.strip()














