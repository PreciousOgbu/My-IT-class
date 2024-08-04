def most_spoken_languages():
    most_spoken = ["Mandarin", "Spanish", "English", 
                   "Hindi", "Arabic", "Bengali",
                     "Portuguese", "Russian", "Japanese", 
                     "Punjabi", "German", "Javanese",
                       "Wu", "French", "Telugu", 
                       "Vietnamese", "Marathi", "Korean", 
                       "Tamil", "Turkish", 
                        "Polish", "Thai", 
                        "Nepail", "Oromo" , "Igbo",]
    user_inputs = []
    while True:
        user_input = input("Enter a language (or 'exit' to print the list and quit): ").capitalize().strip()
        if user_input.lower() == 'exit':
            
            if len(user_inputs) >= 5:
                print("Here are the most spoken languages you entered in descending order:")
                for i, language in enumerate(sorted(user_inputs, key=most_spoken.index, reverse=True), start=1):
                    print(f"{i}. {language}")
                break
            else:
                print("Please enter more languages to see the list.")
        elif user_input in most_spoken:
            print(f"{user_input} is one of the most spoken languages!")
            user_inputs.append(user_input)
        else:
            print("Sorry, this language is not one of the most spoken in the world. Try again.")

most_spoken_languages()


