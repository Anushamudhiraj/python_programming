'''
1.petrol pump fuel filling :vehicle arrive one by one at a petrol station .
record fuel filled for each vehicle until the total fuel sold reaches 500 litres.


reserve=500
res=[]

while reserve>0:
    fuel=int(input('enter the fuel:'))
    reserve=reserve-fuel
    if reserve>=0:
        res.append(fuel)
print(res)

=================================================================================

2. hospital patient temperature check:
 a hospital records temp of patients entering the emergency ward,
 stop when a patient with temp above 104^F if found and display the patient count checked before that.


temp=int(input('enter the temp in ^F:'))
count=0

while temp<104:
    temp=int(input('enter the temp in ^F:'))    #updation
    count=count+1
print(count)

==================================================================================

3. Prime number or not:


n=int(input("enter the number;"))
i=2
count=0

while i<=n//2:    #n//2 is to reduce the no.of iterations
    if n%i==0:
       count+=1
    i+=1

if count>=1:
    print('not prime')
else:
    print('prime')

==================================================================================


4. login attempts system:

oun='anusha'
passward=12345
i=0

while i<4:
    nun=input('enter the username:')
    np=int(input('enter the passward:'))
    if oun==nun:
        if passward==np:
           print('login...!!!')
           break
        else:
            print('Invalid passward')

    else:
        print('Invalid username')

    i+=1

===============================================================================

5. find the specified in the list:


l=[1,3,23,4,3,5,6,44,66,52]
n=int(input('enter the element:'))

for i in l:
    if i==n:
        print('element found')
        break
print('element not found')

===============================================================================

6.print numbers from 1-30 but not mul of 3:


for i in range(1,31):
    if i%3==0:
        continue
    print(i)

==============================================================================

7.find HCF of two numbers:


n1=int(input('enter the first number.'))
n2=int(input('enter the second number.'))

smallest=n1 if n1<n2 else n2     #ternary operation : TSB if cond else FSB    

for i in range(smallest,1-1,-1):
    if n1%i==0 and n2%i==0:
        hcf=i
        break
print(hcf)

===========================================================================

8.find LCM of two numbers:
'''

n1=int(input('enter the first number.'))
n2=int(input('enter the second number.'))

largest=n1 if n1>n2 else n2     #ternary operation : TSB if cond else FSB    

for i in range(largest,1-1,-1):
    if n1%i==0 or n2%i==0:
        lcm=i
       
print(lcm)































           
    
