# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list


import random 

def shuffle_list(input_list):
    list_copy = input_list.copy()


    random.shuffle(list_copy)
    return list_copy

my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print(shuffled_list)
