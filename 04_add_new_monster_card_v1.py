# Allow users to add monster cards through multiple Windows
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
        valid_name = False
        new_name = easygui.enterbox("Please enter the new monster name")
        while not valid_name:
            if new_name is not None:
                if len(new_name) < 25 and new_name.capitalize() not in catalogue:
                    valid_name = True
                else:
                    easygui.msgbox(
                        "Please enter a new name less than 25 characters")
                    new_name = easygui.enterbox(
                        "Please enter the new monster name")
            else:
                break
        if valid_name:
            valid_value = True
            attributes = ['strength', 'speed', 'stealth', 'cunning']
            values = []
            for attribute in attributes:
                value = easygui.integerbox(
                    f"Please enter the {attribute} of {new_name}",
                    lowerbound=1, upperbound=25)
                values.append(value)
                if value is None:
                    valid_value = False
                    break
            if valid_value:
                catalogue[new_name.capitalize()] = {"Strength": values[0],
                                                    "Speed": values[1],
                                                    "Stealth": values[2],
                                                    "Cunning": values[3]}
    elif choice == "Output all":
        OutputAll(catalogue)
