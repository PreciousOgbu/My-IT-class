def most_populated_countries():
    most_populated = ["China", "India", "USA", 
                      "Indonesia", "Pakistan", "Brazil", 
                      "Nigeria", "Bangladesh", "Russia", 
                      "Japan", "Mexico", "Ethiopia",
                       "Philippines", "Vietnam", "Egypt", 
                       "Germany", "Turkey", "Iran", 
                       "Thailand", "France"]
    user_inputs = []
    while True:
        user_input = input("Enter a country (or 'exit' to print the list and quit): ").capitalize().strip()
        if user_input.lower() == 'exit':
            if len(user_inputs) >= 5:
                print("Here are the most populated countries you entered in descending order:")
                for i, country in enumerate(sorted(user_inputs, key=most_populated.index, reverse=True), start=1):
                    print(f"{i}. {country}")
                break
            else:
                print("Please enter more countries to see the list.")
        elif user_input in most_populated:
            print(f"{user_input} is one of the most populated countries!")
            user_inputs.append(user_input)
        else:
            print("Sorry, this country is not one of the most populated in the world. Try again.")

most_populated_countries()

