import math
#from math import log
import sys
#import timeit

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
        print(f"Inspected: {self.numInspected}")
        for item in self.items:
            worry = item.worryLevel
            print(worry)
            print(f"Num Size {sys.getsizeof(worry)}")
        print('\n')

    def getNumInspected(self):
        return self.numInspected

    def takeTurn(self):
        #self.printMonkey()

        # 0. Loop Items
        for i in range(len(self.items)):
            # 1. Monkey inspects item and worry level is adjusted.
            currenWorryLevel = (self.items[i].worryLevel * self.items[i].multiplier) + self.items[i].remainder
            #print(f"Monkey inspects an item with a worry level of {currenWorryLevel}")
            operationValue = self.operationValue

            if self.operator == '+':
                newWorry = operationValue + currenWorryLevel
                #print(f"new worry(1): {newWorry} operation {operationValue} + current {currenWorryLevel}")
                #self.items[i].changeWorryLevel(operationValue + currenWorryLevel)
                #newWorryLevel = operationValue + currenWorryLevel
            elif type(self.operationValue) == int:
                newWorry = operationValue * currenWorryLevel
                #print(f"new worry(2): {newWorry} operation {operationValue} * current {currenWorryLevel}")
                #self.items[i].changeWorryLevel(operationValue * currenWorryLevel)
                #newWorryLevel = operationValue * currenWorryLevel
            else:
                newWorry = currenWorryLevel * currenWorryLevel
                #print(f"new worry (3): {newWorry} current worry {currenWorryLevel} * {currenWorryLevel}")
                #self.items[i].changeWorryLevel(currenWorryLevel * currenWorryLevel)
                #newWorryLevel = currenWorryLevel * currenWorryLevel

            #self.items[i].changeWorryLevel(newWorryLevel)

            # 2. Monkey done inspecting. WorryLevel / 3, rounded down
            self.numInspected += 1
            #newWorryLevel = math.floor((self.items[i].worryLevel)/3)
            #print(f"Worry level divided by 3 to {newWorryLevel}")
            #self.items[i].changeWorryLevel(newWorryLevel)

            if self.items[i].multiplier == 1:
                multiplier = self.divisibleBy
            else:
                multiplier = self.items[i].multiplier

            dMod = divmod(newWorry, multiplier)
            quotient = dMod[0]
            remainder = dMod[1]
            #print(f"dMod 1 - quotient: {quotient} remainder: {remainder} multiplier: {multiplier}")

            # if quotient >= 300000000000000:
            #     multiplier += 5000000
            #     dMod2 = divmod(newWorry, multiplier)
            #     quotient = dMod2[0] 
            #     remainder = dMod2[1]

            # elif quotient >= 5000:
            #     multiplier += 5000
            #     dMod2 = divmod(newWorry, multiplier)
            #     quotient = dMod2[0] 
            #     remainder = dMod2[1]

            # elif quotient < 5000 and quotient > 1000:
            #     multiplier += 1000
            #     dMod3 = divmod(newWorry, multiplier)
            #     quotient = dMod3[0]
            #     remainder = dMod3[1]
            
            # elif quotient < 1000 and quotient > 101:
            #     multiplier += 1000
            #     dMod4 = divmod(newWorry, multiplier)
            #     quotient = dMod4[0]
            #     remainder = dMod4[1]

                #print(f"dMod 2 - quotient: {quotient} remainder: {remainder} multiplier: {multiplier}")
            # if(dMod[0] > 1000):
            #     print(f"Number is still too big.({dMod[0]})")
            #     newDivisibleBy += 100
            #     print(f"New Divisible By: {newDivisibleBy}")
            #     dMod = divmod(newWorry, newDivisibleBy)
            self.items[i].worryLevel = quotient
            self.items[i].remainder = remainder
            self.items[i].multiplier = multiplier

            # 3. Check if divisible & throw
            if ((quotient * multiplier) + remainder) % self.divisibleBy != 0:
                Monkey._registry[self.falseDest].items.append(self.items[i])
            else:
                Monkey._registry[self.trueDest].items.append(self.items[i])

        self.items = []

class Item():

    def __init__(self, worryLevel, multiplier = 1, remainder = 0):
        self.worryLevel = worryLevel
        self.multiplier = multiplier
        self.remainder = remainder

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
    for i in range(len(Monkey._registry)):
    #for monkey in Monkey._registry:
        #f(f"Monkey {i}'s Turn")
        Monkey._registry[i].takeTurn()

def monkeyRounds():
    rounds = 900
    for i in range(rounds):
        print("round: ", i)
        monkeyRound()

def calcMonkeyBusiness():
    inspectionCount = []
    for monkey in Monkey._registry:
        inspectionCount.append(monkey.getNumInspected())
    print(inspectionCount)
    sortedInspections = sorted(inspectionCount)
    #print(inspectionCount)
    monkeyBusiness = sortedInspections[-1]*sortedInspections[-2]
    return monkeyBusiness

# credit for this function to: https://www.youtube.com/watch?v=s3mxIcr7fOQ&t=607s
# def convertFromBase10(num, base):
#     numToChar = {i:'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYX'[i] for i in range(36)}
#     power = int(log(num, base))
#     converted = ""
#     for pow in range(power, -1, -1):
#         converted += numToChar[num // (base**pow)]
#         num %= base**pow
#     return converted

observations = readFile()
parcedObservations = parceObservations(observations)
# parced observations = [[[items],[operator, number], test, true, false] [NEXT MONKEY], ...]
#print(parcedObservations)
createObjects(parcedObservations)
monkeyRounds()
monkeyBusiness = calcMonkeyBusiness()
print(monkeyBusiness)

# testNum = 1872031030704835834282883558571563833954770036049273547297565114521455780848687183242848226735933234959221550961010449546954383823542458817009679857240859501933221266287131228020263718885026030389754903084027969997953552214147391870855669792123415263592714395410911744070582657594917173000067218910154862759103681253861713764506496651828360370393567957994752677455243372757280493283502832966007330079047360877518419307984120870629080018205978801343594771025056711425444470037044323970719255162951126198898321186921911198656226779319211444084900420386770801622043107667333731498530323942134521590919299620561326603670439047120220411728070708551120847022258380007412906596816046813723890310037472043906581621058774758994696225727418304146492641461426780579284899941208614070220282956583060069822647557862295857117547330498486529134628181692024763816330192566241464816561652849157856905200848144432604239642739639233657896269150675719721767691610376222427189016640555902939267619446600958815036934087215012448299698787034410939438715455358302748453728373011654950777779796220150186511703295224098840191738920014945745458423483678022250354519298646871068237285807156265412211481639918703456004834152743409157642819837399395050284103099518120113261470128397998347039475106816176206770569649398436676806093724570474438375078117226968573473835243268765969907129961807455000885916181271779098721085353251568141053188206297088016964701261361922939661790005893001018322324858523160391767169677028640902746214320664869877941917066382988219825036417654553068108836744030911443044520841609538224367664051561747381856605066436088118350688264775545022920881487965470337882968711600633290515974553689276928676812623342847464544525816890805314357637739045908080358943612975960081376953777079146251574700942291215399774875597321141934343064524527246373441675838103801519513468084431936
# convertedNum = convertFromBase10(testNum, 36)
# print(convertedNum)
# print("Converted Size ", sys.getsizeof(convertedNum))



value = 250000089
intSquRoot = math.floor(math.sqrt(value))
dMod = divmod(value, intSquRoot)
#print("Test Answer: ", (dMod[0] * dMod[0]) + dMod[1]) 
#print("Correct Answer: ", value)

# considered log, but that returns a float, so that won't help
# considered numpy, but that works with numbers in a list, which isn't relevant here.