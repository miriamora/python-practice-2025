"""import time

count = 0
number = 1

for i in ['obi', 'ada', 'emeka']:

    while count < 5:
        print(f"hello {i}, {number}")
        time.sleep(1)
        count = count + 1
        number = number + 1"""

import time

names = ['obi', 'ada', 'emeka']

for name in names:
    number = 1  # Reset number for each name
    while number <= 5:
        print(f"Hello {name}, {number}")
        time.sleep(1)
        number += 1
