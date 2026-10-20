data = float(input("Data used (GB): "))
minutes = int(input("Call minutes used: "))
plans = [
    ("Plan A", 199, 2, 100, 20, 1),
    ("Plan B", 299, 5, 200, 15, 0.50),
    ("Plan C", 399, 10, 300, 10, 0.25)
]
costs = []
for name, fee, data_limit, call_limit, data_rate, call_rate in plans:
    extra_gb = max(0, int(data - data_limit + 0.999))
    extra_minutes = max(0, minutes - call_limit)
    total = fee + extra_gb * data_rate + extra_minutes * call_rate
    costs.append((name, total))
    print(name, "cost: Rs.", round(total, 2))
best = min(costs, key=lambda item: item[1])
print("Cheapest plan:", best[0], "at Rs.", round(best[1], 2))