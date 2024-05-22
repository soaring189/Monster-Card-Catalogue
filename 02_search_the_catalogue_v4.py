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
            easygui.msgbox(result)
        else:
            easygui.msgbox("This card is not in the catalogue")


while choice != "Exit" and choice is not None:
    choice = easygui.buttonbox("What would you like to do?",
                               choices=["Find card", "Exit"],
                               title="CATALOGUE OPTIONS")
    if choice == "Find card":
        FindCard(easygui.enterbox("Please enter the card you want to find"))
