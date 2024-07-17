# Print the list





def check_fruits():
    Fruits = {"Apple", "Banana", "Grape", 
              "Orange", "Pineapple", "Cucumber", 
              "Strawberry", "Watermelon", "Kiwi", 
              "Blackberry",}
    #print(len(Fruits))

    
    input_fruits = set()
    while True:
        Fruit = input("Enter the fruits you want to print (or 'end' to finish): ").strip().capitalize()
        if Fruit.lower() == 'end':
            break

        input_fruits.add(Fruit.capitalize())
        if Fruit.capitalize() in Fruits:
            print(f'{Fruit} is in fruit set')

             
        else:
            print(f'{Fruit} is not in the fruit set')
            print("Below are the fruits you entered that are in the fruit set: ")
            print(input_fruits & Fruits)
            
             
            
            

check_fruits()