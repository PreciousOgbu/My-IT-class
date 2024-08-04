def check_negative_number(lst):
    if not isinstance (lst, list):
        return "This is not a list"
    
    for negative in lst:
        if negative < 0:
            print (f'Negative number found in the list')
            return negative
        

print(check_negative_number([1, 2, 3,-4, 9, -6]))