# part 1: a single prompt

# part 1.0: display "Write a sentence."
print('PART 1.0')
print('Write a sentence.')
# part 1.0 complete

# part 1.1: display "Write a sentence about [a noun phrase]."
import random  # noqa
print('PART 1.1')
nounPhrases = ['a dog', 'a lamp', 'an orange peel']
# print(nounPhrases)  # just to test that the list exists. it does.
print('Write a sentence about', random.choice(nounPhrases) + '.')
# part 1.1 complete

# part 1.2.1: display "Write a sentence about [a noun phrase] and [another noun phrase]."
# don't need to import random 'cause I did it in the last section.
# print(PART 1.2)
# firstNoun = random.choice(nounPhrases)
# nounPhrases.remove(firstNoun)
# secondNoun = random.choice(nounPhrases)
# print('Write a sentence about', firstNoun, 'and', secondNoun + '.')
#  problem: this seems kinda klunky? i don't like that it permanently removes firstNoun from the list.
#  i could add firstNoun back into the list immediately afterward, but that still feels bad.

#  part 1.2.2 take 2: same thing but less klunky.
#  commenting out version 1.2.1
print('PART 1.2')
nounsForFirstSentence = random.sample(nounPhrases, 2)
print('Write a sentence about', nounsForFirstSentence[0], 'and', nounsForFirstSentence[1] + '.')
# part 1.2 complete

# part 1.3: display "Describe [a noun phrase] from the perspective of someone who feels [emotion]."
# already created the list nounPhrases in part 1.1, so don't need to do it here.
print('PART 1.3')
emotions = ['excited', 'anxious', 'regretful']
print('Describe', random.choice(nounPhrases), 'from the perspective of someone who feels', random.choice(emotions) + '.')
