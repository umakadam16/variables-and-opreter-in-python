
a = 20
b = 16
c = 30

#Remove comments from the bottom lines to take input from the user
a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: '))

#Semi-perimeter calculation
s = (a + b + c) / 2

#Area calculation
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

#Print the output
print('The area of the triangle is %0.2f' %area)