# Day 2: Multiple Expense Tracker using While Loop
# Mission: Track 3 expenses and show total

print("=== SwiftTrack Day 2 ===")
total = 0
count = 1

while count <= 3:
    expense = float(input(f"Enter expense {count}: "))
    total += expense
    count += 1

print(f"-------------------------")
print(f"Total expenses today: Rs {total}")
print("Day 2 Complete! ✅")
