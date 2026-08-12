
'''

1.Write a program that takes three sides of a triangle as input and
determines whether the triangle is equilateral, isosceles, or scalene.
Additionally, check if the sides satisfy the triangle inequality
theorem; if not, print "Not a valid triangle".

##a=int(input('Enter the first side: '))
##b=int(input('Enter the second side: '))
##c=int(input('Enter the third side: '))
##if a+b>c and b+c>a and c+a>b:
##    if a==b==c:
##        print('Equilateral triangle')
##    elif a==b or b==c or c==a:
##        print('Isoceles triangle')
##    else:
##        print('Scalene triangle')
##else:
##    print('Not a valid triangle')

=======================================================================================
2.Write a program that takes two numbers and an operator (+, -, *, /, %)
as input and performs the corresponding arithmetic operation.
Handle division by zero gracefully by printing "Cannot divide by zero".
If an invalid operator is entered, print "Invalid operator".

##num1=int(input('Enter number1: '))
##num2=int(input('Enter number2: '))
##op=input('Enter the operator(+,-,*,%,/): ')
##
##if op=='+':
##    print(num1+num2)
##elif op=='-':
##    print(num1-num2)
##elif op=='*':
##    print(num1*num2)
##elif op=='/':
##    if num2==0:
##        print('Cannot divide by zero')
##    else:
##        print(num1/num2)
##elif op=='%':
##    if num2==0:
##        print('Cannot divide by zero')
##    else:
##        print(num1%num2)
##else:
##    print('Invalid operator')

========================================================================

3.Take the lengths of three sides of a triangle. Determine if the
triangle is acute, right, or obtuse using the Pythagorean relation
(after checking validity). For a triangle with sides a â‰¤ b â‰¤ c:
   Â· If aÂ² + bÂ² == cÂ² â†’ right
   Â· If aÂ² + bÂ² > cÂ² â†’ acute
   Â· If aÂ² + bÂ² < cÂ² â†’ obtuse

##a=int(input('Enter the first side: '))
##b=int(input('Enter the second side: '))
##c=int(input('Enter the third side: '))
##sides=[a,b,c]
##sides.sort()
##a,b,c=sides[0],sides[1],sides[2]
##if a+b>c:
##    if (a*a)+(b*b)==(c*c):
##        print('Right angle triangle')
##    elif (a*a)+(b*b)>(c*c):
##        print('acute angle triangle')
##    else:
##        print('obtuse angle triangle')
##else:
##    print('Not a valid triangle')

=================================================================================

4.Take a 3-digit number and print its digits in reverse order without using
string slicing or loops (use arithmetic and conditionals only). Also check
if the reversed number equals the original (palindrome)

n=int(input('Enter the number: '))
ones=n%10
tens=(n//10)%10
hund=n//100
rev=ones*100+tens*10+hund

if rev==n:
    print('pallindrome')
else:
    print('Not a pallindrome')

===================================================================================

5. second greatest among three numbers:


a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number:'))

if (a<b and a>c) or (a<c and a>b):
    print(f'{a} is second greatest')

elif (b<a and b>c) or (b<c and b>a):
    print(f'{b} is second greatest')

else:
    print(f'{c} is second greatest')

'''


