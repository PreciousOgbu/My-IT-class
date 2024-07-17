#   Write a code that gives the grades of stdents according to their scores 


score=int(input("Enter the student's score: "))


if 80 <= score <= 100:
 grade = 'A'

elif 70 <= score <= 79:
  grade = 'B'

elif 60<= score <= 69:
  grade= 'C'

elif 50<= score <= 59:
  grade= 'D'

elif 0<= score <= 49:
  grade= 'F'
 
  
else: 
  grade='Invalid score'
  print(grade)

print (f'The grade for a score of {score} is {grade}.')

