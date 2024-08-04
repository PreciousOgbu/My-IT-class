import hashlib


def hash_password(password):
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    return hash_password



password = input('Enter password: ')
hashed_password = hash_password(password)
print('Hashed password:', hashed_password)