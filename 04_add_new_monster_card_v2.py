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
                               choices=["Add card", "Output all", "Exit"],
                               title="CATALOGUE OPTIONS")
    if choice == "Add card":
        fields = ["Name:", "Strength:", "Speed:", "Stealth:", "Cunning:"]
        new_card = easygui.multenterbox('Enter the new card information:',
                                        'Change card', fields)
        while new_card is not None and new_card != ['', '', '', '', '']:
            if len(new_card[0]) < 26:
                try:
                    new_card[1] = int(new_card[1])
                    new_card[2] = int(new_card[2])
                    new_card[3] = int(new_card[3])
                    new_card[4] = int(new_card[4])
                    if 0 < new_card[1] < 26 and 0 < new_card[2] < 26 and 0 < \
                            new_card[3] < 26 and 0 < new_card[4] < 26:
                        add_output = \
                            f"┌{'─' * (int(len(new_card[0]) / 2) + 1)}" \
                            f"┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┐\n" \
                            f"│{' ' * ((int(len(new_card[0]) / 2) + 1) * 2)}" \
                            f"│ Strength │  Speed   │ Stealth  │ Cunning  │\n" \
                            f"├{'─' * (int(len(new_card[0]) / 2) + 1)}" \
                            f"┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
                        if len(new_card[0]) % 2 == 1:
                            add_output += f"│{new_card[0]} │"
                        else:
                            add_output += f"│{new_card[0]}  │"
                        for i in range(1, 5):
                            if len(str(new_card[i])) == 1:
                                add_output += f"    {new_card[i]}     │"
                            elif len(str(new_card[i])) == 2:
                                add_output += f"    {new_card[i]}    │"
                        add_output += \
                            f"\n└{'─' * (int(len(new_card[0]) / 2) + 1)}" \
                            f"┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┘\n"
                        confirm = easygui.buttonbox(f"Do you want to add\n"
                                                    f"\n{add_output}\n"
                                                    f"\nto the catalogue?",
                                                    title="Confirm addition",
                                                    choices=["Yes", "No"])
                        if confirm == "Yes":
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
                            fields)
                except ValueError:
                    easygui.msgbox(
                        "Please enter an integer for each of the four "
                        "values of the monster card")
                    new_card = easygui.multenterbox(
                        'Enter the new card information:',
                        'Add card', fields)
            else:
                easygui.msgbox("Please enter the new monster card name "
                               "no longer than 25")
                new_card = easygui.multenterbox(
                    'Enter the new card information:', 'Add card', fields)
    elif choice == "Output all":
        OutputAll(catalogue)
