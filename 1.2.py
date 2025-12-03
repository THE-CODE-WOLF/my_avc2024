
#Replace with your file path below
fileName = "PycharmProjects/AdventOfCode2024/1.1.txt"

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

#print(left_list)
#print(right_list)
final_sum = 0

for num in left_list:
    same = []
    l_num = num
    for r_num in right_list:
        if int(r_num) == int(l_num):
            same.append(l_num)
    if same:
        #print(num)
        #print(len(same))
        final_sum += int(num) * len(same)
        #print(final_sum)
        #print(same)

print(final_sum)
