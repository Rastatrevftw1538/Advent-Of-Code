import math
import re

Code = []
regex = re.compile("([\d]*[^,])")
read = open("CodeListTest.txt", 'r')
CodeList = read.read()
for thing in regex.finditer(CodeList):
    Code.append(int(thing.group(1)))
print(Code, "CODE")


def RunProgram(self, newCodeList):
    for x in self.newCodeList:
        print(x, "newLine")
        if x[0] == 1:
            Change = True
            inPos1 = x[1]
            inPos2 = x[2]
            outPos = x[3]
            add = Code[inPos1] + Code[inPos2]
            print(inPos1, inPos2, outPos)
            print(add)
            print(x, "x")
            print(newCodeList, "newCodeList")
            Code[outPos] = add
            print(Code, "Code")
            print(Code[outPos], "newValue")
            print(x)
            if Change == True:
                Change = False
                MakeNewCode(Code)
        if x[0] == 2:
            Change = True
            inPos1 = x[1]
            inPos2 = x[2]
            outPos = x[3]
            print(Code[inPos1], "num1")
            print(Code[inPos2], "num2")
            multiply = Code[inPos1] * Code[inPos2]
            print(inPos1, inPos2, outPos)
            print(multiply)
            print(x, "x")
            print(newCodeList, "newCodeList")
            Code[outPos] = multiply
            if outPos <= 3:
                newCodeList[newCodeList.index(x)][outPos] = multiply
                print("WARNING", newCodeList[newCodeList.index(x)][outPos])
            print(Code, "Code")
            print(Code[outPos], "newValue")
            print(x)
            if Change == True:
                Change = False
                MakeNewCode(Code)
        for y in x:
            if y == 99:
                return(print(Code))


def MakeNewCode(self, Code):


count = 0
currentCode = []
newCodeList = []
for i in Code:
    # print(i)
    if i == 99:
        currentCode.append(i)
        newCodeList.append(currentCode)
        # print(newCodeList)
    else:
        currentCode.append(i)
        #print(newCodeList, "current")
    count += 1
    #print(count, "count")
    if count == 4:
        newCodeList.append(currentCode)
        currentCode = []
        count = 0
    if i == 99:
        currentCode = []
        count = 0
