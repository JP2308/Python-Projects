def main():
    user_input = input("Input: ")  # Store the user's input in a variable

    # Convert the string to Twitter space lingo
    output = convert_to_twtr(user_input)  # Pass the user's input to the function

    print("Output:", output)

def convert_to_twtr(string_input):
    result = []
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]  # Include lowercase vowels

    for char in string_input:
        # If the character is a vowel, skip it
        if char in vowels:
            continue
        else:
            result.append(char)  # Add consonants to the result list

    # Join the result list into a single string
    return ''.join(result)

main()
