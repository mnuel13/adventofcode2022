import string


with open('inputs/3.txt') as input:
    bags = input.read()

list_bags = bags.split("\n")

side_a = []
side_b = []
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
values = {}

counter = 1
for x in lower_case:
    values[x] = counter
    counter += 1
for x in upper_case:
    values[x] = counter
    counter += 1

for x in list_bags:
    side_a.append(x[:int((len(x)/2))])
    side_b.append(x[int((len(x)/2)):])

counter = 0
result = 0

for items in side_a:
    for letter in items:
        if letter in side_b[counter]:
            result += values[letter]
            break
    counter += 1


list_three_sacks = []

for i in range(0, len(list_bags), 3):
    list_three_sacks.append(list_bags[i:i+3])

second_result = 0

for sack in range(len(list_three_sacks)):
    for letter in list_three_sacks[sack][0]:
        if letter in list_three_sacks[sack][1] and letter in list_three_sacks[sack][2]:
            second_result += values[letter]
            break

print(f"First result: {result}")
print(f"Second result: {second_result}")
