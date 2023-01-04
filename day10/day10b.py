def readFile():
    with open("day10input.txt", 'r') as program:
        program = program.readlines()
    return program

def parceFile(program):
    parcedFile = []
    for line in program:
        toAppend = line.strip('\n').split()
        if len(toAppend) == 2:
            toAppend[1] = int(toAppend[1])
        parcedFile.append(toAppend)
    return parcedFile

def incrementClock(clock, register):
    programLog[clock] = [register, register]
    return programLog

def incClockAndRegister(clock, register, valueToAdd):
    newValue = register+valueToAdd
    programLog[clock] = [register, newValue]
    return newValue

def main(parcedFile, clock, register, programLog):
    clock += 1
    for line in parcedFile:
        #print(line)
        if line[0] == 'noop':
            incrementClock(clock, register)
            clock += 1
            #print(f"Program Log (after noop): {programLog}")
        elif line[0] == 'addx':
            incrementClock(clock, register)
            #print(f"Program Log (after addx pt. 1): {programLog}")
            clock += 1
            register = incClockAndRegister(clock, register, line[1])
            #print(f"Program Log (after addx pt. 2): {programLog}")
            clock += 1
        #print('\n')
    #print("Program Log: ", programLog)
    return programLog

def renderScreen(signalLog):
    crt=""
    for key, value in signalLog.items():
        xPosition = (key-1)%40
        register = value[0]
        if register == xPosition or register == xPosition - 1 or register == xPosition + 1:
            crt+='#'
        else:
            crt+="."
    print(crt[0:40])
    print(crt[40:80])
    print(crt[80:120])
    print(crt[120:160])
    print(crt[160:200])
    print(crt[200:])

#set global variables
clock = 0
programLog = {}
register = 1

program = readFile()
parcedFile = parceFile(program)
signalLog = main(parcedFile, clock, register, programLog)
renderScreen(signalLog)