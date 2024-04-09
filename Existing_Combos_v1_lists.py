import easygui

# Existing Combos V1 using lists, created by James Renner
# The code is contained in a function to make assembling into the final code easier
def original_combos():
    existing_combos = [
        ["Value:", ["Beef burger", "$5.69"], ["Fries", "$1"], ["Fizzy drink", "$1"]],
        ["Cheezy:", ["Cheeseburger", "$6.69"], ["Fries", "$1"], ["Fizzy drink", "$1"]],
        ["Super", ["Cheeseburger", "$6.69"], ["Large Fries", "$2"], ["Smoothie", "$2"]]
    ]

    # Loops each combo and prints it on a separate line
    for combo in existing_combos:
        easygui.msgbox("\n".join(map(str, combo)))

original_combos()
