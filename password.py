password = 'a123456'
i = 3
while i > 0: 
    i = i - 1
    pws=input('pls input the password:')
    if pws == 'a123456':
        print('the password is correct')
        break
    else:
        print('the password is wrong')
        if i > 0:
        	print('you have', i ,'time(s) left')
        else:
        	print('no chance to try, your account will be locked')

          
