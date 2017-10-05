# a prompt series that outputs a scene plan

# prepare to receive yes/no resposes from the user
affirmativeResponses = ['yes', 'y', 'yep', 'affirmative']
negativeResponses = ['no', 'n', 'nope', 'negative']
def elicitYesOrNoResponse():  # forces yes/no response from user
    x = input()
    if x.lower() in affirmativeResponses:
        return "yes"
    elif x.lower() in negativeResponses:
        return "no"
    else:
        print('Please respond "yes" or "no".')
        return elicitYesOrNoResponse()

# collect the major structural info for the scene
POVCharacter = input("What's the name of the point-of-view character?\n")
goal = input('What is ' + POVCharacter + "'s goal during this scene?\n")

def getObstacle():  # learn the adversary or obstacle name
    print("Will another person get in " + POVCharacter + "'s way?")
    if elicitYesOrNoResponse() == "yes":
        print("Who will it be?")
        return input()
    else:
        print("What will get in their way instead?")
        return input()
obstacle = getObstacle()

# print the scene plan
print("...\n")
print("Scene plan:\n")
print('Point of view character: ' + POVCharacter)
print(POVCharacter, "'s goal: " + goal)
print('Obstacle: ' + obstacle)
