'''
#1. library charges:

d=int(input('enter the no.of days late:'))

if d<=5:
    fine=d*2
    print('fine is',fine)
elif d<=10:
    fine=d*5
    print('fine is',fine)
elif d<=15:
    fine=d*10
    print('fine is',fine)
else:
    fine=d*20
    print('fine is',fine)
    print('Warning letter issue')



#2.Game scoring system:

kills=int(input('enter no.of kills:'))
deaths=int(input('enter no.of deaths:'))

if kills<5:
    score=kills*100

elif kills<=10:
    score=(kills*150)+500

else:
    score=(kills*200)+1500

if deaths>kills:
    score=score/2

print('Final score is:',score)

'''
