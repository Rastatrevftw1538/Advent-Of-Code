import re


def checkForCriteria(i):
    repnum = False
    for x1, x2 in zip(str(i), str(i)[1:]):
        if x1 > x2:
            return False
        elif x1 == x2:
            repnum = True
    return repnum


def checkForCriteria_Rept(i):
    repnum = 0
    boolean = False
    for x1, x2 in zip(str(i), str(i)[1:]):
        if x1 > x2:
            return False
        elif x1 == x2:
            repnum += 1
        else:
            if repnum == 1:
                boolean = True
            repnum = 0
    if repnum == 1:
        boolean = True
    return boolean


def main(Input):
    difPass1 = 0
    difPass2 = 0
    read = open(Input, "r")
    PassRang = read.read()
    PassMin = ""
    PassMax = ""
    regex = re.compile("([\d]{6})-([\d]{6})")
    for thing in regex.finditer(PassRang):
        PassMin = thing.group(1)
        PassMax = thing.group(2)
    print(PassMin, PassMax, "Ranges")
    for i in range(int(PassMin), int(PassMax)+1):
        if checkForCriteria(i):
            # print(checkForCriteria(i))
            difPass1 += 1
        if checkForCriteria_Rept(i):
            # print(checkForCriteria_Rept(i))
            difPass2 += 1
    print("Answer 1 ", difPass1)
    print("Answer 2 ", difPass2)


main("PasswordRange.txt")
