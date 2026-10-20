budget = float(input("Travel budget in Rs.: "))
rate = float(input("Rupees per 1 unit of foreign currency: "))
categories = ["Hotel", "Food", "Transport"]
expenses = []
for category in categories:
    amount = float(input(category + " expense in foreign currency: "))
    converted = amount * rate * 1.02
    expenses.append((category, converted))
total = sum(item[1] for item in expenses)
largest = max(expenses, key=lambda item: item[1])
print("Converted expenses including 2% fee:")
for category, amount in expenses:
    print(category, ": Rs.", round(amount, 2))
print("Total: Rs.", round(total, 2))
print("Largest expense:", largest[0])
print("Budget status:", "Over budget" if total > budget else "Within budget")
