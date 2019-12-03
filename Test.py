def puzzle_one():
    with open("CodeList.txt") as file:
        input = list(map(lambda a: int(a), file.read().split(',')))
        print(input)

    opcode, index = int(input[0]), 0
    while opcode != 99:
        if opcode == 1:
            sum = input[input[index + 1]] + input[input[index + 2]]
            input[input[index + 3]] = sum
        elif opcode == 2:
            product = input[input[index + 1]] * input[input[index + 2]]
            input[input[index + 3]] = product
        elif opcode != 99:
            print('Something went wrong')

        index += 4
        opcode = input[index]

    print(f'Puzzle 1 - {input[0]}')


def puzzle_two():

    goal = 19690720

    with open('CodeList.txt') as file:
        input = list(map(lambda a: int(a), file.read().split(',')))

    found = False
    for noun in range(100):
        for verb in range(100):
            memory = input[:]
            memory[1] = noun
            memory[2] = verb

            opcode, index = int(input[0]), 0
            while opcode != 99:
                if opcode == 1:
                    sum = memory[memory[index + 1]] + memory[memory[index + 2]]
                    memory[memory[index + 3]] = sum
                elif opcode == 2:
                    product = memory[memory[index + 1]] * \
                        memory[memory[index + 2]]
                    memory[memory[index + 3]] = product
                elif opcode != 99:
                    print('Something went wrong')

                index += 4
                opcode = memory[index]

            output = memory[0]

            if output == goal:
                final_noun = noun
                final_verb = verb
                found = True
                break
        if found == True:
            break
    print(f'Puzzle 2 - {100 * final_noun + final_verb}')


# puzzle_one()
puzzle_two()
