
import re

fileName = "C:/Users/woods/PycharmProjects/AdventOfCode2024/3.txt"

with open(fileName, encoding="utf-8") as file:
    text = file.readlines()
    #text = []
    #for line in file:
    #    text.append(str(line))
    #print(text)

test_text = ["mul(10,10)mul(10,10)don't()mul(10,10)mul(10,10)do()mul(10,10)mul(10,10)don't()mul(10,10)mul(10,10)do()mul(10,10)mul(10,10)"]

final_sum = 0

do_split = re.split("do\(\)", str(text))

for index, split in enumerate(do_split):
    #print(index)
    #print(do_split[index])
    dont_split = re.split("don't\(\)", str(do_split[index]))
    #print(re.findall("don't\(\)", str(do_split[index])))
    #print(dont_split[0])
    things_to_multiply = re.findall("mul\(\d+,\d+\)", str(dont_split[0]))
    #print(things_to_multiply)
    #print(len(things_to_multiply))
    for thing in things_to_multiply:
        nums_to_multiply = re.findall(r'\d+', thing)
        final_sum += (int(nums_to_multiply[0]) * int(nums_to_multiply[1]))
        print(nums_to_multiply)
        print(int(nums_to_multiply[0]) * int(nums_to_multiply[1]))
#
#dont_split = re.split("don't\(\)", str(do_split))
#
#things_to_multiply = re.findall("mul\(\d+,\d+\)", str(text))
#
#print(things_to_multiply)
#print(len(things_to_multiply))
#
#final_sum = 0
#
#for thing in things_to_multiply:
#    nums_to_multiply = re.findall(r'\d+', thing)
#    final_sum += (int(nums_to_multiply[0]) * int(nums_to_multiply[1]))
#    print(nums_to_multiply)
#    print(int(nums_to_multiply[0]) * int(nums_to_multiply[1]))
#
print(final_sum)