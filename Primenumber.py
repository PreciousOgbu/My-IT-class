# Write a function that checks if a number is prime or not

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    #if n == 2 or n == 3: #or n == 5:
        return True
    if n % 2 == 0 or n % 3 ==0: #or n %5 == 0:
        return False
    if n == 5 or n == 7:
        return True
    i = 7
    while i * i <= n:
        if n % i == 0 or n % (i +2) == 0: #or  n % (i + 4) == 0:
            return False
        i += 6
    # for i in range(7, int(n**0.5)+ 1, 2):
    #     if n % i == 0:
    #         return False
        return True
    
while True:
    num = int(input("Enter a number (or 0 to quit): "))

    if num == 0:
        print("Goodbye!")
        break

    if is_prime(num):
        print(f'{num} is a prime number')

    else:
        print(f"{num} is not a prime number")