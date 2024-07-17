#Declare a list that has mixed data type (i) Print all (ii)Print individually 

Person_info=['Uche Nnamani', 32, 1.80, 'Single', '10th Adventist Avenue Maryland, Enugu'] 
print(Person_info)


for item in Person_info:
    print(item)
      #OR
name= Person_info[0]
age= Person_info[1]
height=Person_info[2]
marital_status=Person_info[3]
address=Person_info[4]

print(f'Name: {name}')
print(f'Age: {age}')
print(f'Height: {height}')
print(f'Marital-Status: {marital_status}')
print(f'Address: {address}')


