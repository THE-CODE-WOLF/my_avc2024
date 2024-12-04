
fileName = "C:/Users/woods/PycharmProjects/AdventOfCode2024/1.1.txt"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]
    #print(lines)

left_list = []
right_list = []

for line in lines:
    left_list.append(line[0:5])
    right_list.append(line[8:14])

left_list = sorted(left_list)
right_list = sorted(right_list)

i = 0
final_sum = 0

for num in left_list:
    final_sum += abs(int(num) - int(right_list[i]))
    i += 1

print(final_sum)
