'''
1.find length of collection without len():

col=eval(input('ener the values:'))
count=0
i=0

while i<len(col):
    count+=1
    i+=1
print(count)

====================================================

2.Reverse of a string without slicing:


s=input('enter the string:')
rev=''
i=0

while i<len(s):
    rev=s[i] + rev
    i+=1

print(rev)

====================================================


3.to join elements of a list to make a string without split():


l=eval(input('enter the list'))
res=''
i=0

while i<len(l):
    res=res+l[i]+' '    #res=res+str(l[i])+'  ' --->for int values in list
    i+=1
print(res)

==========================================================
4.wap that keeps asking the user for a number until they enter 0, then print the summ of all entered numbers:



sum=0
n=int(input('enter the number:'))

while n!=0:
    sum+=n
    n=int(input('enter the number:'))
print(f'sum is {sum}')

==========================================================


5.sum of digits until single digit:
    eg: 9876--->9+8+7+6+5=35  --->3+5=8 (single digit)


n=int(input('enter the number'))
sums=0

while n>=10:
    while n>0:    #i!=0:
        sums=sums+(n%10)
        n=n//10
    n=sums
print(n)

=================================================================
6.toggle a string ---> uppercase to lowercase and lowercase to uppercase:


s=input('enter the string: ')
out=''
for i in s:
    if 'a'<= i <='z':
        out+=chr(ord(i)-32)

    elif 'A'<= i <='Z':
        out+=chr(ord(i)+32)

    else:
        out+=out
print(out)

'''
    
    
    
