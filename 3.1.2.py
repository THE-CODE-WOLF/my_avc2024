import re

fileName = "C:/Users/woods/PycharmProjects/AdventOfCode2024/3.1.2.txt"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]
    print(lines)

final_sum = 0

for thing in lines:
    nums_to_multiply = re.findall(r'\d+', thing)
    final_sum += int(nums_to_multiply[0]) * int(nums_to_multiply[1])
    print(re.findall(r'\d+', thing))
    print(int(nums_to_multiply[0]))
    #print(nums_to_multiply)
    #print(int(nums_to_multiply[0]) * int(nums_to_multiply[1]))

print(final_sum)