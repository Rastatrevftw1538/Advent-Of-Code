import re


def main1(Input):
    Code = []
    regex = re.compile("([\d]*[^,])")
    read = open(Input, 'r')
    CodeList = read.read()
    for thing in regex.finditer(CodeList):
        Code.append(int(thing.group(1)))
    print(Code, "CODE")

    opcode, index = int(Code[0]), 0
    while opcode != 99:
        print(opcode)
        if opcode == 1:
            add = Code[Code[index+1]] + Code[Code[index+2]]
            Code[Code[index + 3]] = add
        elif opcode == 2:
            multiply = Code[Code[index+1]] * Code[Code[index+2]]
            Code[Code[index + 3]] = multiply
        index += 4
        opcode = Code[int(index)]
    answer = Code[0]
    return (print(answer))


def main2(Input):
    ans_noun = 0
    ans_verb = 0
    Code = []
    regex = re.compile("([\d]*[^,])")
    read = open(Input, 'r')
    CodeList = read.read()
    for thing in regex.finditer(CodeList):
        Code.append(int(thing.group(1)))
    print(Code, "CODE")
    done = False
    for noun in range(100):
        for verb in range(100):
            mem = Code[:]
            mem[1] = noun
            mem[2] = verb
            opcode, index = int(Code[0]), 0
            while opcode != 99:
                # print(opcode)
                if opcode == 1:
                    add = mem[mem[index+1]] + mem[mem[index+2]]
                    mem[mem[index + 3]] = add
                elif opcode == 2:
                    multiply = mem[mem[index + 1]] * mem[mem[index+2]]
                    #print(mem[mem[index + 3]], "yay")
                    mem[mem[index + 3]] = multiply
                elif opcode != 99:
                    print('HALT-RESTARTING')
                index += 4
                opcode = mem[index]
            answer = mem[0]

            if answer == 19690720:
                ans_noun = noun
                ans_verb = verb
                done = True
                break
        if done == True:
            break
    print(ans_noun)
    print(ans_verb)
    print(100 * ans_noun + ans_verb)


main1("CodeList.txt")
main2("CodeList.txt")
