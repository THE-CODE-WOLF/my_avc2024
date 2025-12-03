import re

#Replace with your file path below
fileName = "PycharmProjects/AdventOfCode2024/2.txt"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]
    print(lines)

test_lines = ['1 2 4 7', '7, 4, 2, 1', '1, 4, 2, 3', '7, 2, 3, 10', '1, 2, 6, 7', '1, 2, 2, 5']

final_sum = 0

for the_line in lines:

    string_nums = re.findall(r'\d+', the_line)
    nums = []

    for num in string_nums:
        nums.append(int(num))

    print(string_nums)
    print(nums)

    if nums == sorted(nums):
        differences = []
        i = 0
        for num in nums:
            if i < len(nums) - 1:
                i += 1
                differences.append(int(nums[i]) - int(num))

        good = True
        for num in differences:
            if num > 3 or num == 0:
                good = False

        if good:
            final_sum += 1
            print(differences)

    elif nums == sorted(nums, reverse=True):
        differences = []
        i = 0
        for num in nums:
            if i < len(nums) - 1:
                i += 1
                differences.append(int(num) - int(nums[i]))

        good = True
        for num in differences:
            if num > 3 or num == 0:
                good = False

        if good:
            final_sum += 1
            print(differences)

print(final_sum)
