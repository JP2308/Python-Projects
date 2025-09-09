def main():
    while True:
        try:
            fraction = input("Enter a fraction (e.g., 1/2): ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    numerator, denominator = map(int, fraction.strip().split("/"))
    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator:
        raise ValueError
    return round((numerator / denominator) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
