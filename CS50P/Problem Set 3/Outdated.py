# List of month names for reference
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        try:
            # Prompt user for a date
            date = input("Date: ").strip()

            # Check for month-day-year (e.g., 9/8/1636)
            if "/" in date and date.count("/") == 2:
                month, day, year = map(int, date.split("/"))

            # Check for 'Month day, year'
            else:
                parts = date.split()
                if len(parts) == 3 and parts[0] in MONTHS and "," in parts[1]:
                    month = MONTHS.index(parts[0]) + 1
                    day = int(parts[1].strip(","))
                    year = int(parts[2])
                else:
                    raise ValueError

            # Validate day and month range
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError

            # Output the date in YYYY-MM-DD format
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):
            continue

main()
