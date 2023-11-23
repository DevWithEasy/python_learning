import random as r

secret = r.randint(1,10)
flag = False

def game_func(guese_age,secret):
    if guese_age < secret :
        return 'Too low !'
    elif guese_age > secret :
        return 'Too high !'
    else :
        return 'CORRECT'

for i in range(1,6):
    print(f'Take a guese. You have {6-i} chance only')
    guese_number = int(input())
    if game_func(guese_number,secret) == 'CORRECT' :
        print('YOU WON THE GAME.')
        flag = True
        break
if not flag :
    print('You lose the game.')