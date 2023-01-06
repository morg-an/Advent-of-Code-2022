import math
import datetime

start = datetime.datetime.now()

def readFile():
    with open("day11sample.txt", 'r') as observations:
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
        return self.numInspected

    def takeTurn(self):
        # 0. Loop Items
        #print("Items: ", self.items)
        i = 0
        while i < len(self.items):
            #print(f"Monkey inspects an item with a worry level of {self.items[i].worryLevel}")
            # 1. Monkey inspects item and worry level is adjusted.
            if self.operationValue == 'old':
                if self.operator == '*':
                    newWorryLevel = self.items[i].worryLevel*self.items[i].worryLevel
                elif self.operator == '+':
                    newWorryLevel = self.items[i].worryLevel+ self.items[i].worryLevel
            elif self.operator == '*':
                newWorryLevel = self.operationValue*self.items[i].worryLevel
                #print(f"Worry level is multipled by {self.operationValue} to {newWorryLevel}")
            elif self.operator == '+':
                newWorryLevel = self.operationValue+self.items[i].worryLevel
            self.items[i].changeWorryLevel(newWorryLevel)

            # 2. Monkey done inspecting. WorryLevel / 3, rounded down
            self.numInspected += 1
            #newWorryLevel = math.floor((self.items[i].worryLevel)/3)
            #print(f"Worry level divided by 3 to {newWorryLevel}")
            #self.items[i].changeWorryLevel(newWorryLevel)

            # 3. Check if divisible
            divisible = False
            if newWorryLevel % self.divisibleBy == 0:
                divisible = True
                
            # 4. Throw item
            if divisible:
                Monkey._registry[self.trueDest].items.append(self.items[i])
                self.items.pop(0)
            else:
                #print(f"Current worry level is not divisible by {self.divisibleBy}.")
                Monkey._registry[self.falseDest].items.append(self.items[i])
                self.items.pop(0)

        #print('\n')

class Item():
    _inventory = []

    def __init__(self, worryLevel):
        self.worryLevel = worryLevel
        self._inventory.append(self)
    
    def getWorryLevel(self):
        return self.worryLevel
    
    def changeWorryLevel(self, newLevel):
        self.worryLevel = newLevel

def createObjects(parcedObservations):
    for index, monkey in enumerate(parcedObservations):
        items = []
        monkeyDeets = parcedObservations[index]
        for item in parcedObservations[index][0]:
            items.append(Item(item))
        Monkey(items, monkeyDeets[1][0], monkeyDeets[1][1], monkeyDeets[2],monkeyDeets[3], monkeyDeets[4])

def monkeyRound():
    for monkey in Monkey._registry:
        monkey.takeTurn()

def monkeyRounds():
    rounds = 900
    i = 0
    while i < rounds:
        print("round", i)
        monkeyRound()
        i += 1

def calcMonkeyBusiness():
    inspectionCount = []
    for monkey in Monkey._registry:
        inspectionCount.append(monkey.getNumInspected())
    sortedInspections = sorted(inspectionCount)
    #print(inspectionCount)
    monkeyBusiness = sortedInspections[-1]*sortedInspections[-2]
    return monkeyBusiness

def printMonkeys():
    print(Monkey._registry)

observations = readFile()
parcedObservations = parceObservations(observations)
# parced observations = [[[items],[operator, number], test, true, false] [NEXT MONKEY], ...]
#print(parcedObservations)
createObjects(parcedObservations)
monkeyRounds()
monkeyBusiness = calcMonkeyBusiness()
print(monkeyBusiness)

end = datetime.datetime.now()
print(f"Start: {start} End: {end} Runtime: {end-start}")