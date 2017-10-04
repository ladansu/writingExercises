# 3.1 Store the response to 'Joe wants a cup of tea. Mary wants something that
# conflicts with that. What is it?', then ask 'Why does Mary want
# [the stored response]?'

conflict = input('Joe wants a cup of tea. Mary wants something that conflicts with that. What is it? \n')
motivation = input('Why does Mary want '+ conflict + '?\n')
print('Mary wants', conflict, 'because', motivation + '.')
