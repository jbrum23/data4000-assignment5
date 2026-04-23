# --- Functions ---

def get_student_key():
    student_key = input("Student key: ")
    seed = sum(ord(ch) for ch in student_key.strip())
    return seed

def get_item_name():
    while True:
        name = input("Enter item name (or DONE to finish): ").strip()
        if name.upper() == "DONE":
            return "DONE"
        elif name == "":
            print("Item name cannot be empty. Please try again.")
        else:
            return name

def get_unit_price():
    while True:
        try:
            price = float(input("Enter unit price: "))
            if price <= 0:
                print("Unit price must be greater than 0. Please try again.")
            else:
                return price
        except ValueError:
            print("Invalid price. Please enter a number.")

def get_quantity():
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty < 1:
                print("Quantity must be at least 1. Please try again.")
            else:
                return qty
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

def apply_discount(total_units, subtotal):
    if total_units >= 10 or subtotal >= 100:
        return 10
    else:
        return 0

def apply_perk(seed, total):
    if seed % 2 != 0:
        total -= 3.00
        if total < 0:
            total = 0.00
        return total, "YES"
    else:
        return total, "NO"


seed = get_student_key()

subtotal = 0.0
total_units = 0

while True:
    item_name = get_item_name()

    if item_name == "DONE":
        break

    price = get_unit_price()
    quantity = get_quantity()

    subtotal += price * quantity
    total_units += quantity

discount_percent = apply_discount(total_units, subtotal)
discounted_total = subtotal * (1 - discount_percent / 100)

discounted_total, perk_applied = apply_perk(seed, discounted_total)

print(f"Seed: {seed}")
print(f"Units: {total_units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount_percent}%")
print(f"Perk applied: {perk_applied}")
print(f"Total: ${discounted_total:.2f}")