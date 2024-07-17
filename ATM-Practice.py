Balance=1000

#adding to the balance

choice= int(input('How much do you want to add to the balance: '))

if choice <= 0:
    print('invalid amount')

else:
    Balance += choice
    #Balance= Balance + choice
    print(f'Your new balance is now: ${Balance}')

    #withdrawing from the balance

choice= int(input('How much do you want to withdraw from the balance? '))
if choice <= 0 or choice > Balance:
    print('Invalid amount or insufficient balance')

else:
    Balance -=choice
    #Balance= Balance-choice
    print(f'Your new balance is now: ${Balance}')

#Checking the balance
    
#print(f'Your current balance is: ${Balance}')
