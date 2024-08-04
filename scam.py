from faker import Faker

fake = Faker()

print(fake.name())
print(fake.address())
print(fake.email())
print(fake.phone_number())
print(fake.credit_card_number())
print(fake.date_of_birth())
print(fake.country())

