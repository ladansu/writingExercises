# a prompt series that displays different prompts based on user input, choose-your-own-adventure style

# prepare to receive yes/no resposes from the user
affirmativeResponses = ['yes', 'y', 'yep', 'affirmative']
negativeResponses = ['no', 'n', 'nope', 'negative']
def getYNResponses(x): # forces yes/no response from user
     if (x) in affirmativeResponses:
         return "yes"
     elif (x) in negativeResponses:
         return "no"
     else:
         x = input('Please respond "yes" or "no".\n')
         return getYNResponses(x)

# collect the major structural info for the scene
POVCharacter = input("What's the name of the point-of-view character?\n")
goal = input('What is ' + POVCharacter + "'s goal during this scene?\n")

def getAdversaryYN(): # check if there's an adversary
    return input("Will another person get in " + POVCharacter + "'s way?\n")

def getObstacle(): # learn the adversary or obstacle name
    if getYNResponses(getAdversaryYN()) == "yes":
        return input("Who will it be?\n")
    else:
        return input("What will get in their way instead?\n")
obstacle = getObstacle()

# print the scene plan
print("...\n")
print("Scene plan:\n")
print('Point of view character: ' + POVCharacter)
print(POVCharacter, "'s goal: " + goal)
print('Obstacle: ' + obstacle)
