# A funtion named Print_list that allows a user to print his list once the item is up to 5

def print_list():
    my_list = []

    while True:
        item = input("Enter an item to add to the list (or  stop to finish): ").strip().capitalize()
        if item.lower() == 'stop':
            break
        elif item == " ":
          print("You cannot add empty text to the list") 
          continue
        elif item in my_list:
            print(f"{item} already exists in the list. It will not be added")
            continue

        else:
            my_list.append(item)
            print(f"Item added: {item}")
        
        if len(my_list) >= 5:
            print("Here is your list: ")
            for i, item in enumerate(my_list, start=1):
                print(f'{i}. {item}')
                continue
            return my_list

        # else:
        #     print("Goodbye, below is your list: ")
        #     print(my_list)
        #     return my_list
        

print_list()