def main():
    user_input = input("Input: ")  # Store the user's input in a variable

    # Convert the string to Twitter space lingo
    output = shorten(user_input)  # Pass the user's input to the function

    print("Output:", output)


def shorten(word):
    result = []
    vowels = ["A", "E", "I", "O", "U"]  # Include lowercase vowels

    for char in word:
        # If the character is a vowel, skip it
        if char in vowels:
            continue
        else:
            result.append(char)  # Add consonants to the result list

    # Join the result list into a single string
    return ''.join(result)


if __name__ == "__main__":
    main()
