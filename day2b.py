file = open("day2input.txt", 'r')

strategyGuide = file.readlines()
score = 0

for game in strategyGuide:
    opponentGuess = game[0]
    guess = ""

    if game[2] == 'X':
        objective = 'Lose'
    if game[2] == 'Y':
        objective = 'Tie'
    if game[2] == 'Z':
        objective = 'Win'

    if objective == 'Tie':
        score += 3
        if opponentGuess == 'A': #rock
            score += 1
        if opponentGuess == 'B': #paper
            score += 2
        if opponentGuess == 'C': #scissors
            score += 3
    
    if objective == 'Win':
        score += 6
        if opponentGuess == 'A': #rock
            guess = "paper"
        if opponentGuess == 'B': #paper
            guess = "scissors"
        if opponentGuess == 'C': #scissors
            guess = "rock"

    if objective == 'Lose':
        if opponentGuess == 'A': #rock
            guess = "scissors"
        if opponentGuess == 'B': #paper
            guess = "rock"
        if opponentGuess == 'C': #scissors
            guess = "paper"

    if guess == "rock":
        score += 1
    elif guess == "paper":
        score += 2
    elif guess == "scissors":
        score += 3
    
print(score)
