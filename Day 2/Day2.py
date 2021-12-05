inputpath = 'input.txt'
puzzleinput = open(inputpath,'r')

puzzlelist = []

for pi in puzzleinput.readlines():
    puzzlelist.append(pi.replace("\n", ""))

horizontal = 0
depth = 0

#Part 1
for x in range(len(puzzlelist)):
    newinputlist = puzzlelist[x].split(" ")
    direction = newinputlist[0]
    amount = int(newinputlist[1])

    match direction:
        case "forward":
            horizontal += amount
            continue
        case "up":
            depth -= amount
            continue
        case "down":
            depth += amount
            continue

print(str(horizontal) + " " + str(depth))
print(str(horizontal*depth))

horizontal = 0
depth = 0
aim = 0

#Part 2
for x in range(len(puzzlelist)):
    newinputlist = puzzlelist[x].split(" ")
    direction = newinputlist[0]
    amount = int(newinputlist[1])

    match direction:
        case "forward":
            horizontal += amount
            depth += amount * aim
            continue
        case "up":
            aim -= amount
            continue
        case "down":
            aim += amount
            continue

print(str(horizontal) + " " + str(depth))
print(str(horizontal*depth))
