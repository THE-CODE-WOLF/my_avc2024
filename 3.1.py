
import re

#Replace with your file path below
fileName = "C:/Users/woods/PycharmProjects/AdventOfCode2024/3.txt"

with open(fileName, encoding="utf-8") as file:
    text = file.readlines()
    #text = []
    #for line in file:
    #    text.append(str(line))
    #print(text)

things_to_multiply = re.findall("mul\(\d+,\d+\)", str(text))

print(things_to_multiply)
print(len(things_to_multiply))

final_sum = 0

for thing in things_to_multiply:
    nums_to_multiply = re.findall(r'\d+', thing)
    final_sum += (int(nums_to_multiply[0]) * int(nums_to_multiply[1]))
    print(nums_to_multiply)
    print(int(nums_to_multiply[0]) * int(nums_to_multiply[1]))

print(final_sum)