my_dict = {
    "name": 'Presh', 
    'lastname': 'Daniel',
    'skills': ['html', 'java', 'javascript', 'typescript', 'Python'],
     'address': {
         'street':  '123 Main St', 
         'city' : 'New York', 
         "state": 'NY',
         'zip code': 10001 
     } 
}
print((my_dict))
print((my_dict['address'])['zip code'])
print((my_dict['skills'][1]))
print(len(my_dict))

if my_dict.get('name'):
    print('Name exist in dictionary')
else:
    print("Name does not exist in dictionary")

# Replacing an item
# my_dict['name'] = 'testing'
# print(my_dict['name'])
# print(my_dict)

# Appending an item to a list in a dict
my_dict['skills'].append('Go lang')
my_dict['skills'].insert(2,'C##')
print(my_dict['skills'])


# Checking whether a key exists in a dictionary
# print('name' in my_dict)

# # Using Pop in dict
# #my_dict.pop('name')
# print(my_dict.get('name'))

# # Using pop item in dict 
# my_dict.popitem()
# print(my_dict)


# Looping through dictionary
for value in my_dict:
   print (value)

# Looping for printing both key and item
for key, value in my_dict.items():
    print(f'{key}: {value}')

# Looping for just the key
for key in my_dict.keys():
    print(f'{key} --')

# Looping for just the items
for value in my_dict.values():
    print(f'{value}')


# Loopping and exchanging the position of the key and items
for value, key in my_dict.items():
    print(f'{key}: {value}')


#print(my_dict,key())



key = input("Enter a random key: ")

if my_dict.get(key):
    print(my_dict.get(key))


else:
    print("Does not exist")