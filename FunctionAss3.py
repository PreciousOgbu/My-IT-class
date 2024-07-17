# A function to show voter's eligbility to vote

def check_voter_eligibility():
    Age = int(input("Please enter your age: "))
    if Age < 18:
        return 'You are not eligible to vote.'
    
    elif Age > 90:
     return 'You are too old to vote.'
    
    else:
       return "Congratulation, you can now vote online."
    
result = check_voter_eligibility()
#print(result)