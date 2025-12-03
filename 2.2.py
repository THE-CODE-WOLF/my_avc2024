
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

    modded_nums = nums

    count = 0

    is_safe = False
    done = False

    while not done:

        print(modded_nums)

        if modded_nums == sorted(modded_nums):
            differences = []
            i = 0
            for num in modded_nums:
                if i < len(modded_nums) - 1:
                    i += 1
                    differences.append(int(modded_nums[i]) - int(num))

            good = True
            for num in differences:
                if num > 3 or num == 0:
                    good = False

            if good:
                #final_sum += 1
                is_safe = True
                print(differences)

        elif modded_nums == sorted(modded_nums, reverse=True):
            differences = []
            i = 0
            for num in modded_nums:
                if i < len(modded_nums) - 1:
                    i += 1
                    differences.append(int(num) - int(modded_nums[i]))

            good = True
            for num in differences:
                if num > 3 or num == 0:
                    good = False

            if good:
                #final_sum += 1
                is_safe = True
                print(differences)

        if count >= len(nums) + 1 or is_safe:
            done = True
        else:
            nums = []
            for num in string_nums:
                nums.append(int(num))
            modded_nums = nums
            del modded_nums[count]
            count += 1



    if is_safe:
        final_sum += 1


print(final_sum)
