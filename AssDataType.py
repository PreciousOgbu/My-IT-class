def check_data_type():
    lst = ['item1', 'item2',  4, 3.0]


    for my_list in lst:
        if type(my_list) == str or type(my_list) == float or type(my_list) == bool or type(my_list) == int:
            return 'List  contains mixed data type'
            
        
        else:
            return type(my_list)
        


print(check_data_type())