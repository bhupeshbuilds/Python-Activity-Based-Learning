subtotal = 0
for i in range(1, 4):
    price = float(input("Enter price of item " + str(i) + ": "))
    quantity = int(input("Enter quantity: "))
    if price < 0 or quantity < 0:
        print("Invalid item values")
        break
    subtotal += price * quantity
else:
    discount = subtotal * 0.10 if subtotal >= 1000 else 0
    taxable = subtotal - discount
    tax = taxable * 0.05
    total = taxable + tax
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))
    print("GST: Rs.", round(tax, 2))
    print("Final bill: Rs.", round(total, 2))