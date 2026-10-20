units = int(input("Enter units consumed: "))
if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5
    bill = energy + 50
    if units > 300:
        bill = bill * 1.05
    print("Energy charge: Rs.", round(energy, 2))
    print("Total bill: Rs.", round(bill, 2))
