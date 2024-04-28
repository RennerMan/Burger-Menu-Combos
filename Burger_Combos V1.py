# Burger Combos V1 created by James Renner
# The assembled version of my code

import easygui

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
    # Shows user their deleted combo
    message = f"Deleted combo:\n{combo_eraser}:\n"
    for item, price in deleted_combo.items():
        # Prints the combo items and their prices
        message += f"{item}: ${price:.2f}\n"
    combo_deleter_confirmation = easygui.buttonbox(msg=f"{message}\nIs this correct?", choices=["Yes", "No"])
    if combo_deleter_confirmation == "No":
        combo_deleter()
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
        meal_cost = easygui.enterbox("How much does the meal cost? ($0.1-20)")
        combo_items[combo_meal] = float(meal_cost)
        combo_meal_counter += 1
        combo_item_num -= 1
    # Adds the combo meal info to the dictionary at the top
    combo[combo_name] = combo_items
    # Formats and prints the combo meal
    combos_text = f"Added combo:\n{combo_name}:\n"
    for meal, cost in combo_items.items():
        combos_text += f"{meal}: ${cost:.2f}\n"
    combo_adder_confirmation = easygui.buttonbox(msg=f"{combos_text}\nIs this correct?", choices=["Yes", "No"])
    if combo_adder_confirmation == "No":
        combo_adder()
    return combo


def combo_printer():
    added_message = ""
    user_input = ""  # Initialize user_input
    # Loop until the user chooses to quit
    while user_input != "Quit":
        # Asks user what action they want to take
        user_input = easygui.buttonbox(msg="Welcome! What would you like to do?\n",
                                       choices=["Add Combo", "Delete Combo", "Print Existing Combos",
                                                "Print Updated Combos", "Quit"])
        if user_input == "Delete Combo":
            combo_deleter()

        # Asks user if they want to add a combo or not
        if user_input == "Add Combo":
            added_combo = combo_adder()
            # Updates existing combos with the added combo
            existing_combos.update(added_combo)
            added_message = "Added Combo:\n\n"
            for combo, items in added_combo.items():
                added_message += f"{combo}:\n"
                for item, price in items.items():
                    added_message += f"{item}: ${price:.2f}\n"
                added_message += "\n"

        # Print existing and added combos
        if user_input == "Print Existing Combos":
            message = ""
            for combo, items in existing_combos.items():
                message += f"{combo}:\n"  # Adds combo title on a new line
                for item, price in items.items():
                    # Prints the combo on a new line below the combo name
                    message += f"{item}: ${price:.2f}\n"
                message += "\n"
            easygui.msgbox(message, title="Existing Combos")

        # Print updated combos
        if user_input == "Print Updated Combos":
            updated_message = ""
            for combo, items in existing_combos.items():
                updated_message += f"{combo}:\n"  # Adds combo title on a new line
                for item, price in items.items():
                    # Prints the combo on a new line below the combo name
                    updated_message += f"{item}: ${price:.2f}\n"
                updated_message += "\n"
            updated_message += added_message
            easygui.msgbox(updated_message, title="Updated Combos")

    if user_input == "Quit":
        easygui.msgbox("Have a nice day!")


combo_printer()
