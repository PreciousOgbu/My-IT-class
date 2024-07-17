# Declare a function  named capitalized_items

def capitalized_items():


 items =[]

while True:
  item = input("Enter an item (or 'stop' to finish): ").strip().capitalize()\
  
  if item.lower() == 'stop':
   break
 items.append(item)
  return items