import easygui


# Combo Adder V1 created by James Renner
def combo_adder():
    # A clear dictionary which values can be added to later
    combo = {}
    # Asks for the combo name and how many items are in the combo
    combo_name = easygui.enterbox("Enter Combo Name:")
    combo_item_num = easygui.integerbox("How many items are in the combo?", lowerbound=1, upperbound=5)
    combo_items = {}
    combo_meal_counter = 1
    # While the number of items in the combo is greater than 0, it asks the name and cost of the meal
    # Then adds it into another empty dictionary
    while combo_item_num > 0:
        combo_meal = easygui.enterbox(f"What is combo meal {combo_meal_counter} called?").lower()
        meal_cost = easygui.integerbox("How much does the meal cost? ($0.1-20)", lowerbound=1, upperbound=20)
        combo_items[combo_meal] = meal_cost
        combo_meal_counter += 1
        combo_item_num -= 1
    # Adds the combo meal info to the dictionary at the top
    combo[combo_name] = combo_items
    # Formats and prints the combo meal
    combos_text = ""
    for combo_name, combo_items in combo.items():
        combos_text += f"{combo_name}:\n"
        for meal, cost in combo_items.items():
            combos_text += f"- {meal}: ${cost}\n"
        combos_text += "\n"

    easygui.msgbox(f"Combos added:\n\n{combos_text}")
    correct_combo = easygui.buttonbox(msg="Is this the correct combo?", choices=["yes", "no"])
    if correct_combo == "no":
        combo_adder()
    else:
        easygui.msgbox("Great! Have a good day!")


# Runs the whole program
combo_adder()
