from gmpy2 import mpz
import datetime
import numpy as np

start = datetime.datetime.now()

def readFile():
    with open("day11input.txt", 'r') as observations:
        observations = observations.read()
    return observations

def parceObservations(observations):
    separateMonkeys = observations.split('\n\n')
    parcedObservations = []
    for monkey in separateMonkeys:
        parcedObservations.append(monkey.split('\n'))
    for monkey in parcedObservations:
        #remove unnecessary first line
        monkey.pop(0)
        #trim whitespace
        for index, line in enumerate(monkey):
            monkey[index] = line.strip()

        #starting items
        monkey[0] = list(map(int, monkey[0].strip("Starting items: ").split(", ")))
        startingItems = monkey[0]

        #operation
        monkey[1] = monkey[1].split()[-2:]
        try:
            monkey[1][1] = int(monkey[1][1])
        except ValueError:
            pass
        operation = monkey[1]

        #test: divisible by
        monkey[2] = int(monkey[2].split()[-1])
        testCondition = monkey[2]

        #true outcome ("Throw to monkey ...")
        monkey[3] = int(monkey[3].split()[-1])
        trueOutcome = monkey[3]

        #false outcome ("Throw to monkey ...")
        monkey[4] = int(monkey[4].split()[-1])
        falseOutcome = monkey[4]
        
    return parcedObservations

class Monkey():
    _registry = []

    def __init__(self, items, operator, operationValue, divisibleBy, trueDest, falseDest, numInspected = 0):
        self.items = items
        self.operator = operator
        self.operationValue = operationValue
        self.divisibleBy = divisibleBy
        self.trueDest = trueDest
        self.falseDest = falseDest
        self.numInspected = numInspected
        self._registry.append(self)
    
    def printMonkey(self):
        print(f"Items: {self.items} Num Inspected: {self.numInspected}")
        for item in self.items:
            worry = item.getWorryLevel()
            print(worry)

    def getNumInspected(self):
        return mpz(self.numInspected)

    def takeTurn(self, lcm):
        # 0. Loop Items
        #print("Items: ", self.items)
        for i in range(len(self.items)):
            #print(f"Monkey inspects an item with a worry level of {self.items[i].worryLevel}")
            # 1. Monkey inspects item and worry level is adjusted.

            currentWorry = mpz(self.items[i].worryLevel)
            operationValue = self.operationValue
            operator = self.operator
            
            if operator == '+':
                nextWorry = currentWorry + operationValue

            elif operationValue == 'old':
                nextWorry = currentWorry * currentWorry

            elif operator == '*':
                nextWorry = currentWorry * operationValue
                #print(f"Worry level is multipled by {self.operationValue} to {newWorryLevel}")

            nextWorry = nextWorry % lcm
            self.items[i].setWorryLevel(nextWorry)

            # 2. Monkey done inspecting.
            self.numInspected += 1

            if mpz(nextWorry) % self.divisibleBy != 0:
                Monkey._registry[self.falseDest].items.append(self.items[i])
            else:
                Monkey._registry[self.trueDest].items.append(self.items[i])

        self.items = []
        #print('\n')

class Item():

    # def __init__(self, worryLevel):
    #     self.worryLevel = worryLevel
    
    def __init__(self, worryLevel):
        self.worryLevel = worryLevel

    def getWorryLevel(self):
        return mpz(self.worryLevel)
    
    def getRemainder(self):
        return mpz(self.remainder)
    
    def setWorryLevel(self, newLevel):
        self.worryLevel = mpz(newLevel)
    
    def setRemainder(self, remainder):
        self.remainder = remainder

def createObjects(parcedObservations):
    for index, monkey in enumerate(parcedObservations):
        items = []
        monkeyDeets = parcedObservations[index]
        for item in parcedObservations[index][0]:
            items.append(Item(item))
        Monkey(items, monkeyDeets[1][0], monkeyDeets[1][1], monkeyDeets[2],monkeyDeets[3], monkeyDeets[4])

def monkeyRound(lcm):
    #find common demominator
    for monkey in Monkey._registry:
        monkey.takeTurn(lcm)

def monkeyRounds(lcm):
    rounds = 10000
    i = 0
    while i < rounds:
        print("round", i)
        monkeyRound(lcm)
        i += 1

def calcMonkeyBusiness():
    inspectionCount = []
    for monkey in Monkey._registry:
        inspectionCount.append(monkey.getNumInspected())
    print(inspectionCount)
    sortedInspections = sorted(inspectionCount)
    #print(inspectionCount)
    monkeyBusiness = sortedInspections[-1]*sortedInspections[-2]
    return monkeyBusiness

def printMonkeys():
    print(Monkey._registry)

def findLCM(parcedObservations):
    allDenominators = []
    for monkey in parcedObservations:
        allDenominators.append(monkey[2])
    lcm = int(np.lcm.reduce(allDenominators))
    print(type(lcm))
    return lcm

observations = readFile()
parcedObservations = parceObservations(observations)
# parced observations = [[[items],[operator, number], test, true, false] [NEXT MONKEY], ...]
lcm = findLCM(parcedObservations)
createObjects(parcedObservations)
monkeyRounds(lcm)
monkeyBusiness = calcMonkeyBusiness()
print(monkeyBusiness)

end = datetime.datetime.now()
print(f"Start: {start} End: {end} Runtime: {end-start}")