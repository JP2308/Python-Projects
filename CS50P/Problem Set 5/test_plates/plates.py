def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    banned = {".", " ", "!"}

    # Rule 1: Length between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Starts with at least two letters
    if not s[0:2].isalpha():
        return False

    # Rule 3: No banned characters
    if any(char in banned for char in s):
        return False

    # Rule 4: Numbers must be at the end, and first digit can't be 0
    digit_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not digit_started:
                if char == "0":
                    return False
                digit_started = True
        elif digit_started:
            return False  # Letters after numbers = invalid

    return True


if __name__ == "__main__":
    main()
