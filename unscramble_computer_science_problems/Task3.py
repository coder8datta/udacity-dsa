"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
phone_number_dict = {}
total = 0

def getMapFromColumns(list_of_numbers):
    total = 0
    for numbers in list_of_numbers:
        if numbers[0].find('(080)') != -1:
            format_number = formatNumber(numbers[1])
            phone_number_dict[format_number] = phone_number_dict.get(format_number,0) + 1
            total += 1
    return total


def formatNumber(called_number):
    if called_number.find('(') != -1:
        return called_number[1:called_number.find(')')]
    elif called_number[:3] == '140':
        return '140'
    elif int(called_number[:1]) >= 7 and int(called_number[:1]) <= 9:
        return called_number[:4]


total = getMapFromColumns(calls)
print('The numbers called by people in Bangalore have codes:')
for keys in sorted(phone_number_dict.keys()):
    print(keys)
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(round(phone_number_dict['080']/total * 100,2)))