

def get_modes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


def get_param(mode, increment, index, data):
    if mode == 0:
        return data[data[index + increment]]
    return data[index + increment]


def get_params(mode1, mode2, index, data):
    return get_param(mode1, 1, index, data), get_param(mode2, 2, index, data)


def add(mode1, mode2, index, data):
    param1, param2 = get_params(mode1, mode2, index, data)
    data[data[index + 3]] = param1 + param2


def multiply(mode1, mode2, index, data):
    param1, param2 = get_params(mode1, mode2, index, data)
    data[data[index + 3]] = param1 * param2


def less_than(mode1, mode2, index, data):
    param1, param2 = get_params(mode1, mode2, index, data)
    data[data[index + 3]] = 1 if param1 < param2 else 0


def equals(mode1, mode2, index, data):
    param1, param2 = get_params(mode1, mode2, index, data)
    data[data[index + 3]] = 1 if param1 == param2 else 0


def jump_if_true(mode1, mode2, index, data):
    param1, param2 = get_params(mode1, mode2, index, data)
    return param2 if param1 != 0 else index + 3


def jump_if_false(mode1, mode2, index, data):
    param1, param2 = get_params(mode1, mode2, index, data)
    return param2 if param1 == 0 else index + 3


def main(data, inputs):
    index = 0
    diagnostic = None
    while data[index] != 99:
        mode1, mode2, mode3, opcode = get_modes(f"{data[index]:05}")
        if opcode == 1:
            add(mode1, mode2, index, data)
            index += 4
        elif opcode == 2:
            multiply(mode1, mode2, index, data)
            index += 4
        elif opcode == 3:
            data[data[index + 1]] = inputs
            index += 2
        elif opcode == 4:
            diagnostic = data[data[index + 1]]
            index += 2
        elif opcode == 5:
            index = jump_if_true(mode1, mode2, index, data)
        elif opcode == 6:
            index = jump_if_false(mode1, mode2, index, data)
        elif opcode == 7:
            less_than(mode1, mode2, index, data)
            index += 4
        elif opcode == 8:
            equals(mode1, mode2, index, data)
            index += 4
    return diagnostic


with open("CodeListNewParam.txt", 'r') as CodeList:
    for thing in CodeList:
        inputs = [int(val) for val in thing.split(",")]
        print("Answer Part 1: ", main(inputs[:], 1))
        print("Answer Part 2: ", main(inputs[:], 5))
