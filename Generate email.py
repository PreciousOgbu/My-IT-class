# A function that generates email

def add_email(first_name, last_name):
    first_letter = first_name[0].lower()
    email = (f'{first_letter}.{last_name.lower()}@gmail.com')
    return email

while True:
    first_name = input("Enter your first name(or 'quit' to stop): ")

    if first_name.lower() == 'quit':
       break

    last_name = input("Enter your last name: ") 
    email = add_email(first_name, last_name)
    print("Your email address is:", email)