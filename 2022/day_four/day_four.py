firstSec = []
secondSec = []
counter = 0
with open("input.txt", "r") as f:
    sack = [line.strip().split(",") for line in f]
    for eachSect in sack:
        for eachTime in eachSect:
            if not firstSec:
                firstSec = eachTime.split("-")
            else:
                secondSec = eachTime.split("-")
        if (int(firstSec[1]) < int(secondSec[0])):
            firstSec.clear()
            secondSec.clear()
            continue
        elif (int(secondSec[1]) < int(firstSec[0])):
            firstSec.clear()
            secondSec.clear()
            continue
        else:
            counter += 1
        firstSec.clear()
        secondSec.clear()
        

print(counter)
