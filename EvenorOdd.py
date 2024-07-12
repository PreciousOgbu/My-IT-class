# Write a function to check if a number is even or odd


def get_user_input():
    return int(input("Enter a number (or 0 to quit): "))

def check_even_or_odd():
    num = get_user_input()
    if num == 0:  
        return None
    elif num % 2 == 0:
        return f"{num} is an even number."
    else: 
        return f'{num} is an odd number'
    
def goodbye_message():
        print("Goodbye!")

def confirm_continue():
     response = input('Zero is invalid, Do you want to continue? (Yes/No): ')
     if response.capitalize()== 'Yes':
          return True
     else:
          return False
     
def main_loop():
     while True:
          result = check_even_or_odd()
          if result is None:
               if confirm_continue():
                    continue
               else:
                    goodbye_message()
                    break
          else:
               print(result)


main_loop()

