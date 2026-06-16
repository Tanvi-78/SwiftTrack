# SwiftTrack | Day 3: Student Analyzer
# Mission: Lists, Functions, Loops in Python

print("=== SwiftTrack Day 3 ===")

# Task 1: Student Data
students = ["Tanvi Dalvi", "Rahul Sharma", "Priya Patel", "Amit Kumar"]
sql_scores = [95, 76, 98, 65]

# Task 2: Find Topper
topper_index = sql_scores.index(max(sql_scores))
print(f"SQL Topper: {students[topper_index]} - {sql_scores[topper_index]} marks")

# Task 3: Function for Average
def calculate_average(scores):
    return sum(scores) / len(scores)

avg = calculate_average(sql_scores)
print(f"Class Average: {avg:.2f}")

# Task 4: Filter Students
print("\nStudents with Score > 80:")
for i in range(len(students)):
    if sql_scores[i] > 80:
        print(f"- {students[i]}")

print("\nDay 3 Complete! ✅")
