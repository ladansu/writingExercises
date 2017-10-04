# a prompt series that displays different prompts based on user input, choose-your-own-adventure style

affirmativeResponses = ['yes', 'y', 'yep', 'affirmative']
negativeResponses = ['no', 'n', 'nope', 'negative']

# collect the major structural info for the scene
POVCharacter = input("What's the name of the point-of-view character?\n")
goal = input('What is ' + POVCharacter + "'s goal during this scene?\n")

adversaryYesNo = input('Will another person get in ' + POVCharacter + "'s way?")
while adversaryYesNo not in affirmativeResponses and adversaryYesNo not in negativeResponses:
    adversaryYesNo = input("Please respond with 'yes' or 'no'. Will another person get in " + POVCharacter + "'s way?\n")
if adversaryYesNo in affirmativeResponses:
    adversary = input('Who will it be?\n')
elif adversaryYesNo in negativeResponses:
    obstacle = input('What will get in their way instead?\n')

# print the scene plan
print('Point of view character:', POVCharacter)
print(POVCharacter, "'s goal:", goal)
if adversaryYesNo in affirmativeResponses:
    print(adversary, 'will get in ' + POVCharacter + "'s way.")
else:
    print(obstacle + ' will get in ' + POVCharacter + "'s way.")

# This was my first go at dealing with unexpected user responses.
# I expect the flow is klunky and inelegant. I'd like to improve it.
# Next action: make a program that uses a self referential function in place of the while loop
