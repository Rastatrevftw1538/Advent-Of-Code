import re


def main1(Input):
    i = j = 0
    step = 1
    path = {}
    for t in Input:
        dir, position = t[0], int(t[1:])
        x = y = 0
        if dir == 'U':
            x = -1
        elif dir == 'D':
            x = 1
        elif dir == 'L':
            y = -1
        elif dir == 'R':
            y = 1
        else:
            raise Exception('Unexpected direction')

        for _ in range(position):
            i += x
            j += y
            path[(i, j)] = step
            step += 1
    return path


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def calculate_min_distance(intersections):
    return min(dist(point, (0, 0)) for point in intersections)


def calculate_min_steps(intersections, steps_a, steps_b):
    min_steps = float('inf')
    for point in intersections:
        if point not in steps_a or point not in steps_b:
            raise Exception('Not an shared path intersection.')
        min_steps = min(min_steps, steps_a[point] + steps_b[point])
    return min_steps
    #length = int(i[1: len(i)])
    # if i[0] == "R":
    #print("+".rjust(length, "-"))
    # if i[0] == "U":
    #print("+" + length * "|\n", end='+', flush=True)
    # if i[0] == "D":
    #print("+" + -length * "|\n", end='+', flush=True)
    # if i[0] == "L":
    #print("+".ljust(length, "-"))


wire1 = ""
wire2 = ""
regex = re.compile("([,((\w{1})[(\d*))]+)[\s]*([,((\w{1})[(\d*))]+)")
read = open("WireList.txt", 'r')
WireList = read.read()
for thing in regex.finditer(WireList):
    wire1 = thing.group(1)
    wire2 = thing.group(2)
wire1, wire2 = wire1.strip().split(","), wire2.strip().split(",")


path_wire1, path_wire2 = main1(wire1), main1(wire2)
intersections = list(set(path_wire1.keys()) & set(path_wire2.keys()))
print(calculate_min_distance(intersections), "answer")


def main2(Input):

    return


# main2("WireList.txt")
