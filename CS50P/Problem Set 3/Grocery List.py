from collections import Counter

#  creates an empty list to fill with items
shopping_list = []

try:
# prompts the user for items, one per line. Treats the user’s input case-insensitively
    while True:
        shopping = input().casefold()
        shopping_list.append(shopping)

# the user inputs control-d
except:
    print()
    # sorted alphabetically by item

# Count the frequency of each item
counter = Counter(shopping_list)

# Output the grocery list in uppercase, sorted alphabetically
for item in sorted(counter.keys(), key=str.casefold):
    # Output the user’s grocery list in all uppercase,
    # prefixing each line with the number of times the user inputted that item.
    # # Note: does not pluralize the items.
    print(f"{counter[item]} {item.upper()}")

