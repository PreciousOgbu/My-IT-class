#Get two numbers from a user, using input method, prompt if A>B 

A= int(input('Enter the first number (A): '))
B= int(input('Enter the second number(B): '))

if A > B:
    print(f'{A} > {B}')
elif A < B:
    print(f'{A} < {B}')

else:
    print(f'{A}  = {B}')


