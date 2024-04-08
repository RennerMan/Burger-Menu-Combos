import easygui


# Existing Combos V1 using dictionaries, created by James Renner
# The code is contained in a function to make assembling into the final code easier
def original_combos():
    # A list of all existing combos and their key pair (in this case, the value of the item)
    existing_combos = {
        "Value": {
            "Beef burger": 5.69,
            "Fries": 1,
            "Fizzy drink": 1
        },
        "Cheezy": {
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
# Asks the user if they want to print out the menu or not. The Easygui buttonbox ensures no errors are made.
    print_menu = easygui.buttonbox(msg="Do you want to print out the menu? (y/n)", choices=["yes", "no"])
# If the user wants to print the menu, it loops the existing combo dictionary to show each combo and their prices.
    if print_menu == "yes":
        for combo, items in existing_combos.items():
            message = f"{combo}:\n"  # Adds combo title on a new line
            for item, price in items.items():
                # Prints the combo
                message += f"{item}: ${price:.2f}\n"
            easygui.msgbox(message, title=combo)
    elif print_menu == "no":
        easygui.msgbox("Have a great day!")


# Call the function to execute the code
original_combos()
