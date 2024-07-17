
my_tuple = (1, 2, 5, 3, 5, 5, 4, 5, 6.1, 2.3, 5.9, 3.3)
fruits = ('Banana', 'Pineapple', 'Orange', "Applee", "Watermelon" )
print('Apple' in fruits, )


# my_list = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]
# my_tuple = tuple(my_list)
# print(my_tuple)
# # print((my_tuple))
# print(my_tuple.count(5))
# print(len(my_tuple))
# print(my_tuple[-1])
# print(my_tuple[0:5])

# lst = list(my_tuple)
# print(lst)
# lst.append(7)
# print(lst)
    

def my_fruits(fruits):
    for fruit in fruits:
        print(fruit)


#my_fruits(fruits)

#del fruits
#print(fruits)

my_full_tuple =  my_tuple + fruits 
print(my_full_tuple)

for my_full_t in my_full_tuple:
  if type(my_full_t) == str:
      print(my_full_t.upper())
    
  if type(my_full_t) == int:
        print(my_full_t *10)

  if type(my_full_t) == float:
      print(my_full_t *100)

  





   