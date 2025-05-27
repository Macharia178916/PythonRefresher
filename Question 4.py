def check_case(char):
    if char.isupper():
        return "The character is uppercase."
    elif char.islower():
        return "The character is lowercase."
    else:
        return "The character is not a letter."

def main():
    char = input("Enter a single character: ")

    # Ensure only one character is entered
    if len(char) != 1:
        print("Please enter exactly one character.")
    else:
        result = check_case(char)
        print(result)

# Run the main function
main()