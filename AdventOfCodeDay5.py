

def get_modes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


def get_param(mode, increment, idx, data):
    if mode == 0:
        return data[data[idx + increment]]
    return data[idx + increment]


def get_params(mode1, mode2, idx, data):
    return get_param(mode1, 1, idx, data), get_param(mode2, 2, idx, data)


def add(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    data[data[idx + 3]] = param1 + param2


def multiply(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    data[data[idx + 3]] = param1 * param2


def less_than(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    data[data[idx + 3]] = 1 if param1 < param2 else 0


def equals(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    data[data[idx + 3]] = 1 if param1 == param2 else 0


def jump_if_true(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    return param2 if param1 != 0 else idx + 3


def jump_if_false(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    return param2 if param1 == 0 else idx + 3


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
    return diagnostic


with open("CodeListNewParam.txt", 'r') as CodeList:
    for thing in CodeList:
        inputs = [int(val) for val in thing.split(",")]
        print("Answer: ", main(inputs[:], 1))
