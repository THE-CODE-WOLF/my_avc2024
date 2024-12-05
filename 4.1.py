
import re

#Replace with your file path below
fileName = "C:/Users/woods/PycharmProjects/my_avc2024/Puzzles/4.txt"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

test_lines = [
        "XMASA",
        "MSMMM",
        "AAAAA",
        "SSSMM"
    ]

#print(lines)
grid = []
length = len(lines)
#print(length)

#for line in lines:
#    #print(line)
#    for y in range(0, length):
#        #print(line[y])
#        grid.append(line[y])

#print(grid)
#print(len(grid))

final_sum = 0

for line_num, line in enumerate(lines):
    #print(line)
    for num, item in enumerate(line):
        grid.append(item)
        #print(line[num:num + 4])
        #print(line[num:num + 4] == 'XMAS')
        if line[num:num + 4] == 'XMAS':
            final_sum += 1
            ##for i in range(4):
            #grid[num] = '+'

        elif line[num:num + 4] == 'SAMX':
            final_sum += 1

        elif item == 'X' and line_num < length - 3 and lines[line_num + 1][num] == 'M' and lines[line_num + 2][num] == \
                'A' and lines[line_num + 3][num] == 'S':
            final_sum += 1

        elif item == 'S' and line_num < length - 3 and lines[line_num + 1][num] == 'A' and lines[line_num + 2][num] == \
                'M' and lines[line_num + 3][num] == 'X':
            final_sum += 1

        elif item == 'X' and line_num < length - 3 and num < len(line) - 4 and lines[line_num + 1][num + 1] == 'M' and \
                lines[line_num + 2][num + 2] == 'A' and lines[line_num + 3][num + 3] == 'S':
            final_sum += 1

        elif item == 'S' and line_num < length - 3 and num < len(line) - 4 and lines[line_num + 1][num + 1] == 'A' and \
                lines[line_num + 2][num + 2] == 'M' and lines[line_num + 3][num + 3] == 'X':
            final_sum += 1

        elif item == 'X' and line_num < length - 3 and num < len(line) - 4 and lines[line_num + 1][num + 1] == 'M' and \
                lines[line_num + 2][num + 2] == 'A' and lines[line_num + 3][num + 3] == 'S':
            final_sum += 1

        elif item == 'S' and line_num < length - 3 and num < len(line) - 4 and lines[line_num + 1][num + 1] == 'A' and \
                lines[line_num + 2][num + 2] == 'M' and lines[line_num + 3][num + 3] == 'X':
            final_sum += 1

#        if item == 'X' and num < len(line) - 4:
#            if line[num + 1] == 'M':
#                if line[num + 2] == 'A':
#                    if line[num + 3] == 'S':
#                        final_sum += 1
#                        #for i in range(4):
#                        #    final_sum += 1
#                        #    grid[num] = '+'
#                        #    #grid.append('+')
#
#
#        elif item == 'X' and num > 4:
#            if line[num - 1] == 'M':
#                if line[num - 2] == 'A':
#                    if line[num - 3] == 'S':
#                        final_sum += 1
#                        #for i in range(4):
#                        #    final_sum += 1
#                        #    grid[num - i] = '-'
#                        #    #grid.append('-')








#for id, item in enumerate(grid):
#    #print(grid[y * length:(y + 1) * length][x])
#    #print(item)
#    if item == 'X' and not id == 140 * (id + 1):
#        if grid[id + 1] == 'M' :
#            if grid[id + 2] == 'A':
#                if grid[id + 3] == 'S':
#                    #print(grid[id:id + 4])
#                    #print(id)
#                    final_sum += 1
#                    for i in range(4):
#                        grid[id + i] = '+'
#
#        if item == 'X' and not id == 140 + id:
#            if grid[id - 1] == 'M':
#                if grid[id - 2] == 'A':
#                    if grid[id - 3] == 'S':
#                        #print(grid[id:id - 4])
#                        #print(id)
#                        final_sum += 1
#                        for i in range(4):
#                            grid[id - i] = '-'
#
#
#        #print(grid[y * length:(y + 1) * length][x])
#
#for line in range(0, length):
#    print(grid[line * length:(line + 1) * length])
print(len(grid))
#print(grid)
print(final_sum)


