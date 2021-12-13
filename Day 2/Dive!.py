"""
depth = 0
horizontal = 0

with open("inputs.txt") as inputs:
    directions = inputs.read()
    directions = directions.split("\n")

for elem in directions:
    if elem[0] == "f":
        horizontal += int(elem[-1])
    elif elem[0] == "d":
        depth += int(elem[-1])
    elif elem[0] == "u":
        depth -= int(elem[-1])
print(depth * horizontal)
"""

depth = 0
horizontal = 0
aim = 0

with open("inputs.txt") as inputs:
    directions = inputs.read()
    directions = directions.split("\n")

for elem in directions:
    if elem[0] == "f":
        horizontal += int(elem[-1])
        depth += int(elem[-1]) * aim
    elif elem[0] == "d":
        aim += int(elem[-1])
    elif elem[0] == "u":
        aim -= int(elem[-1])

print(horizontal * depth)
