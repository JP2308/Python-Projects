import random


while True:
    try:
       level = int(input('Level: '))
       if level < 1:
           raise ValueError()
       break
    except ValueError:
        continue

# generates a random number for the level
number = random.randint(1,level)


while True:
   try:
        guess = int(input('Guess: '))

        # Checks if guess is within a valid range
        if guess < 1 or guess > level:
            raise ValueError("Too large!")

        if guess == number:
            print('Just right!')
            break

        elif guess < number:
            print('Too small!')
            continue

        else:
            print('Too large!')
            continue

   except ValueError:
       print("Too large!")
       continue
