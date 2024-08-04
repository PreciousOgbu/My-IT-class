# try:
#     print(10 + '5')
# except:
#     print('TypeError: cannot convert integer to a string')


# try:
#     name = input('Enter your name: ')
#     year_of_birth = int(input('Enter your year of birth: '))
#     age = 2024 - year_of_birth

#     print(f'Hello {name}, you are {age} years old')
    

# except TypeError:
#     print('Type Error occurred')

# except ValueError:
#     print('Invalid Year of Birth')

# except ZeroDivisionError:
#     print('ZeroDivision Error occurred')




# try:
#     name = "Presh"
#     print(name)

# except NameError:
#     print('Name is not defined')


# finally:
#     print("Finally, block executed")






try:
    #name = 'Presh'
    #name = input("Enter your name: ")
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter second number: "))

    print(num_1 / num_2)

    # print(name)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except Exception as e:
    print(e)


finally:
    print("Finally, block executed")




