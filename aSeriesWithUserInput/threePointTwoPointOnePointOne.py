# print "that's a valid affirmative response" or "that's a valid negative response"
# and re-propt when given an invalid response

affirmativeResponses = ['yes', 'yep', 'y', 'affirmative']
negativeResponses = ['no', 'nope', 'n', 'negative']

def response():
    return input("What's your response?")


def validResponseChecker(x):
     if (x) in affirmativeResponses:
         print("That's a valid affirmative response!")
         return "yes"
     elif (x) in negativeResponses:
         print("That's a valid negative response!")
         return "no"
     else:
         print('Please respond "yes" or "no".')
         return validResponseChecker(response())

print(validResponseChecker(response()))
