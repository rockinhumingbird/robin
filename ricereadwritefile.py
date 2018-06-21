"""
Dictionary creation.
"""

print("Dictionary Literals")
print("===================")

# Dictionary literals
empty = {}
print(empty)

simple = {1: 2}
print(simple)

squares = {1: 1, 2: 4, 3: 9, 4: 16}
print(squares)

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'} 
print(cipher)

zoe = {'zoe': True, 'eht': False}
print(zoe)

cities = {'China': ['Shanghai', 'Beijing'],
          'USA': ['New York', 'Los Angeles'],
          'Spain': ['Madrid', 'Barcelona'],
          'Australia': ['Sydney', 'Melbourne'],
          'Texas': ['Houston', 'San Antonio']}
print(cities)

print("")
print("Creating Dictionaries")
print("=====================")

empty2 = dict()
print(empty2)

data = [(1, 'one'), (2, 'two'), (3, 'three')]
names = dict(data)
print(names)

cipher2 = dict(cipher)
print(cipher2)


"""
Dictionary lookup and update.
"""


print("Dictionary Lookup")
print("=================")

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'} 
print(cipher)

# Use indexing with keys to access values
print(cipher['t'])
print(cipher['n'])

def encrypt(cipher, word):
    """encrypt word using cipher"""
    encrypted = ""
    for char in word:
        encrypted += cipher[char]
    return encrypted

python = "python"
enc = encrypt(cipher, python)
print(python, enc)

# It is an error to use a non-existent key
# print(cipher[1])

# Use .get when you are unsure if the key exists
print(cipher.get('t'))
print(cipher.get(1))
print(cipher.get(1, 'z'))

print("")
print("Dictionary Update")
print("=================")

print(cipher)

# Modify an existing key->value mapping
cipher['p'] = 'q'
print(cipher)

# Create a new key->value mapping
cipher['r'] = 'z'
print(cipher)

enc2 = encrypt(cipher, python)
print(python, enc, enc2)
"""
Checking for keys in a dictionary.
"""

print("Using 'in'")
print("==========")

mapping = {1: 5, 8: -3, 7: 22, 4: 13, 22: 17}

# Keys
print(1 in mapping)
print(8 in mapping)

# Values
print(5 in mapping)
print(-3 in mapping)

# Both
print(22 in mapping)

# Neither
print(82 in mapping)

print("")

print("Protecting from Errors")
print("======================")

keys = [8, 14, 22, 25]

#for key in keys:
#    print(key, mapping[key])

for key in keys:
    if key in mapping:
        print(key, mapping[key])
    else:
        print("{} not in mapping".format(key))


print("Issues with Keys")
print("================")
        
# Be careful with what you use as keys!
# If all keys are of the same type, you won't run
#  into these issues
mapping = {4.0: 2, 'a': 3, True: 'true', False: 9}
print(mapping)

mapping[1] = 7
print(mapping)

mapping[0] = 'false'
print(mapping)

mapping[4] = 7
print(mapping)

mapping['A'] = 'abc'
print(mapping)


"""
Checking for keys in a dictionary.
"""

print("Using 'in'")
print("==========")

mapping = {1: 5, 8: -3, 7: 22, 4: 13, 22: 17}

# Keys
print(1 in mapping)
print(8 in mapping)

# Values
print(5 in mapping)
print(-3 in mapping)

# Both
print(22 in mapping)

# Neither
print(82 in mapping)

print("")

print("Protecting from Errors")
print("======================")

keys = [8, 14, 22, 25]

#for key in keys:
#    print(key, mapping[key])

for key in keys:
    if key in mapping:
        print(key, mapping[key])
    else:
        print("{} not in mapping".format(key))


print("Issues with Keys")
print("================")
        
# Be careful with what you use as keys!
# If all keys are of the same type, you won't run
#  into these issues
mapping = {4.0: 2, 'a': 3, True: 'true', False: 9}
print(mapping)

mapping[1] = 7
print(mapping)

mapping[0] = 'false'
print(mapping)

mapping[4] = 7
print(mapping)

mapping['A'] = 'abc'
print(mapping)


"""
Example code for working with dictionary keys
"""

# Three example of dictionaries - note that dictionary keys in Python must be immutable
simple_dict = {"zoe" : 1, "scarlett" : 2, "nolan" : 3}
print(simple_dict)

bad_dict = {["Zoe", "chuh"] : 1, ["scarlett", "Johnasoon"] : 2, ["nolan", "ui"] : 3}
print(bad_dict)

good_dict = {("Zoe", "chuh") : 1, ("scarlett", "Johnasoon") : 2, ("nolan", "ui") : 3}
print(good_dict)


# Examples of dictionary lookup
#print(simple_dict["Zoe"])
#print(good_dict[("Zoe", "chuh")])

# Custom code for looking up keys that may not always be present

def lookup(my_dict, my_key, default_value=None):
    """
    Given dictionary my_dict and key my_key, 
    return my_dict[my_key] if my_key is in my_dict
    otherwise return default_value
    """
    if my_key in my_dict:
        return my_dict[my_key]
    else:
        return default_value

isimple_dict = {"Zoe" : 1, "Bob" : 2, "John" : 3}
print(lookup(isimple_dict, "Zoe", -1))
print(lookup(isimple_dict, "Bob", -1))
print(lookup(isimple_dict, "Stephen"))

#print(isimple_dict.get("Zoe", -1))
#print(isimple_dict.get("Bob", -1))
#print(isimple_dict.get("John"))		# default value if parameter is omitted is None

# Note that we can acheive the same effect in lookup() 
# via default parameter definition of the form "default_value = None"

def count_letters(word_list):
    """ See question description 
    return the most frequent letter in wordlist
    
    """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for item in word_list:
        for letter in item:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(" ")
count_letters(monty_words)

"""
Iterating over dictionaries.
"""

# Mapping from various cities to their country
capitals = {'USA': 'Washington, D.C.',
            'China': 'Beijing',
            'France': 'Paris',
            'England': 'London',
            'Italy': 'Rome',
            'Russia': 'Moscow',
            'Australia': 'Canberra',
            'Peru': 'Lima',
            'Japan': 'Tokyo'}

print("Direct Iteration")
print("================")

for country in capitals:
    print("{}, {}".format(capitals[country], country))

print("")

print("Iteration over Keys")
print("===================")

for country in capitals.keys():
    print("{}, {}".format(capitals[country], country))

print("")

print("Iteration over Values")
print("=====================")

for city in capitals.values():
    print("Capital city: {}".format(city))

print("")

print("Iteration over Items")
print("===================")

for country, city in capitals.items():
    print("{}, {}".format(city, country))

print("")

print("Checking Membership")
print("===================")

print('England' in capitals)
print('Lima' in capitals)

print('Moscow' in capitals.keys())
print('Italy' in capitals.keys())

print('Houston' in capitals.values())
print('Beijing' in capitals.values())


"""
Tabular data as a nested list.
"""

# Programming language popularity, from www.tiobe.com/tiobe-index
popularity = [["Language", 2017, 2012, 2007, 2002, 1997, 1992, 1987],
              ["Java", 1, 2, 1, 1, 15, 0, 0],
              ["C", 2, 1, 2, 2, 1, 1, 1],
              ["C++", 3, 3, 3, 3, 2, 2, 5],
              ["C#", 4, 4, 7, 13, 0, 0, 0],
              ["Python", 5, 7, 6, 11, 27, 0, 0],
              ["Visual Basic .NET", 6, 17, 0, 0, 0, 0, 0],
              ["PHP", 7, 6, 4, 5, 0, 0, 0],
              ["JavaScript", 8, 9, 8, 7, 23, 0, 0],
              ["Perl", 9, 8, 5, 4, 4, 10, 0]]

format_string = "{:<20}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}"

# Display langauges table
headers = popularity[0]
#take each 8 individual argument then can pass to format method for format string
header_row = format_string.format(*headers)
print(header_row)
print("-" * len(header_row))
#iterate over the first row
for language in popularity[1:]:
    print(format_string.format(*language))

print("")
    
# Finding/selecting items

# What was Python's popularity in 1997?
print("Python's popularity in 1997:", popularity[5][5])

def find_col(table, col):
    """
    Return column index with col header in table
    or -1 if col is not in table
    """
    return table[0].index(col)

def find_row(table, row):
    """
    Return row index with row header in table
    or -1 if row is not in table
    """
    for idx in range(len(table)):
        if table[idx][0] == row:
            return idx
    return -1
    
idx1997 = find_col(popularity, 1997)
idxpython = find_row(popularity, "Python")
print("Python's popularity in 1997:", popularity[idxpython][idx1997])



"""
Tabular data as nested dictionaries.
"""

# Top 10 software products with the most vulnerabilities in 2017
# (through August).  From www.cvedetails.com.
vulnerabilities2017 = {
    'Android': {'vendor': 'Google',
                'type': 'Operating System',
                'number': 564},
    'Linux Kernel': {'vendor': 'Linux',
                     'type': 'Operating System',
                     'number': 367},
    'Imagemagick': {'vendor': 'Imagemagick',
                    'type': 'Application',
                    'number': 307},
    'IPhone OS': {'vendor': 'Apple',
                  'type': 'Operating System',
                  'number': 290},
    'Mac OS X': {'vendor': 'Apple',
                 'type': 'Operating System',
                 'number': 210},
    'Windows 10': {'vendor': 'Microsoft',
                   'type': 'Operating System',
                   'number': 195},
    'Windows Server 2008': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 187},
    'Windows Server 2016': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 183},
    'Windows Server 2012': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 176},
    'Windows 7': {'vendor': 'Microsoft',
                  'type': 'Operating System',
                  'number': 174}
}

# Display vulnerabilities table
print("Product               Vendor        Type               Vulnerabilities")
print("----------------------------------------------------------------------")

for product, values in vulnerabilities2017.items():
    row = "{:21} {:13} {:18} {:8}".format(product, values['vendor'], values['type'], values['number'])
    print(row)

print("")

# Finding/selecting items

# How many vulnerabilites does Windows 7 have?
print(vulnerabilities2017['Windows 7']['number'])

# What product had the most vulnerabilities?
maxproduct = None
maxnumber = -1

for product, values in vulnerabilities2017.items():
    if values['number'] > maxnumber:
        maxproduct = product
        maxnumber = values['number']

print(maxproduct, maxnumber)


"""
Example code for printing the contents of a dictionary to the console
"""


NAME_DICT = {"Warren" : "Joe", "Rixner" : "Scott", "Greiner" : "John"}

def run_dict_methods():
    """
    Run some simple examples of calls to dictionary methods
    """
    
    # Note that these methods return an iterable object (similar to range())
    print(NAME_DICT.keys())
    print(NAME_DICT.values())
    print(NAME_DICT.items())
    print()
    
    # These objects can be converted to lists
    print(list(NAME_DICT.keys()))
    print(list(NAME_DICT.values()))
    print(list(NAME_DICT.items()))

run_dict_methods()


def print_dict_keys(my_dict):
    """
    Print the contents of a dictionary to the console
    in a readable form using the keys() method
    """
    print("Printing dictionary", my_dict, "in readable form")
    for key in my_dict:                                # note my_dict.keys() works here too
        print("Key =", key, "has value =", my_dict[key])
        
        
def print_dict_items(my_dict):
    """
    Print the contents of a dictionary to the console
    in a readable form using the items() method
    """
    print("Printing dictionary", my_dict, "in readable form")
    for (key, value) in my_dict.items():
        print("Key =", key, "has value =", value)


def run_print_dict_examples():
    """
    Run some examples of printing dictionaries to the console
    """
    print()
    print_dict_keys(NAME_DICT)
    print()
    print_dict_items(NAME_DICT)
    
#run_print_dict_examples()


"""
Example code for printing the contents of a dictionary to the console
"""


NAME_DICT = {"Warren" : "Joe", "Rixner" : "Scott", "Greiner" : "John"}

def run_dict_methods():
    """
    Run some simple examples of calls to dictionary methods
    """
    
    # Note that these methods return an iterable object (similar to range())
    print(NAME_DICT.keys())
    print(NAME_DICT.values())
    print(NAME_DICT.items())
    print()
    
    # These objects can be converted to lists
    print(list(NAME_DICT.keys()))
    print(list(NAME_DICT.values()))
    print(list(NAME_DICT.items()))

run_dict_methods()


def print_dict_keys(my_dict):
    """
    Print the contents of a dictionary to the console
    in a readable form using the keys() method
    """
    print("Printing dictionary", my_dict, "in readable form")
    for key in my_dict:                                # note my_dict.keys() works here too
        print("Key =", key, "has value =", my_dict[key])
        
        
def print_dict_items(my_dict):
    """
    Print the contents of a dictionary to the console
    in a readable form using the items() method
    """
    print("Printing dictionary", my_dict, "in readable form")
    for (key, value) in my_dict.items():
        print("Key =", key, "has value =", value)


def run_print_dict_examples():
    """
    Run some examples of printing dictionaries to the console
    """
    print()
    print_dict_keys(NAME_DICT)
    print()
    print_dict_items(NAME_DICT)
    
#run_print_dict_examples()



NUM_ROWS = 5
NUM_COLS = 5

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(col*row)
    my_matrix.append(new_row)
 

######

NUM_ROWS = 5
NUM_COLS = 9

# construct a matrix
my_matrix = {}
for row in range(NUM_ROWS):
    row_dict = {}
    for col in range(NUM_COLS):
        row_dict[col] = row * col
    my_matrix[row] = row_dict
    
print(my_matrix)
 
# print the matrix
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(my_matrix[row][col], end = " ")
    print()


"""
Example code to read and parse a CSV file.
"""

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table


def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # Header column left justified
        print("{:<19}".format(row[0]), end='')
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')

table = parse("hightemp.csv")
print_table(table)

print("")
print("")

table2 = parse("hightemp2.csv")
print_table(table2)

"""
Using csv.DictReader.
"""

import csv

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sep', 'Oct', 'Nov', 'Dec')

def dictparse(csvfilename, keyfield):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True)
        for row in csvreader:
            table[row[keyfield]] = row
    return table


def print_table(table):
    """
    Print out table, which must be a dictionary
    of dictionaries, in a nicely formatted way.
    """
    print("City               ", end='')
    for month in MONTHS:
        print("{:>6}".format(month), end='')
    print("")
    for name, row in table.items():
        # Header column left justified
        print("{:<19}".format(name), end='')
        # Remaining columns right justified
        for month in MONTHS:
            print("{:>6}".format(row[month]), end='')
        print("", end='\n')

table = dictparse("hightemp.csv", 'City')
print_table(table)

"""
CSV reader options.
"""

import csv

def dictparse(csvfilename, keyfield, separator, quote, quotestrategy):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True,
                                   delimiter=separator,
                                   quotechar=quote,
                                   quoting=quotestrategy)
        for row in csvreader:
            table[row[keyfield]] = row
    return table, csvreader.fieldnames


def print_table(table, fieldnames):
    """
    Print out table, which must be a dictionary
    of dictionaries, in a nicely formatted way.
    """
    print("{:<19}".format(fieldnames[0]), end='')
    for field in fieldnames[1:]:
        print("{:>6}".format(field), end='')
    print("")
    for name, row in table.items():
        # Header column left justified
        print("{:<19}".format(name), end='')
        # Remaining columns right justified
        for field in fieldnames[1:]:
            print("{:>6}".format(row[field]), end='')
        print("", end='\n')

table, fieldnames = dictparse("hightemp.csv", 'City', ',', '"', csv.QUOTE_MINIMAL)
print(fieldnames)
print_table(table, fieldnames)

print("")
print("")

table2, fieldnames2 = dictparse("hightemp2.csv", 'City', ',', '"', csv.QUOTE_NONNUMERIC)
print_table(table2, fieldnames2)

print("")
print("")

table3, fieldnames3 = dictparse("hightemp3.csv", 'City', ',', '"', csv.QUOTE_NONNUMERIC)
print_table(table3, fieldnames3)

"""
Examples code for experimenting with options to the csv.read() and csv.write() methods
"""

import csv


# Function that prints 2D table to console

def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)


# Options for reading a CSV file

def read_csv_file(file_name, file_delimeter):
    """
    Given a CSV file path and a delimiter as strings,
    read the data into a 2D table and return the table
    """
       
    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=file_delimeter)
        for row in csv_reader:
            csv_table.append(row)
    return csv_table


def csv_delimiter_examples():
    """
    Run some example of reading CSV files using different delimiter options
    """
    number_table = read_csv_file("number_table.csv", " ")
    print_table(number_table)
    print()
    name_table = read_csv_file("name_table.csv", ",")
    print_table(name_table)



csv_delimiter_examples()




# Options for writing a CSV file

def write_csv_file(csv_table, file_name, file_delimiter, quoting_value):
    """
    Given a nested list csv_table, write the data into a
    CSV file with the name file_name
    """
    
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=file_delimiter, quoting=quoting_value)
        for row in csv_table:
            csv_writer.writerow(row)
            
def csv_quoting_examples():
    """
    Run some example of writing 2D tables as CSV files using various quoting options
    """
    name_table = read_csv_file("name_table.csv", ",")
    name_table.append([1, 2, 3])
    write_csv_file(name_table, "name_table_minimal.csv", ",", csv.QUOTE_MINIMAL)
    write_csv_file(name_table, "name_table_all.csv", ",", csv.QUOTE_ALL)
    write_csv_file(name_table, "name_table_nonnumeric.csv", ",", csv.QUOTE_NONNUMERIC)
    #write_csv_file(name_table, "name_table_none.csv", ",", csv.QUOTE_NONE)        # no escapechar is set for lots of quotes

    

#csv_quoting_examples()


"""
Examples code for experimenting with options to the csv.read() and csv.write() methods
"""

import csv


# Function that prints 2D table to console

def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)


# Options for reading a CSV file

def read_csv_file(file_name, file_delimeter):
    """
    Given a CSV file path and a delimiter as strings,
    read the data into a 2D table and return the table
    """
       
    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=file_delimeter)
        for row in csv_reader:
            csv_table.append(row)
    return csv_table


def csv_delimiter_examples():
    """
    Run some example of reading CSV files using different delimiter options
    """
    number_table = read_csv_file("number_table.csv", " ")
    print_table(number_table)
    print()
    name_table = read_csv_file("name_table.csv", ",")
    print_table(name_table)



csv_delimiter_examples()




# Options for writing a CSV file

def write_csv_file(csv_table, file_name, file_delimiter, quoting_value):
    """
    Given a nested list csv_table, write the data into a
    CSV file with the name file_name
    """
    
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=file_delimiter, quoting=quoting_value)
        for row in csv_table:
            csv_writer.writerow(row)
            
def csv_quoting_examples():
    """
    Run some example of writing 2D tables as CSV files using various quoting options
    """
    name_table = read_csv_file("name_table.csv", ",")
    name_table.append([1, 2, 3])
    write_csv_file(name_table, "name_table_minimal.csv", ",", csv.QUOTE_MINIMAL)
    write_csv_file(name_table, "name_table_all.csv", ",", csv.QUOTE_ALL)
    write_csv_file(name_table, "name_table_nonnumeric.csv", ",", csv.QUOTE_NONNUMERIC)
    #write_csv_file(name_table, "name_table_none.csv", ",", csv.QUOTE_NONE)        # no escapechar is set for lots of quotes

    

#csv_quoting_examples()