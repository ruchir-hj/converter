
# valid colors
VALID_COLORS = set(['blue',
                    'green',
                    'red',
                    'yellow',
                    'aqua marine',
                    'violet',
                    'orange',
                    'black',
                    'brown',
                    'white',
                    'pink',
                    'gray'])


# valid length zip code length
# Add other zip code lengths in this list
# if International zipcodes of different lengths
# are to be considered in future.
VALID_ZIPCODE_LENGTH = [5  ]

# Invalid chars in a phone number
# Add other invalid chars in this list
# if more invalid chars are found in future
INVALID_CHARS_IN_PHONENUMBER = ['(', ')', '-', ' ']

# valid number of digits in a phonenumber
VALID_PHONENUMBER_LENGTHS = [10 ]

# keys on which sorting should happen
SORT_GROUP = ["lastname", "firstname"]

# valid size of a record
VALID_RECORD_LENGTH = [4,5 ]