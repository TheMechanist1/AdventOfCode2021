inputpath = 'input.txt'
puzzleinput = open(inputpath,'r')

puzzlelist = []

poneincrease = 0
ponedecrease = 0
poneuhoh = 0

#Part 1
for pi in puzzleinput.readlines():
    puzzlelist.append(int(pi.replace("\n", "")))

print(puzzlelist)

for x in range(len(puzzlelist)):
    if(x > 0):
        if(puzzlelist[x] > puzzlelist[x - 1]):
            poneincrease += 1
        elif(puzzlelist[x] < puzzlelist[x - 1]):
            ponedecrease += 1
        else:
            poneuhoh += 1

print(str(poneincrease) + "\n" + str(ponedecrease) + "\n" + str(poneuhoh))

ptwoincrease = 0
ptwodecrease = 0
ptwouhoh = 0

#Part 2
for y in range(len(puzzlelist)):
    if(y > 0 and y < len(puzzlelist) - 2):
        thissection = puzzlelist[y] + puzzlelist[y + 1] + puzzlelist[y + 2]
        prevsection = puzzlelist[y - 1] + puzzlelist[y] + puzzlelist[y + 1]

        if(thissection > prevsection):
            ptwoincrease += 1
        elif(thissection < prevsection):
            ptwodecrease += 1
        else:
            ptwouhoh += 1

print(str(ptwoincrease) + "\n" + str(ptwodecrease) + "\n" + str(ptwouhoh))
