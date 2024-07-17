Fruits = {"Apple", "Banana", 
          "Grape", "Orange", "Pineapple", 
          "Cucumber", "Strawberry", "Watermelon", 
          "Kiwi", "Blackberry"}
print(len(Fruits))

def check_set():
    copy_fruits = set()
    user_fruit = input("Please input a fruit name: ").capitalize().strip()
    if user_fruit in Fruits:
        copy_fruits.add(user_fruit)
        #return copy_fruits
    else:
        print("Fruit not found")
    return copy_fruits
    

print(check_set())