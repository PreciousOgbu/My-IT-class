# Write a function that which generates a six digit/ character random_user_id.

import random
#import string


# def random_user_id():
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for i in range (6))


# print(random_user_id())



def random_user_id():
    return f'{random.randint(0, 2**24):06x}'



print(random_user_id())