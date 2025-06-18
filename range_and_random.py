import random

"""for i in range(1,10):
    print(i)

for r in range(1,20,3):
    print(r)"""

courses = ["aws", "trF", "python"]

c = random.choice(courses)
print(c)

random.shuffle(courses)

