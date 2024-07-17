# # Function

def greeting():
    print("Hello world")
    print("Hello, Good afternoon")

#greeting()

def main():
   greeting()
   print("Hello from main function")

main()

# def get_fullname():
#     first_name= input('Enter first name: ')
#     last_name = input('Enter your last name: ')
#     full_name = first_name + " " + last_name
#     print(full_name)

# get_fullname()

def add_num():
    num_1 = int(input('Enter the first number: '))
    num_2 = int(input('Enter the second number: '))
    sum = num_1 + num_2
    print(sum)
    return num_1 * 10

result = add_num()
result = result + 500
print (result)


# def multiply():
#     for i in range(15):
# #         print(f'{i} * {i}= {i * i}')

# # multiply()

# # RETURNING A VALUE TO A FUNCTION

def add_num():
    num_1 = int(input('Enter the first number: '))
    num_2 = int(input('Enter the second number: '))
    sum = num_1 + num_2
    return sum
    

result = add_num() + 500
result = result  + 500
print(result)



