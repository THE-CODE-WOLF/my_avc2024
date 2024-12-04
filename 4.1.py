fileName = "C:/Users/woods/PycharmProjects/my_avc2024/Puzzles/1.1.txt"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]
