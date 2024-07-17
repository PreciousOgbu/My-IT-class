# Declare a function named capitalize_items

def capitalize_items(items_list):
    capitalized_list =[item.strip().capitalize() for item in items_list] 
    return capitalized_list


items = []
while True:
    item = input("Enter an item (or 'stop' to finish): ")

    if item.lower()== 'stop':
        break
    items.append(item)


capitalized_items =capitalize_items(items)

print("Here are your capitalized items: ")

for i, item in enumerate (capitalized_items, start=1):
    print(f'{i}.{item}')

print(f'Your capitalized list is: ', capitalized_items)