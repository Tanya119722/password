password = 'a123456'
i = 3
while True: 
    pws=input('pls input the password:')
    if pws == 'a123456':
        print('the password is correct')
        break
    else:
        i = i - 1 
        print('the password is wrong, you have', i , 'time(s) left')
        if i == 0:
            break