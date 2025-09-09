def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    banned = [".", " ", "!"]
    digits = "0123456789"

    # Rule 1: Maximum of 6 characters, minimum of 2 characters
    if not (2 <= len(s) <= 6):
        return False

    # “Numbers cannot be used in the middle of a plate; 
    # they must come at the end. For example, AAA222 would be an acceptable … vanity plate; 
    # AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

    has_seen_digit = False
    for char in s:
        if char.isdigit():
            if not has_seen_digit and char == "0":
                return False  # First number cannot be 0
            has_seen_digit = True
        elif has_seen_digit:  # If we've seen a digit, no more letters allowed
            return False

    # “All vanity plates must start with at least two letters.”
    if not (s[0:1].isalpha()):
        return False

    # “No periods, spaces, or punctuation marks are allowed.”
    if any(char in banned for char in s):
        return False

    return True

main()



