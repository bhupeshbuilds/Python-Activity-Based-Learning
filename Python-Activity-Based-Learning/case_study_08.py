vehicle = input("Vehicle (car/bike): ").lower()
entry = int(input("Entry hour (0-23): "))
exit_time = int(input("Exit hour (0-23): "))
if vehicle not in ("car", "bike") or not (0 <= entry <= 23 and 0 <= exit_time <= 23):
    print("Invalid input")
else:
    duration = exit_time - entry if exit_time >= entry else 24 - entry + exit_time
    if duration == 0:
        duration = 24
    hours = int(duration) if duration == int(duration) else int(duration) + 1
    rate, limit = (30, 200) if vehicle == "car" else (15, 100)
    fee = min(hours * rate, limit)
    print("Parking hours charged:", hours)
    print("Parking fee: Rs.", fee)
