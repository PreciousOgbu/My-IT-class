# Packing and Unpacking Functions


def add_numbers(num_1, num_2, num_3, num_4, num_5, num_6):
    return num_1 + num_2 + num_3 + num_4 + num_5 + num_6

lst = [1, 2, 3, 4, 5, 6]
sum = add_numbers(*lst)
print(sum)

def unpack(*args):  # Packing
    for num in args:
        print(num )

#unpack(1, 2, 3, 4, 5, 6)

lst_1 = ["Hello", "World","Python", "Is", "Fun"]
# for i in lst_1:
#     print(i)


unpack(*lst_1)   #Unpacking


lst_2 = [1, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9]

lst_3 = [1, 2, 3, 4,  5,]

generallist = [*lst_2,*lst_3]
print(generallist)

print('index |', 'items')
for index, general in enumerate(generallist):
    print("  ",index, '----', general)




