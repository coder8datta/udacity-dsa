"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone_number_dict = dict()

for i in range(len(calls)) :
    phone_number_dict[calls[i][0]] = phone_number_dict.get(calls[i][0],0) + int(calls[i][3])
    phone_number_dict[calls[i][1]] = phone_number_dict.get(calls[i][1],0) + int(calls[i][3])

max_phone_number = max(phone_number_dict, key= lambda x:phone_number_dict.get(x))
max_duration = phone_number_dict.get(max_phone_number)
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(
    max_phone_number, max_duration))
