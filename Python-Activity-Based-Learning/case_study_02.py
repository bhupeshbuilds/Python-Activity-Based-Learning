distance = float(input("Journey distance (km): "))
fuel_price = float(input("Fuel price per litre: "))
vehicles = [("Vehicle A", 12), ("Vehicle B", 15), ("Vehicle C", 20)]
costs = []
if distance <= 0 or fuel_price < 0:
    print("Invalid distance or fuel price")
else:
    for name, mileage in vehicles:
        fuel = (distance / mileage) * 1.10
        cost = fuel * fuel_price
        costs.append((name, cost))
        print(name, "fuel with 10% reserve:", round(fuel, 2), "litres")
        print(name, "journey cost: Rs.", round(cost, 2))
    best = min(costs, key=lambda item: item[1])
    print("Lowest-cost vehicle:", best[0], "Rs.", round(best[1], 2))