import os

# # location = '/test.txt'

# file = open('./test.txt', 'r')
# txt = file.readlines()
# print(txt)
# print(type(txt))
# file.close()


# with open('./test.txt', 'r') as file:
#     txt = file.readlines()
#     print(txt)
#     print(type(txt))

with open('./test.txt', 'a') as file:
    file.write("This is a new line")
    



# with open('./tesst.txt', 'w') as file:
#     file.write("This is a new line in tests.text")

# try:
#     os.remove('./tesst.txt')

# except FileNotFoundError: 
#     print("File does not exist")


if os.path.exists('./tesst.txt'):
    print("Deleting file.........")
    os.remove('./tesst.txt')
    print("File deleted succesfully")

else:
    print("File does not exist")