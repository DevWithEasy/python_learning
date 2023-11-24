import pprint as pp

string = 'Bangladesh is a small country.'

letters = {}

for i in string :
    letters.setdefault(i,0)
    letters[i] = letters[i]+1

pp.pprint(letters)