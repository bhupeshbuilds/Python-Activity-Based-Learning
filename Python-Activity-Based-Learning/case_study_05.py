level = 40
capacity = 100
target = 80
target_day = None
for day in range(1, 4):
    inflow = int(input("Day " + str(day) + " inflow (litres): "))
    outflow = int(input("Day " + str(day) + " outflow (litres): "))
    level = level + inflow - outflow
    if level > capacity:
        print("Overflow detected")
        level = capacity
    if level < 0:
        print("Shortage detected")
        level = 0
    print("Water level:", level, "litres")
    if level >= target and target_day is None:
        target_day = day
if target_day is None:
    print("Target was not reached")
else:
    print("Target first reached on day", target_day)
