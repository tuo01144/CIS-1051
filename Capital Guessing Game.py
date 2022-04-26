statesData = open("capitals data/USStateCapitals.csv", "r")
statesText = statesData.readlines()
statesList = []
capitalsList = []
statesDict = {}
for i in range(len(statesText)):
    pairing = statesText[i].split(",")
    statesList.append(pairing[0])
    capitalsList.append(pairing[1])
    capitalStr = pairing[1]
    alteredStr = capitalStr[:len(capitalStr) - 1]
    statesDict[pairing[0]] = alteredStr

usersData = open("capitals data/usernames.csv", "r")
readUsers = usersData.readlines()
usersList = []
scoresList = []
userIndex = {}
for items in readUsers:
    listItems = items.split(",")
    user = str(listItems[0])
    score = str(listItems[1])
        
    usersList.append(user)
    alteredScore = score[:len(score) - 1]
    scoresList.append(alteredScore)
    userIndex[user] = alteredScore
usersData.close()

def savingNewUser(username, score):
    usersFile = open("capitals data/usernames.csv", "a")
    score = str(score)
    usersFile.write(username + "," + score + "\n")
    userIndex[username] = score
    usersFile.close()
    

def welcome():
    print("Welcome to my capital guessing game!")
    print()
    name = str(input("Create/enter your username: "))
    if name in usersList:
        print()
        print("Welcome back " + name + "!")
        print("Your highscore is " + userIndex[name])
        print("Let's get started!")
        print()
    else:
        score = 0
        savingNewUser(name, score)
        print()
        print("Nice to meet you", name)
        print("Let's get started!")
        print()

    return name


def shuffle():
    
    import random
    ticket = random.randint(0,49)
    selectState = statesList[ticket]
    return selectState


def statesGame():
    score = 0
    index = 0
    done = False
    while index < 50:
        state = shuffle()
        capital = statesDict[state]
        answer = str(input("What is the capital of " + state + "? "))
        print()
        answer = answer.lower()
        state = state.lower()
        capital = capital.lower()

        if answer == capital:
            score += 10
            print("Correct! That's 10 points.")
            index += 1
            command = str(input("Press enter to go again or type anything to quit "))
            print()
            if command != "":
                index = 50
        else:
            print("Incorrect. You have one more attempt.")
            state = state.capitalize()
            capital = capital.capitalize()
            answer = str(input("What is the capital of " + state + "? "))
            print()
            answer = answer.lower()
            state = state.lower()
            capital = capital.lower()
            
            if answer == capital:
                score += 5
                print("Phew! That was a close one. That's 5 points")
                index += 1
                command = str(input("Press enter to go again or type anything to quit "))
                print()
                if command != "":
                    index = 50
            else:
                state = state.capitalize()
                capital = capital.capitalize()
                print("Incorrect. The capital of " + state + " is " + capital)
                index += 1
                command = str(input("Press enter to go again or type anything to quit "))
                print()
                if command != "":
                    index = 50

    score = str(score)
    print()
    print("Game complete. You scored", score, "points!")
    print()
    return score


def game():
    name = welcome()
    score = statesGame()
    intScore = int(score)
    oldScore = str(userIndex[name])
    intOldScore = int(userIndex[name])
    print("Select a save option:")
    print("[1] Add this score to your total. New score will be", (intScore + intOldScore))
    print("[2] Save this as a new score. New score will be", score)
    print()
    
    done = False
    while not done:
        decision = str(input("Type 1 or 2: "))
        if decision == "1" or decision == "2":
            done = True

    file = open("capitals data/usernames.csv", "r")
    text = file.readlines()        
    file = open("capitals data/usernames.csv", "w")
    for lines in text:
        if str(lines.strip("\n")) != str(name + "," + oldScore):  
            file.write(lines)

    if decision == "1":
        newScore = str(intScore + intOldScore)
        file = open("capitals data/usernames.csv", "a")
        file.write(name + "," + newScore + "\n")
    else:
        file = open("capitals data/usernames.csv", "a")
        file.write(name + "," + score + "\n")


def fullScript():
    done = False
    while not done:
        game()
        command = str(input("Input anything to return to the main menu "))
        print()


fullScript()


