'''
1. Print the middle character of a string if it is Odd length, or print first and last characters



s=input('enter the string: ')
if len(s)%2==0:
    print(s[0]+s[-1])

else:
    print(s[len(s)//2])  #print(chr(ord(s[len(s)//2])))
 ==============================================================================   

2.hostel food menu:


food={'sunday':'chicken','monday':'sambar','tuesday':'egg','wednesday':'prawns',
      'thursday':'lady finger','friday':'mutton','saturday':'fish'}

day=input('enter the day:')

if day in food:
    if day=='sunday':
        print(f'the food is {food[day]}')

    elif day=='monday':
        print(f'the food is {food[day]}')

    elif day=='tuesday':
        print(f'the food is {food[day]}')

    elif day=='wednesday':
        print(f'the food is {food[day]}')

    elif day=='thursday':
        print(f'the food is {food[day]}')

    elif day=='friday':
        print(f'the food is {food[day]}')

    elif day=='saturday':
        print(f'the food is {food[day]}')

else:
    print('Invalid day')

==========================================================================


3. calculate the total bill of the user based on her shopping

bill=2000 --->10%
bill=3500 --->20%
bill=5000 --->30%


bill=int(input('enter the amount of bill:'))

if bill>=5000:
    bill=bill*0.7

elif bill>=3500:
    bill=bill*0.8

elif bill>=2000:
    bill=bill*0.9

print('the total bill is',bill)

===========================================================================

4.  Stimulate rock paper scissor game:

    

import random
user=input('enter your choice(stone, paper, scissor):')
options=['stone','paper','scissor']

for i in range(0,6):
    comp=random.choice(options)
    print('computer choose:',comp)

    if user==comp:
        print('Match tie')

    elif user=='stone':
        if comp=='scissor':
            print('you won the match')

        else:
            print('computer won the match')

    elif user=='paper':
        if comp=='stone':
            print('you won the match')

        else:
            print('computer won the match')

    elif user=='scissor':
        if comp=='paper':
            print('you won the match')

        else:
            print('computer won the match')

    else:
        print('Invalid input')
'''











