def calculate_bill(items, quantities):
    total = sum(items[item] * quantities[item] for item in quantities if item in items)
    return total

def calculate_discount_gst(total, discount_rate=10, gst_rate=5):
    discount = (discount_rate / 100) * total
    gst = (gst_rate / 100) * (total - discount)
    return discount, gst

def final_amount(total, discount, gst):
    return total - discount + gst

def generate_bill(items, quantities):
    total = calculate_bill(items, quantities)
    discount, gst = calculate_discount_gst(total)
    final_amt = final_amount(total, discount, gst)
    print("\n------Priya Computers------")
    print("\n1/12,Ghandi road,Madurai-626004\nPh no. 987463536273")
    print("\n----- Final Bill -----")
    for item in quantities:
        if item in items:
            print(f"{item} (x{quantities[item]}) - Rs.{items[item] * quantities[item]:.2f}")
    print(f"Total: Rs.{total:.2f}")
    print(f"Discount: Rs.{discount:.2f}")
    print(f"GST: Rs.{gst:.2f}")
    print("-----------------------------")
    print(f"Final Amount: Rs.{final_amt:.2f}")
    print("-----------------------------")

items = {
    "Tv": 50000,
    "Phone": 40000,
    "Watch": 4500,
    "Headphone": 1500,
    "Mouse": 600
}

quantities = {}
n = int(input("Enter number of items you want to purchase: "))
for _ in range(n):
    item = input("Enter item name: ").strip()
    qty = int(input("Enter quantity: "))
    if item in items:
        quantities[item] = qty
    else:
        print(f"{item} is not available.")

generate_bill(items, quantities)
