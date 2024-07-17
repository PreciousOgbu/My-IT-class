# # Set

st = {"item1", "item2", "item3"}

fruits= {"apple", "orange", "banana", "pineapple", 'banana' }
print(len(fruits))
print(fruits)


print("Does banana exist in fruit set", 'banana' in fruits)

# def check_items(item):
#    return item

# while True:
#     item = input("Enter the name of the item you want to check: ")
#     if item in fruits:
#      check_items(item)
#      print(f'{item} is in fruit set')
#      break
#     else:
#         print(f'{item} is not in fruit set. Please try again.')



def update_set(item =[]):
    names = set()
    names.update(item)
    return names

# lst = ["Hello", "Chief"]
# print(update_set(lst))


set_list =  {"item1", "item2", "item3"}
set_list.remove("item1")
print(set_list)


fruits= {"apple", "orange", "banana", "pineapple", 'banana' }
# returned_item = fruits.pop()
# print(returned_item)
#del fruits
#print (fruits)
fruits.remove('apple')
print(fruits)
