def limited_list():
    user_list = []
    while len(user_list) < 10:
        user_input = input("Enter an item to add to the list (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        user_list.append(user_input)
        print(f"Added '{user_input}' to the list. {10 - len(user_list)} spots remaining.")
    print("List is full! Here are the items:")
    for i, item in enumerate(user_list, start=1):
        print(f"{i}. {item}")

limited_list()