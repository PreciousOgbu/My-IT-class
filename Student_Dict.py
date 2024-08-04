# Create a student Dictionary

def Student_Dictionary():
    Student_Dict = {
        "First_name": "Kelechi",
        "Last_name": "Ogbu", 
        "Gender" : "Male",
        'Age': '17 years, 11 months and 7 days',
        "Marital_status": "Single",
        "Skills": ["Java", "Html", "Javascript", "Python"],
        "Country": "Nigeria", 
        "City": "Enugu",
        "Address": "10 Adventist Centenary Avenue Maryland Enugu"
    }
    print (Student_Dict)


# Length of the dictionary 
    Len_Student_Dict_ = Student_Dict
    print('Length of student dictionary is:', len(Len_Student_Dict_))

# Get the value of the skills and check the data type
    print('Skills:', Student_Dict["Skills"])
    print("Type of skills:", type(Student_Dict["Skills"]))

# Modify the skills values by adding one or two skills
    Student_Dict['Skills'].append('C++')
    Student_Dict['Skills'].insert(3,'C##')
    print('Modified Skills:',Student_Dict['Skills'])

# Get the dictionary keys as a list
    print("Dictionary keys:", list(Student_Dict.keys()))


# Get the dictionary values as a list
    print("Dictionary values:", list(Student_Dict.values()))

# Change the dictionary to a list of tuples using items method
    print("List of tuples:", list(Student_Dict.items()))

# Delete one of the items in the dictionary
    del Student_Dict["Age"]
    print("Student dictionary after deleting age:", Student_Dict)




Student_Dictionary()