inputpath = 'input.txt'
puzzleinput = open(inputpath,'r')

puzzlelist = []

increase = 0
decrease = 0
uhoh = 0

for pi in puzzleinput.readlines():
    puzzlelist.append(int(pi.replace("\n", "")))

print(puzzlelist)

for x in range(len(puzzlelist)):
    if(x > 0):
        if(puzzlelist[x] > puzzlelist[x - 1]):
            increase += 1
        elif(puzzlelist[x] < puzzlelist[x - 1]):
            decrease += 1
        else:
            uhoh += 1

print(str(increase) + "\n" + str(decrease) + "\n" + str(uhoh))
            
