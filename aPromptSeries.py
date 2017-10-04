# part 2: a prompt series
import random

# part 2.1: display three variations on a single prompt
# part 2.1.0
nounPhrases = ['a cup', 'a scarf', 'an animal', 'something lost', 'a child']
nounPhraseSeries = random.sample(nounPhrases, 3)
# print('Write a sentence about', nounPhraseSeries[0] + '.')
# print('Write a sentence about', nounPhraseSeries[1] + '.')
# print('Write a sentence about', nounPhraseSeries[2] + '.')
# that works, but i'd like to automate the sieries-ness more.
# i feel like i want a loop, but i also remember something about "loops are bad".
# i think go ahead and try it as a loop if you want, so you know what you're trying to do,
#    then go through this essay to find alternatives.
#    https://medium.com/python-pandemonium/never-write-for-loops-again-91a5a4c84baf

# part 2.1.1
#like before, but with a while loop

# numberOfPrompts = 0
# while numberOfPrompts < 3:
#    print ('Write a sentence about', nounPhraseSeries[numberOfPrompts - 1] + '.')
#    numberOfPrompts += 1
# part 2.1.1 complete

#part 2.1.2
#like before, but with a for loop instead of a while loop

for nounPhraseSeriesElement in nounPhraseSeries:
    print('Write a sentence about', nounPhraseSeriesElement + '.')


# part 2.2: display two prompts that build on each other
# "Describe [a noun phrase] from the perspective of someone who feels [emotion]."
# "Something happens that makes the person feel [new emotion] instead of [old emotion]. What new thing do they notice about [the previous noun phrase]?"

emotions = ['serene', 'agitated', 'excited', 'regretful', 'angry']
nounPhraseA = random.choice(nounPhrases)
emotionsSeries = random.sample(emotions, 2)
print('Describe', nounPhraseA, 'from the perspective of someone who feels', emotionsSeries[0] + '.')
print('Something happens that makes the person feel', emotionsSeries[1], 'instead of', emotionsSeries[0], '. What new thing do they notice about', nounPhraseA + '?')

# problem: i need to switch 'a' to 'the' in the second prompt. i think this kind of thing will happen a lot in even the most basic series.
# i think i'll declare this exercise complete, and make combination rules the next exercise.
# part 2.2 complete

# part 2.3.1: convert atomic nouns to noun phrases using a for loop

atomicNouns = ['table', 'pen', 'apple', 'mask', 'letter']

# indefiniteNounPhrases = []
#definiteNounPhrases = []
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

# for atomicNounsElement in atomicNouns:
#    if atomicNounsElement[0] in consonants:
#        indefiniteNounPhrases.append('a ' + atomicNounsElement)
#    else:
#        indefiniteNounPhrases.append('an ' + atomicNounsElement)

# for atomicNounsElement in atomicNouns:
#    definiteNounPhrases.append('the ' + atomicNounsElement)



# print('The indefinite noun phrases are', indefiniteNounPhrases)
# print('The definite noun phrases are', definiteNounPhrases)

# part 2.3.2: convert atomic nouns to noun phrases using list comprehension

# definiteNounPhrases = ['the ' + atomicNounsElement for atomicNounsElement in atomicNouns]
# print(definiteNounPhrases)

# indefiniteNounPhrases = ['a ' + atomicNounsElement if atomicNounsElement[0] in consonants else 'an ' + atomicNounsElement for atomicNounsElement in atomicNouns]
# print(indefiniteNounPhrases)

# part 2.3.3: make a function that converts atomic nouns to noun phrases (actually a pair of functions)

definiteNounPhrase = lambda x: 'the ' + x
print(definiteNounPhrase('clock'))

indefiniteNounPhrase = lambda x: 'a ' + x if x[0] in consonants else 'an ' + x
print(indefiniteNounPhrase('key'))
print(indefiniteNounPhrase('elephant'))

# 2.4 display two prompts that build on each other and use an indefinite to definite article switch.
# "Describe [a noun phrase] from the perspective of someone who feels [emotion]."
# "Something happens that makes the person feel [new emotion] instead of [old emotion]. What new thing do they notice about [the previous noun phrase]?"

atomicNoun1 = random.choice(atomicNouns)
print('Describe', indefiniteNounPhrase(atomicNoun1), 'from the perspective of someone who feels', emotionsSeries[0] + '.')
print('Something happens that makes the person feel', emotionsSeries[1], 'instead of', emotionsSeries[0], '. What new thing do they notice about', definiteNounPhrase(atomicNoun1) + '?')
