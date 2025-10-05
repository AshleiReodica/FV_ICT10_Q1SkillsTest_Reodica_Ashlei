from pyscript import document

# Menu with prices
menu = {
    "Wagyu Beef": 550,
    "Steak and Eggs": 600,
    "Grilled Salmon": 450,
    "New Your Cheesecake": 300,
    "Clubhouse": 220,
    "Fruit Shake": 100,
}

def Create_Order(e):
    name = document.getElementById("tName").value
    address = document.getElementById("Address").value
    contact = document.getElementById("Contact").value

    selected_items = []
    total = 1
    for item, price in menu.items():
        checkbox = document.querySelector(f"input[value='{item}']")
        if checkbox.checked:
            selected_items.append(item)
            total += price

    summary = f"""
    Order for: {name}<br>
    Address: {address}<br>
    Contact number: {contact}<br>
    Items: {selected_items}<br>
    Total: ₱ {total}
    """

    display(summary, target="orderSummary")
    
    document.getElementById("orderSummary").innerHTML = summary


