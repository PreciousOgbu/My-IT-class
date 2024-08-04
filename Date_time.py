# Create a function that greets according to the time you run the program

from datetime import datetime

def greet_current_time():

    name = input("What is your name: ")
    current_time = datetime.now().hour

    if current_time < 12:
        print(f"Good morning {name}!")
    
    elif current_time < 17:
        print(f'Good afternoon {name}!')

    elif current_time < 22:
        print(f'Good evening {name}')

    else: 
        print(f"Go and sleep {name}, it's late")

    




greet_current_time()


