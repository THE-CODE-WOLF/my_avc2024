
#Replace with your file path below
fileName = "C:/Users/woods/PycharmProjects/my_avc2024/Puzzles/4.txt"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

test_lines = [
    "M.M.",
    ".A..",
    "S.S.",
    ".A..",
    "M.M.",
    "M.S.",
    ".A..",
    "M.S.",
    "S.M.",
    ".A..",
    "S.M."
]

grid = []
#length = len(lines)
length = len(lines)

final_sum = 0

for line_num, line in enumerate(lines):
    for num, item in enumerate(line):

        if line_num > 0 and line_num < length - 1 and num > 0 and num < len(line) - 1 and item == 'A':
            # print(item)

            if lines[line_num - 1][num - 1] == 'M' and lines[line_num + 1][num + 1] == 'S' and lines[line_num - 1][num + 1] == 'M' and lines[line_num + 1][num - 1] == 'S':
                final_sum += 1

            if lines[line_num - 1][num - 1] == 'S' and lines[line_num + 1][num + 1] == 'M' and lines[line_num - 1][num + 1] == 'S' and lines[line_num + 1][num - 1] == 'M':
                final_sum += 1

            if lines[line_num - 1][num - 1] == 'M' and lines[line_num + 1][num + 1] == 'S' and lines[line_num - 1][num + 1] == 'S' and lines[line_num + 1][num - 1] == 'M':
                final_sum += 1

            if lines[line_num - 1][num - 1] == 'S' and lines[line_num + 1][num + 1] == 'M' and lines[line_num - 1][num + 1] == 'M' and lines[line_num + 1][num - 1] == 'S':
                final_sum += 1


print(final_sum)