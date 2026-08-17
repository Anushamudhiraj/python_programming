'''
1.rigth aligned triangle:

*
**
***
****
*****

n=int(input('enter the number: '))
for i in range(1,n+1):
    print('* '*i)

###########################################

2.left aligned triangle:

    *
   **
  ***
 ****
*****
   

n=int(input('enter the number: '))
for i in range(1,n+1):
    print(' '*(n-i) + ' *'*i)

###########################################

3.reverse of a right aligned triangle:

*****
****
***
**
*

n=int(input('enter the number: '))
for i in range(1,n+1):
    print('* '*((n-i)+1))

or

n=int(input('enter the number: '))
for i in range(n,0,-1):
    print('* '*i)

##########################################

4.reverse of a left aligned triangle:

*****
 ****
  ***
   **
    *

    
n=int(input('enter the number:'))
for i in range(1,n+1):
    print(' '*(i-1) + '*'*((n-i)+1))

##########################################

5. Pyramid of a triangle:

      *
     ***
    *****
   *******
  *********

n=int(input('enter the number:'))
for i in range(1,n+1):
    print(' '*(n-i) + '*'*((2*i)-1))

##########################################


6. Reverse Pyramid of a triangle:

  *********
   *******
    *****
     ***
      *

n=int(input('enter the number:'))
for i in range(1,n+1):
    print(' '*(i-1) + '*'*(2*(n-i)+1))

##########################################

7. Diamond --->pyramid + Inverted pyramid (with no duplicate row)

      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *

n=int(input('enter the number:'))
for i in range(1,n+1):
    print(' '*(n-i) + '*'*((2*i)-1))

for i in range(n-1,0,-1):
    print(' '*(n-i) + '*'*((2*i)-1))

##########################################

8. Only the boundary of diamond:

        *
       * *
      *   *
     *     *
    *       *
     *     *
      *   *
       * *
        *

n=int(input('enter the number:'))
for i in range(1,n+1):
    if i==1:
        print(' '*(n-i) + '*')
    else:
        print(' '*(n-i) + '*' + ' '*((2*i)-3) + '*')

for i in range(n-1,0,-1):
    if i==1:
        print(' '*(n-i) + '*')
    else:
        print(' '*(n-i) + '*' + ' '*((2*i)-3) + '*')

#############################################

8.half reverse of diamond:

  *********
   *******
    *****
     ***
      *
     ***
    *****
   *******
  *********
        
n=int(input('enter the number:'))
for i in range(n,0,-1):
    print(' '*(n-i) + '*'*((2*i)-1))

for i in range(2,n+1):
    print(' '*(n-i) + '*'*((2*i)-1))


#############################################

9.left based triangle:

*
**
***
****
*****
****
***
**
*
       
n=int(input('enter the number:'))
for i in range(1,n+1):
    print('*'*i)

for i in range(n-1,0,-1):
    print('*'*i)

#############################################

10.hollow right angled triangle:

*
**
* *
*  *
*****


n=int(input('enter the number:'))
for i in range(1,n+1):
    if i==1:
        print('*')
    elif i==n:
        print('*'*n)
    else:
        print('*' + ' '*(i-2) + '*')

#############################################

11.hollow pyramid:
           *
          * *
         *   *
        *     *
       *********

n=int(input('enter the number:'))
for i in range(1,n+1):
    if i==1:
        print(' '*(n-i) + '*')
    elif i==n:
        print('*'*((2*n)-1))
    else:
        print(' '*(n-i) + '*' + ' '*((2*i)-3) + '*')

'''

       
    
   





























