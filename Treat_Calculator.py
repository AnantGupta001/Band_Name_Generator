# DAY 4

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
n = len(names)
i = random.randint(0, n - 1)
print(names[i], "is going to buy the meal today!")
