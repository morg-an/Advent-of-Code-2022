file = open("day2input.txt", 'r')

strategyGuide = file.readlines()
score = 0

for game in strategyGuide:
    opponentGuess = game[0]
    guess = game[2]
    
    # Add to score based on guess
    if guess == 'X': #Rock
        score += 1
    if guess == 'Y': #Paper
        score += 2
    if guess == 'Z': #Scissors:
        score += 3

    if opponentGuess == 'A': #Rock
        if guess == 'X': #Rock
            outcome = "tie"
        if guess == 'Y': #Paper
            outcome = "win"
        if guess == 'Z': #Scissors
            outcome = "lose"

    elif opponentGuess == 'B': #Paper
        if game[2] == 'X': #Rock
            outcome = "lose"
        if game[2] == 'Y': #Paper
            outcome = "tie"
        if game[2] == 'Z': #Scissors
            outcome = "win"

    elif opponentGuess == 'C': #Scissors
        if game[2] == 'X': #Rock
            outcome = "win"
        if game[2] == 'Y': #Paper
            outcome = "lose"
        if game[2] == 'Z': #Scissors
            outcome = "tie"

    if outcome == 'win':
        score += 6
    if outcome == "tie":
        score += 3

print(score)
