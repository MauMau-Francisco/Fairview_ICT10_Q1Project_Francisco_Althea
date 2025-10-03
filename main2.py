from pyscript import document


#summarize order
def generate_order(event):
    # strings
    name = document.getElementById("name").value
    number = document.getElementById("number").value
    location = document.getElementById("location").value

    # if user left empty
    if not name:
        name = "Blank"
    if not number:
        number = "Blank"
    if not location:
        location = "Blank"

    # escape codes
    profile = f""" Customer Information:
Name\n: \"{name}\"
Number\n:\t{number}
Location\n: {location}

Summary:
Order for:{name}.\n We will call you at: {number}.\n You are located at: {location}.\nWe hope you enjoy your order!\
"""

    document.getElementById("output").innerHTML = profile


menu = {
    "Pesto Pasta": 170,
    "Tomato Premium Pasta": 220,
    "Scallop Pasta": 230,
    "Leche Flan Special": 60.00,
    "Grape Juice": 40.00
}

order_items = []
total_price = 0

def calculate_order(event):
    menu = {
    "Pesto Pasta": 170,
    "Tomato Premium Pasta": 220,
    "Scallop Pasta": 230,
    "Leche Flan Special": 60.00,
    "Grape Juice": 40.00
    }

    order_items = []
    total_price = 0

    for item, price in menu.items():
        checkbox = document.getElementById(item)
        if checkbox.checked:
            order_items.append(f"{item.capitalize()} (₱{price})")
            total_price += price

    if not order_items:
        outcome = "No food selected."
    else:
        outcome = "<br>".join(order_items) + f"<br><b>Total: ₱{total_price}</b>"

    document.getElementById("compute").innerHTML = outcome
