# Check if a variable is a valid python variable

# def check_valid_variable(variable):
#     if variable.startswith("_"):
#         return True
#     if  variable[0]. isdigit():
#        # return True
#         return "Variable doesn't start with a number"
    
#     if variable .startswith('@'):
#         return "Varaible name doesn't start with @"
    
    

#     return variable

# print(check_valid_variable('name'))



def check_valid_variable_2(variable):
    if variable.isidentifier():
        return True
    return False

while True:
    variable = input("Enter a variable name: ")
    if variable == 'exit':
        break
    if check_valid_variable_2(variable):
        print(f'The variable {variable} is valid.')
        break
    else:
        print(f'The variable {variable} is not valid')