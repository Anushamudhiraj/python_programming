'''
1.Guess the game:


import random
num=random.randint(1,100)     #randint(sv,ev)
count=0

while True:
    count+=1
    guess=int(input('enter the number: '))

    if guess==num:
        print('your guess is correct!!')
        print(f'you gussed in {count} attempts. ')
        break
    
    elif guess>num:
        print('Guess lower')

    else:
        print('Guess higher')

####################################################################

2.to get the following output:
s='Independence Day'
out='ecnednepednI yaD'


s='Independence Day'
s=s.split()  #['Independence','Day']
out=''

for i in s:
    out=out+i[::-1]+' '

print(out)

####################################################################

3.extract the words from the string without split():
s='we need holiday'

s='we need holiday'
res=[]
word=''

for i in s:
    if i!=' ':
        word+=i

    else:
        res.append(word)
        word=''

res.append(word)
print(res)

'''








































    
