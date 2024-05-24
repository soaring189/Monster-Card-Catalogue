import easygui

catalogue = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}}

choice = ""


def FindCard(search):
    if search is not None and search != "":
        if search.capitalize() in catalogue:
            search = search.capitalize()
            result = f"┌{'─' * (int(len(search) / 2) + 1)}" \
                     f"┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┐\n" \
                     f"│{' ' * ((int(len(search) / 2) + 1) * 2)}" \
                     f"│ Strength │  Speed   │ Stealth  │ Cunning  │\n" \
                     f"├{'─' * (int(len(search) / 2) + 1)}" \
                     f"┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
            if len(search) % 2 == 1:
                result += f"│{search} │"
            else:
                result += f"│{search}  │"
            for i, j in catalogue[search].items():
                if len(str(j)) == 1:
                    result += f"    {j}     │"
                elif len(str(j)) == 2:
                    result += f"    {j}    │"
            result += f"\n└{'─' * (int(len(search) / 2) + 1)}" \
                      f"┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┘\n"
            if easygui.buttonbox(result + "\nDo you want to make any changes?",
                                 choices=["Yes", "No"]) == "Yes":
                EditCard(search.capitalize())
        else:
            easygui.msgbox("This card is not in the catalogue")


def EditCard(edit):
    fields = ["Name:", "Strength:", "Speed:", "Stealth:", "Cunning:"]
    defaults = [edit,
                str(catalogue[edit]["Strength"]),
                str(catalogue[edit]["Speed"]),
                str(catalogue[edit]["Stealth"]),
                str(catalogue[edit]["Cunning"])]
    new_card = easygui.multenterbox('Enter the new card information:',
                                    'Change card', fields, defaults)
    while new_card is not None and new_card != defaults:
        if len(new_card[0]) < 26:
            try:
                new_card[1] = int(new_card[1])
                new_card[2] = int(new_card[2])
                new_card[3] = int(new_card[3])
                new_card[4] = int(new_card[4])
                if 0 < new_card[1] < 26 and 0 < new_card[2] < 26 and 0 < \
                        new_card[3] < 26 and 0 < new_card[4] < 26:
                    catalogue.pop(edit)
                    catalogue[new_card[0].capitalize()] = \
                        {"Strength": new_card[1],
                         "Speed": new_card[2],
                         "Stealth": new_card[3],
                         "Cunning": new_card[4]}
                    break
                else:
                    easygui.msgbox(
                        "Please enter the four values from 1 to 25")
                    new_card = easygui.multenterbox(
                        'Enter the new card information:', 'Change card',
                        fields, defaults)
            except ValueError:
                easygui.msgbox("Please enter an integer for each of the four "
                               "values of the monster card")
                new_card = easygui.multenterbox('Enter the new card information:',
                                                'Change card', fields, defaults)
        else:
            easygui.msgbox("Please enter the new monster card name "
                           "no longer than 25")
            new_card = easygui.multenterbox('Enter the new card information:',
                                            'Change card', fields, defaults)


def OutputAll(cards):
    max_name_length = max(len(name) for name in cards.keys())
    output = f"┌{'─' * (int(max_name_length / 2) + 1)}" \
             f"┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┐\n"
    output += f"│{' ' * (int(max_name_length / 2) - 1)}" \
              f"Name{' ' * (int(max_name_length / 2) - 1)}" \
              f"│ Strength │  Speed   │ Stealth  │ Cunning  │\n"
    output += f"├{'─' * (int(max_name_length / 2) + 1)}" \
              f"┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
    for i, j in cards.items():
        if max_name_length % 2 == 1:
            output += f"│{i}{' ' * (max_name_length - len(i) + 1)}│"
        else:
            output += f"│{i}{' ' * (max_name_length - len(i) + 2)}│"
        for k in j:
            if len(str(j[k])) == 2:
                output += f"    {j[k]}    │"
            elif len(str(j[k])) == 1:
                output += f"    {j[k]}     │"
        if i != list(cards.keys())[-1]:
            output += f"\n├{'─' * (int(max_name_length / 2) + 1)}" \
                      f"┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
        else:
            output += f"\n└{'─' * (int(max_name_length / 2) + 1)}" \
                      f"┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┘\n"
    easygui.msgbox(output, title="Cards")


while choice != "Exit" and choice is not None:
    choice = easygui.buttonbox("What would you like to do?",
                               choices=["Output all", "Find card", "Exit"],
                               title="CATALOGUE OPTIONS")
    if choice == "Output all":
        OutputAll(catalogue)
    elif choice == "Find card":
        FindCard(easygui.enterbox("Please enter the card you want to find"))
