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

choice = easygui.buttonbox("What would you like to do?",
                           choices=["Find card", "Exit"],
                           title="CATALOGUE OPTIONS")


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
    if choice == "Find card":
        card_list = []
        for i in catalogue.keys():
            card_list.append(i)
        search = easygui.buttonbox("Please select the card you want to find",
                                   choices=card_list)
        result = f"┌{'─'*(int(len(search) / 2) + 1)}┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┬{'─' * 5}┐\n" \
                 f"│{' '*((int(len(search) / 2) + 1) * 2)}│ Strength │  Speed   │ Stealth  │ Cunning  │\n" \
                 f"├{'─'*(int(len(search) / 2) + 1)}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┼{'─' * 5}┤\n"
        if len(search) % 2 == 1:
            result += f"│{search} │"
        else:
            result += f"│{search}  │"
        for i, j in catalogue[search].items():
            if len(str(j)) == 1:
                result += f"    {j}     │"
            elif len(str(j)) == 2:
                result += f"    {j}    │"
        result += f"\n└{'─' * (int(len(search) / 2) + 1)}┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┴{'─' * 5}┘\n"
        easygui.msgbox(result)
