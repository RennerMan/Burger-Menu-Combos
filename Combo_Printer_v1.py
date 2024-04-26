import easygui

# Existing combos
existing_combos = {
    "Value": {
        "Beef burger": 5.69,
        "Fries": 1,
        "Fizzy drink": 1
    },
    "Cheesy": {
        "Cheeseburger": 6.69,
        "Fries": 1,
        "Fizzy drink": 1
    },
    "Super": {
        "Cheeseburger": 6.69,
        "Large Fries": 2,
        "Smoothie": 2
    }
}


def combo_deleter():
    # Prompts user for the combo title
    combo_eraser = easygui.enterbox(msg="Type the name of the combo you want to delete\n"
                                        " (eg: Value, Cheesy, Super)").capitalize()

    # Loop until a valid combo name is entered
    while combo_eraser not in existing_combos:
        easygui.msgbox("Combo not found!", title="Error")
        combo_eraser = easygui.enterbox(msg="Type the name of the combo you want to delete,"
                                            " (eg: Value, Cheesy, Super)").capitalize()

    # If correct, pop the combo and show user what combo was popped
    deleted_combo = existing_combos.pop(combo_eraser)
    # Asks user if their combo is correct. If not, the code asks the user to enter it again.
    message = f"Deleted combo:\n{combo_eraser}:\n"
    for item, price in deleted_combo.items():
        # Prints the combo items and their prices
        message += f"{item}: ${price:.2f}\n"
    easygui.msgbox(message, title="Deleted Combo")

    return message


def combo_adder():
    # A dictionary to store the new combo
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
        meal_cost = easygui.integerbox("How much does the meal cost? ($0.1-20)")
        combo_items[combo_meal] = float(meal_cost)
        combo_meal_counter += 1
        combo_item_num -= 1
    # Adds the combo meal info to the dictionary at the top
    combo[combo_name] = combo_items
    # Formats and prints the combo meal
    combos_text = f"Added combo:\n{combo_name}:\n"
    for meal, cost in combo_items.items():
        combos_text += f"{meal}: ${cost:.2f}\n"

    easygui.msgbox(combos_text, title="Added Combo")

    return combo


def combo_printer():
    added_message = ""

    delete_combo = easygui.buttonbox(msg="Do you want to delete a combo?", choices=["Yes", "No"])
    if delete_combo == "Yes":
        combo_deleter()

    add_combo = easygui.buttonbox(msg="Do you want to add a combo?", choices=["Yes", "No"])
    if add_combo == "Yes":
        added_combo = combo_adder()
        # Update existing_combos with added_combo
        existing_combos.update(added_combo)
        added_message = "Added Combo:\n\n"
        for combo, items in added_combo.items():
            added_message += f"{combo}:\n"
            for item, price in items.items():
                added_message += f"{item}: ${price:.2f}\n"
            added_message += "\n"

    # Display existing combos after removing deleted combos
    existing_combos_message = "Existing Combos:\n"
    for combo, items in existing_combos.items():
        existing_combos_message += f"{combo}:\n"
        for item, price in items.items():
            existing_combos_message += f"{item}: ${price:.2f}\n"
        existing_combos_message += "\n"

    # Print existing and added combos
    full_message = existing_combos_message + added_message
    easygui.msgbox(full_message, title="Summary")


combo_printer()
