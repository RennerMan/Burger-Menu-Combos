import easygui


# Combo Deleter V1 created by James Renner

def original_combos():
    # A dictionary of all existing combos and their key pair (in this case, the value of the item)
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
    # Prompts users on the combo title
    combo_deleter = easygui.enterbox(msg="Type the name of the combo you want to delete\n"
                                         " (eg: Value, Cheesy, Super)").capitalize()

    # Loop until a valid combo name is entered
    while combo_deleter not in existing_combos:
        easygui.msgbox("Combo not found!", title="Error")
        combo_deleter = easygui.enterbox(msg="Type the name of the combo you want to delete,"
                                             " (eg: Value, Cheesy, Super").capitalize()

    # If correct, pop the combo and show user what combo was popped
    deleted_combo = existing_combos.pop(combo_deleter)
    # Asks user if their combo is correct. If not, the code asks the user to enter it again.
    message = f"Is this the correct combo? \n {combo_deleter}:\n"
    for item, price in deleted_combo.items():
        # Prints the combo items and their prices
        message += f"{item}: ${price:.2f}\n"
    confirmation = easygui.buttonbox(msg=message, choices=["yes", "no"])
    if confirmation == "no":
        easygui.msgbox("Try again:")
        original_combos()

    # Displays remaining combos to the user
    remaining_combos_message = "Remaining Combos:\n"
    for combo, items in existing_combos.items():
        remaining_combos_message += f"{combo}:\n"
        for item, price in items.items():
            remaining_combos_message += f"{item}: ${price:.2f}\n"
        remaining_combos_message += "\n"
    easygui.msgbox(remaining_combos_message, title="Remaining Combos")


original_combos()
