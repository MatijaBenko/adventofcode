sum_priority = 0

prior_one = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
             "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
prior_two = {"A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38,
             "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}


one_set = set()
two_set = set()
third_set = set()
counter = 0
string_temp = "y"
temp = []

with open("input.txt", "r") as f:
    sack = [line.strip() for line in f]
    print(sack)
    for eachWord in sack:
        temp.append(eachWord)
        if (len(temp) == 3):
            firstsack = temp[0]
            secondsack = temp[1]
            thirdsack = temp[2]
            
            for eachChar in firstsack:
                if eachChar not in one_set:
                    one_set.add(eachChar)
            for eachChar in secondsack:
                if eachChar not in two_set:
                    two_set.add(eachChar)
            for eachChar in thirdsack:
                if eachChar not in third_set:
                    third_set.add(eachChar)
                    
            for eachChar in one_set:
                if eachChar in two_set and eachChar in third_set:
                    if (eachChar in prior_one):
                        sum_priority += prior_one[eachChar]
                    else:
                        sum_priority += prior_two[eachChar]
                    break
            one_set.clear()
            two_set.clear()
            third_set.clear()
            temp.clear()


print(sum_priority)
