
# Replace with your file path below
fileName = "C:/Users/woods/PycharmProjects/my_avc2024/Puzzles/6.txt"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

print(len(lines))
print(len(lines[0]))

# directions 0:up 1:right 2:down 3:left
directions = ['^', ">", "v", "<"]
x, y, direction = 0, 0, 0

grid = [[0 for _ in range(len(lines))] for _ in range(len(lines[0]))]

for line_num, line in enumerate(lines):
    for item_num, item in enumerate(line):
        grid[line_num][item_num] = item
        if directions.__contains__(item):
            direction = directions.index(item)
            x, y = item_num, line_num

has_exited = False

print(x, y, direction)

final_sum = 0

while not has_exited:

    if direction == 0:
        if y > 0 and grid[y - 1][x] != "#":
            y -= 1
            if grid[y][x] == ".":
                final_sum += 1
                grid[y][x] = "*"
        elif y > 0 and grid[y - 1][x] == "#":
            direction = 1
        else:
            has_exited = True

    if direction == 1:
        if x < len(lines[0]) - 1 and grid[y][x + 1] != "#":
            x += 1
            if grid[y][x] == ".":
                final_sum += 1
                grid[y][x] = "*"
        elif x < len(lines[0]) - 1 and grid[y][x + 1] == "#":
            direction = 2
        else:
            has_exited = True

    if direction == 2:
        if y < len(lines) - 1 and grid[y + 1][x] != "#":
            y += 1
            if grid[y][x] == ".":
                final_sum += 1
                grid[y][x] = "*"
        elif y < len(lines) - 1 and grid[y + 1][x] == "#":
            direction = 3
        else:
            has_exited = True

    if direction == 3:
        if x > 0 and grid[y][x - 1]!= "#":
            x -= 1
            if grid[y][x] == ".":
                final_sum += 1
                grid[y][x] = "*"
        elif x > 0 and grid[y][x - 1] == "#":
            direction = 0
        else:
            has_exited = True

print(final_sum + 1)


