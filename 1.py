with open('inputs/1.txt') as file:
    calories = file.read()

cal_list = calories.split('\n')
cal_list_int = []

for x in cal_list:
    try:
        cal_list_int.append(int(x))
    except ValueError:
        cal_list_int.append('')

indexes = []
list_of_lists = []

for x in range(len(cal_list_int)):
    if cal_list_int[x] == "":
        indexes.append(x)

list_of_lists.append(cal_list_int[:indexes[0]])

for x in range(len(indexes)):
    try:
        list_of_lists.append(cal_list_int[indexes[x]+1:indexes[x+1]])
    except IndexError:
        list_of_lists.append(cal_list_int[indexes[x]+1:])

sums = []

for x in list_of_lists:
    sums.append(sum(x))

print(f"First result: {max(sums)}")

print(f"Second result: {sum(sorted(sums)[-3:])}")
