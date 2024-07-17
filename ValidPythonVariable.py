
# Write a function to check if a varaible is a valid python varable


def check_valid_variable():


    invalid_variable = ('@', '?', '!', '#', '%', '$', '^', '&', '*', '()', ")", '-', '=', '+', '[]', ']', ";", '"', '|', '<')
    

    while True:
        valid_variable = input("Enter Python varaible or ('exit' to finish): ")

        if valid_variable == 'exit':
            break

        elif valid_variable .startswith ('_') or valid_variable [0] .isalpha():
            return "This is a valid python variable"

        
        elif valid_variable[0] .startswith(invalid_variable) or valid_variable in invalid_variable:
            return "Variable cannot start with symbol"
        
        elif  valid_variable[0] .isdigit():
            return "Variable cannot start with a number"
        
        #elif  valid_variable[0] .isalpha():
            return "This is a valid python variable"
        #elif valid_variable in invalid_variable:
            return "Python variable cannot start with symbol/sign"
        
        continue
    


# def to_exit_program():
#     response = input("Do you want to exit the program (Yes/No): ")
#     if response.capitalize() == "Yes":
#         return True
#     else:
#         return False
    

def main_loop():
    while True:
        output = check_valid_variable()
        if output is None:
            # if to_exit_program():
                break
            

        else:
            print(output)
main_loop()


