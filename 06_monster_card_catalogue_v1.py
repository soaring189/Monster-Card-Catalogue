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


def OutputAll():
    if catalogue != {}:
        max_name_length = max(len(name) for name in catalogue.keys())
        output = f"┌{'─' * (int(max_name_length / 2) + 1)}" \
                 f"┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┐\n"
        output += f"│{' ' * (int(max_name_length / 2) - 1)}" \
                  f"Name{' ' * (int(max_name_length / 2) - 1)}" \
                  f"│ Strength │  Speed   │ Stealth  │ Cunning  │\n"
        output += f"├{'─' * (int(max_name_length / 2) + 1)}" \
                  f"┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
        for i, j in catalogue.items():
            if max_name_length % 2 == 1:
                output += f"│{i}{' ' * (max_name_length - len(i) + 1)}│"
            else:
                output += f"│{i}{' ' * (max_name_length - len(i) + 2)}│"
            for k in j:
                if len(str(j[k])) == 2:
                    output += f"    {j[k]}    │"
                elif len(str(j[k])) == 1:
                    output += f"    {j[k]}     │"
            if i != list(catalogue.keys())[-1]:
                output += f"\n├{'─' * (int(max_name_length / 2) + 1)}" \
                          f"┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
            else:
                output += f"\n└{'─' * (int(max_name_length / 2) + 1)}" \
                          f"┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┘\n"
        easygui.msgbox(output, title="Cards")
    else:
        easygui.msgbox("There is no card in the catalogue")


def DeleteCard():
    if catalogue != {}:
        card_list = []
        for i in catalogue.keys():
            card_list.append(i)
        card_list.append("Cancel")
        delete = easygui.buttonbox("Please select the card you want to delete",
                                   choices=card_list)
        if delete != "Cancel":
            result = f"┌{'─' * (int(len(delete) / 2) + 1)}" \
                     f"┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┐\n" \
                     f"│{' ' * ((int(len(delete) / 2) + 1) * 2)}" \
                     f"│ Strength │  Speed   │ Stealth  │ Cunning  │\n" \
                     f"├{'─' * (int(len(delete) / 2) + 1)}" \
                     f"┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
            if len(delete) % 2 == 1:
                result += f"│{delete} │"
            else:
                result += f"│{delete}  │"
            for i, j in catalogue[delete].items():
                if len(str(j)) == 1:
                    result += f"    {j}     │"
                elif len(str(j)) == 2:
                    result += f"    {j}    │"
            result += f"\n└{'─' * (int(len(delete) / 2) + 1)}" \
                      f"┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┘\n"
            confirm = easygui.buttonbox(
                result + "\nDo you want to delete this card?",
                title="Confirm deletion",
                choices=["Yes", "No"])
            if confirm == "Yes":
                catalogue.pop(delete)
    else:
        easygui.msgbox("There is no card in the catalogue")


def AddCard():
    fields = ["Name:", "Strength:", "Speed:", "Stealth:", "Cunning:"]
    new_card = easygui.multenterbox('Enter the new card information:',
                                    'Change card', fields)
    while new_card is not None and new_card != ['', '', '', '', '']:
        if len(new_card[0]) < 26:
            if str(new_card[0]).capitalize() not in catalogue:
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
                            add_output += f"│{new_card[0].capitalize()} │"
                        else:
                            add_output += f"│{new_card[0].capitalize()}  │"
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
                easygui.msgbox("This card is already in the catalogue")
                new_card = easygui.multenterbox(
                    'Enter the new card information:', 'Add card', fields)
        else:
            easygui.msgbox("Please enter the new monster card name "
                           "no longer than 25")
            new_card = easygui.multenterbox(
                'Enter the new card information:', 'Add card', fields)


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
                EditCard(search.capitalize(), result)
        else:
            easygui.msgbox("This card is not in the catalogue")


def EditCard(edit, result_before_edit):
    fields = ["Name:", "Strength:", "Speed:", "Stealth:", "Cunning:"]
    defaults = [edit,
                str(catalogue[edit]["Strength"]),
                str(catalogue[edit]["Speed"]),
                str(catalogue[edit]["Stealth"]),
                str(catalogue[edit]["Cunning"])]
    new_card = easygui.multenterbox('Enter the new card information:',
                                    'Change card', fields, defaults)
    while new_card is not None and new_card != defaults and new_card != ['', '', '', '', '']:
        if len(new_card[0]) < 26:
            try:
                new_card[1] = int(new_card[1])
                new_card[2] = int(new_card[2])
                new_card[3] = int(new_card[3])
                new_card[4] = int(new_card[4])
                if 0 < new_card[1] < 26 and 0 < new_card[2] < 26 and 0 < \
                        new_card[3] < 26 and 0 < new_card[4] < 26:
                    result_after_edit = \
                        f"┌{'─' * (int(len(new_card[0]) / 2) + 1)}" \
                        f"┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┐\n" \
                        f"│{' ' * ((int(len(new_card[0]) / 2) + 1) * 2)}" \
                        f"│ Strength │  Speed   │ Stealth  │ Cunning  │\n" \
                        f"├{'─' * (int(len(new_card[0]) / 2) + 1)}" \
                        f"┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
                    if len(new_card[0]) % 2 == 1:
                        result_after_edit += f"│{new_card[0]} │"
                    else:
                        result_after_edit += f"│{new_card[0]}  │"
                    for i in range(1, 5):
                        if len(str(new_card[i])) == 1:
                            result_after_edit += f"    {new_card[i]}     │"
                        elif len(str(new_card[i])) == 2:
                            result_after_edit += f"    {new_card[i]}    │"
                    result_after_edit += \
                        f"\n└{'─' * (int(len(new_card[0]) / 2) + 1)}" \
                        f"┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┘\n"
                    confirm = easygui.buttonbox(f"Do you want to change\n"
                                                f"\n{result_before_edit}\n"
                                                f"to\n"
                                                f"\n{result_after_edit}\n",
                                                title="Confirm changes",
                                                choices=["Yes", "No"])
                    if confirm == "Yes":
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
                new_card = easygui.multenterbox(
                    'Enter the new card information:',
                    'Change card', fields, defaults)
        else:
            easygui.msgbox("Please enter the new monster card name "
                           "no longer than 25")
            new_card = easygui.multenterbox('Enter the new card information:',
                                            'Change card', fields, defaults)


while choice != "Exit" and choice is not None:
    choice = easygui.buttonbox("What would you like to do?",
                               choices=["Add card", "Delete card",
                                        "Find card", "Output all", "Exit"],
                               title="CATALOGUE OPTIONS")
    if choice == "Add card":
        AddCard()
    elif choice == "Delete card":
        DeleteCard()
    elif choice == "Find card":
        FindCard(easygui.enterbox("Please enter the card you want to find"))
    elif choice == "Output all":
        OutputAll()
