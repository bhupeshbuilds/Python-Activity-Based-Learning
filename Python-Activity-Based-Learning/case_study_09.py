schedule = [
    ("Python", 9, 10, "Lab-1"),
    ("Maths", 9, 11, "Room-2"),
    ("Web", 9, 10, "Lab-1"),
    ("English", 11, 12, "Room-2")
]
found = False
for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        s1, start1, end1, room1 = schedule[i]
        s2, start2, end2, room2 = schedule[j]
        overlap = start1 < end2 and start2 < end1
        if overlap and room1 == room2:
            print("Conflict:", s1, "and", s2, "in", room1)
            found = True
if not found:
    print("No room conflicts found")
