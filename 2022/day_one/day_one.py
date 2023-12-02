elf_max = 0
elf_temp = 0
topThree = []


with open("input.txt", "r") as f:
    list_elves = [line.strip() for line in f]
    for eachItem in list_elves:
        if (eachItem != ''):
            elf_temp += int(eachItem)
        
        else:
            if elf_temp > elf_max:
                elf_max = elf_temp
            print(topThree)
            if (len(topThree) < 3):
                topThree.append(elf_max)
                topThree = sorted(topThree)
            if (len(topThree) == 3):
                topThree = sorted(topThree)
                for eachElf in range(0, len(topThree)):
                    if (elf_temp > topThree[eachElf]):
                        topThree[eachElf] = elf_temp
                        break
            elf_temp = 0
            
    print(sum(topThree))
    print(elf_max)