'''#1. hotel room booking system:
  !. single roon: 2000
 !!. double room: 3000
!!!. suite: 5000

if stay for 5 days or more discount is 10%,
if stay for 10 days or more discount is 20%,
if is a member then discount of 5% after all discounts,
    calculate the total bill.

print('1=single room 2000/night')
print('2=double room 3000/night')
print('3=suite 5000/night')
r=int(input('enter room type:'))
n=int(input('enter no.of days to stay:'))
m=input('are you a member(y/n):')


if r==1:
    bill=n*2000
    if n>=10:
        bill=bill*0.8
    elif n>=5:
        bill=bill*0.9
        
elif r==2:
    bill=n*3000
    if n>=10:
        bill=bill*0.8
    elif n>=5:
        bill=bill*0.9
        
elif r==3:
    bill=n*5000
    if n>=10:
        bill=bill*0.8
    elif n>=5:
        bill=bill*0.9
else:
    print('Invalid room')

if m=='y' or m=='Y':
    bill=bill*0.95
    print(f'Total bill is {bill}')
    
else:
    print(f'Total bill is {bill}')
'''

''' simple ATM transaction,start with a balance of 5000.
Ask the user for options:1-withdraw, 2-deposite, 3-check balance .
bal=5000
print('1- withdraw, 2- Deposit, 3- Check balance')
option=int(input('enter the option:'))

if option==1:
    amt=int(input('enter the amount to withdraw:'))
    if amt > bal:
        print('insufficient funds')
    else:
        bal=bal-amt
        print('available balance is:',bal)

elif option==2:
    amt=int(input('enter the amount to deposit:'))
    bal=bal+amt
    print('available balance is:',bal)
    
elif option==3:
    print(f'the total balance is {bal}.')
    
else:
    print('Invalid option')

'''
    
           

        










































    
