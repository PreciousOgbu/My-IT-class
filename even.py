def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False

while True:
    num = int(input('Add a number: '))
    if num == 0:
        break
    print(is_even(num))

 