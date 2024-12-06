
#Replace with your file path below
fileName = "C:/Users/woods/PycharmProjects/my_avc2024/Puzzles/4.txt"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

grid = []
length = len(lines)

final_sum = 0

for line_num, line in enumerate(lines):
    for num, item in enumerate(line):

        # Horizontal
        if line[num:num + 4] == 'XMAS':
            final_sum += 1

        # Horizontal backwards
        if line[num:num + 4] == 'SAMX':
            final_sum += 1

        # Vertical
        if item == 'X' and line_num < length - 3 and lines[line_num + 1][num] == 'M' and lines[line_num + 2][
                    num] == 'A' and lines[line_num + 3][num] == 'S':
            final_sum += 1

        # Vertical backwards
        if item == 'S' and line_num < length - 3 and lines[line_num + 1][num] == 'A' and lines[line_num + 2][
                    num] == 'M' and lines[line_num + 3][num] == 'X':
            final_sum += 1

        # Diagonal
        if item == 'X' and line_num < length - 3 and num < len(line) - 3 and lines[line_num + 1][num + 1] == 'M' and \
                lines[line_num + 2][num + 2] == 'A' and lines[line_num + 3][num + 3] == 'S':
            final_sum += 1

        # Diagonal backwards
        if item == 'S' and line_num < length - 3 and num < len(line) - 3 and lines[line_num + 1][num + 1] == 'A' and \
                lines[line_num + 2][num + 2] == 'M' and lines[line_num + 3][num + 3] == 'X':
            final_sum += 1

        # Anti-diagonal
        if item == 'X' and line_num < length - 3 and num >= 3 and lines[line_num + 1][num - 1] == 'M' and \
                lines[line_num + 2][num - 2] == 'A' and lines[line_num + 3][num - 3] == 'S':
            final_sum += 1

        # Anti-diagonal backwards
        elif item == 'S' and line_num < length - 3 and num >= 3 and lines[line_num + 1][num - 1] == 'A' and \
                lines[line_num + 2][num - 2] == 'M' and lines[line_num + 3][num - 3] == 'X':
            final_sum += 1

print(final_sum)
