# Write a function that rewrites a string when written


def reverse_string():
    input_string = input("Enter a string: ")

    reversed_string = input_string[:: -1]

    print(f'Orginal String {input_string}')

    print(f'Reversed string: {reversed_string}')


reverse_string()