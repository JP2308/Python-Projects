# prompt a user for names, continued loop
name_list = []

while True:
    try:
        name = input('Name: ')
        # when name is inputted, add to the list
        name_list.append(name)

    # when user hits control-d
    except EOFError:
        print()
        total_names = len(name_list)
        if total_names >3:
            print(f"Adieu, adieu, to {', '.join(name_list[:-1])}, and {name_list[-1]}")

        elif total_names == 3:
            print(f'Adieu, adieu, to {name_list[0]}, {name_list[1]}, and {name_list[-1]}')

        elif total_names == 2:
            print(f'Adieu, adieu, to {name_list[0]} and {name_list[-1]}')

        else:
            print(f'Adieu, adieu, to {name_list[0]}')

        break
