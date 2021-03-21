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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
primary_callers = set()
secondary_callers = set()

for i in range(len(calls)):
    primary_callers.add(calls[i][0])
    secondary_callers.add(calls[i][1])
for j in range(len(texts)):
    secondary_callers.add(texts[j][0])
    secondary_callers.add(texts[j][1])

primary_callers = primary_callers - secondary_callers
print('These numbers could be telemarketers:')
for key in sorted(primary_callers):
    print(key)
