import random

def main():
    level = get_level()
    # tracks correct answers
    score = 0

    for questions in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        answer = num1 + num2
        attempts = 0

        while attempts < 3:
            try:
                # asks a user a sum
                question = int(input(f'{num1} + {num2} = '))

        # if the input is equal to the answer, the next sum is present
                if question == answer:
                    score += 1
                    break
                else:
                    print('EEE')
                    attempts += 1
            except ValueError:
                print('EEE')
                attempts += 1
        if attempts == 3:
            print(f'{num1} + {num2} = {answer}')

    print(f'Score: {score}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level < 1 or level > 3:
                raise ValueError()
            return level

        except ValueError:
                print("Please input a level between 1 and 3")

# random integers will be generated for the level
def generate_integer(level):
        if level == 1:
            return random.randint(0, 9)  # Single-digit numbers
        elif level == 2:
            return random.randint(10, 99)  # Two-digit numbers
        elif level == 3:
            return random.randint(100, 999)  # Three-digit numbers
        else:
            raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
