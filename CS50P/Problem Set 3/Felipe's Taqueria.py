Taco = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    # call the menu function logic
    menu()

def menu():
    # create a list where each respective item in the order can be stored
    total = 0.0

    # create a loop so items can be added to the order list
    while True:
        # Continually Prompt user for the Item contained in Taco
        # Note: This makes the input lowered but the dictionary is all uppercase, hence the loop below
        # After each item total should be displayed NOT after the cumulative menu has been commanded
        try:
            items = input('Item: ').title()
            # for items that are in the dictionary and add their value to the Menu_order list
            # note: price can be anything, it is just accessing the value of the dictionary
            # this now checks that items in the dictionary (as they are lowered) are equivalent to items
            if items in Taco:
                # add the price value to the Menu_order
                total+= Taco[items]
                # this breaks the loop because once it has found the first match of the menu item, it stops iterating
                # if I didn't include this, the loop would add 3 different menu items
            # check each item in the order and sum

            if items not in Taco:
                input('Item: ').title()

            print("Total: $", end="")
            print("{:.2f}".format(total))


        except EOFError:
            # error checker won't accept a solution where output is 'Item: Total' so this line ensures total hits a new line
            print()
            break

main()
