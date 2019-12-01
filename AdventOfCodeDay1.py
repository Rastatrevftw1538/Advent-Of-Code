import math
import re


def main(Input):
    read = open(Input, 'r')
    mass = []
    totalFuelValue = 0
    regex = re.compile("([\d]+)")
    massList = read.read()

    for thing in regex.finditer(massList):
        mass.append(thing.group(1))

    for i in mass:
        totalFuelForModule = 0
        fuel_equation = math.floor(int(i) / 3) - 2
        fuel_num = fuel_equation
        totalFuelForModule += fuel_equation
        while fuel_num > 0:
            fuel_num = math.floor(int(fuel_num) / 3) - 2
            if fuel_num > 0:
                totalFuelForModule += fuel_num
        totalFuelValue += totalFuelForModule
    return(print(totalFuelValue))


main("MassList.txt")
