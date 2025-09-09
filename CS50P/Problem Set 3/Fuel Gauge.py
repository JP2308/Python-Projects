# Step 1: prompt a user for a fraction
# format the input as X/Y, wherein each of X and Y is an integer,

def get_percentage():
    while True:
        try:
            # Step 1: prompt a user for a fraction
            fraction = input("Enter a fraction (e.g., 1/2): ")
            # format the input as X/Y, wherein each of X and Y is an integer, making sure to split each input
            numerator, denominator = map(int, fraction.split('/'))
            # because input has been mapped as an integer, they are divisible
            percentage = (numerator / denominator)

            if percentage >=1.01:
                continue
            elif percentage >= 0.99:
                print('F')
            elif percentage <= .01:
                print('E')
            else:
                # this is playing with format, the ':2.0% means no decimals and display as a percentage
                print(f'{percentage:2.0%}')
            break  # Exit loop if successful

        # errors will re-ask the question until the correct format
        except ZeroDivisionError:
            fraction = input("Enter a fraction (e.g., 1/2): ")
        except ValueError:
            fraction = input("Enter a fraction (e.g., 1/2): ")

get_percentage()
