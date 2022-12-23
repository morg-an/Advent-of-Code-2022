with open('day1input.txt', 'r') as input:
    rations = input.readlines()

elfInventory = []
elfTotals = []
i = 0
rations.insert(0, '\n')

for item in rations:
    if item == '\n':
        elfInventory.append([])
        i += 1
    else:
        elfInventory[i-1].append(int(item.strip()))

for elf in elfInventory:
    totalCalories = 0
    for snack in elf:
        totalCalories += snack
    elfTotals.append(totalCalories)

answer = max(elfTotals)

print(answer)
