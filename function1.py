
def add_number():
    num_one = int(input('Enter the first number: '))
    num_two = int(input('Enter the second number: '))
    sum = num_one + num_two
    return sum


def sub_number():
    num_one  = int(input('Enter the first number: '))
    num_two = int(input('Enter the second number: '))
    difference = num_one - num_two
    return difference


def mul_number():
    num_one = int(input('Enter the first number: '))
    num_two = int(input('Enter the second number: '))
    product = num_one * num_two
    return product


def div_number():
    num_one = int(input('Enter the first number: '))
    num_two = int(input('Enter the second number: '))
    quotient = num_one / num_two
    return quotient

def breakpoint():
    print(" Are you sure you want to exit?...")
    print('Yes, exit\nNo to continue ')
    choice = input('Enter your choice: ').capitalize()
    if choice == 'Yes':
        exit()


def main():
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    while True:
        choice = int(input('Enter your choice: '))
        if choice > 4:
            print("Invalid Choice")
            break
        if choice == 0:
         breakpoint()
            
            # else:
            #     continue
            #break
            #exit()

        if choice == 1:
            print(add_number())

        elif choice == 2:
            print(sub_number())

        elif choice ==3:
            print(mul_number())

        elif choice == 4:
            print(div_number())


main()
