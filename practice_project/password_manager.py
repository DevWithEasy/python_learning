password_manager = {
    'robiul' : 123456,
    'rubel' : 1234567,
    'rasel' : 12345678
}

match = False
x = 0

print('Enter your name :')

while x < 5 :
    
    name = input()

    if name in password_manager :
        for i in range(0,3):
            print('Enter your password :')
            password = int(input())
            if password in password_manager.values() :
                match = True
                print('Congratulations!')
                break
            else:
                print(f'Enter correct password.you have {2-1} chances.')
    else:
        print('There is no such name in password_manager')

    x = x+1
    if match :
        break

