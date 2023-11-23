while True:
    print('Enter your email:')
    email = input()
    if email != 'admin@mail.com':
        continue
    print('Enter your password')
    password = input()
    if password != 'admin':
        continue
    else:
        print(f'Hello {email}.you are can entry the game.')
        break