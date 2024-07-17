# A function to remove set 




def remove_item():
     State_Capitals = {"Umuahia", "Yola", "Uyo", 
                  "Awka", "Bauchi", "Calabar", 
                    "Asaba", "Markudi", 
                  "Enugu", "Jos"}
     
     while True:
          user_input = input("Enter a state capital to remove (or 'quit' to stop): ")

          if user_input.lower() == 'quit':
               break
          if user_input.capitalize() in State_Capitals:
           State_Capitals.remove(user_input.capitalize())
           (f'Removed {user_input.capitalize()}. Remaining items: {State_Capitals}')

          else:
              print(f'{user_input.capitalize()} not found in the set.')

              if not State_Capitals:
                  print(f'Set  is empty')


print(remove_item())