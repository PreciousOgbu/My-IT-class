# To check data tyypes
def check_data_types(lst):
    if not isinstance(lst, list):
        return 'This is not a list'
    
    first_item = type(lst[0])
    if len(lst) == 1:
        return 'You only have one item in the list, Nothing to compare'
    
    for item in lst:
        if type(item) != first_item:
            return False
        
    return True

print(check_data_types(['5', 'Presh']))