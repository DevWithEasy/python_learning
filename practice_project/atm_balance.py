user_list = [
    {'id': 1, 'name': 'Alice', 'password': 123456, 'balance' : 5000},
    {'id': 2, 'name': 'Bob', 'password': 1234567, 'balance' : 5000},
    {'id': 3, 'name': 'Charlie', 'password': 1234568, 'balance' : 5000},
]

# user = [user for user in user_list if user['name'] == 'Alice']

# print([user[0]])

logged_in = False
user = {}

while True:
    print('Wellcome to Banking')
    print(' 1.Login')
    print(' 2.Check balance')
    print(' 3.Cash widrow')
    print(' 4.Account details')
    print(' 5.Logout')

    print('\nPlease enter your : ')
    i = input('')

    if i == '1' : 
        name = input('Please enter your name : ')

        user = [user for user in user_list if user['name'] == name]

        if user :
            i = 0
            for i in range(0,3) :
                password = input('Enter your password')
            
                if int(password) == user[0]['password']:
                    logged_in = True
                    user = user[0]
                    print(f'Successfully logged.')
                else:
                    print(f'Wrong password.Try again {2-i}')
            
        else :
            print('Please enter correct name')
        # print(user)
    
    if i == 2 :
        print(user)

    if i == '5' :
        break