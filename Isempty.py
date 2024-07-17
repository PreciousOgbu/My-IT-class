# A function that takes a parameter and checks if its empty 

def is_empty(empty):
    user_input = input("Enter anything: ")
    if (empty) == 0:
        return True
    else:
        return False
    

print(is_empty('hi'))
