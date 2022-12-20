with open('input.txt', 'r') as input:
    rations = input.readlines()

elfInventory = []
elfTotals = []
answer = 0

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

for x in range(0, 3):
    answer += max(elfTotals)
    elfTotals.remove(max(elfTotals))

print(answer)