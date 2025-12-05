task = input("Enter your daily task: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()
match priority:
    case "high":
        reminder = f" '{task}' is a HIGH priority task."
    case "medium":
        reminder = f" '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f" '{task}' is a LOW priority task."
    case _:
        reminder = f" '{task}' has an UNKNOWN priority level."
if time_bound == "yes":
    reminder += " that requires timely attention!"
else:
    if priority in ["high", "medium", "low"]:
        reminder  = f"Note: {reminder} consider completing it when you have free time soon."
print("\nReminder:", reminder)