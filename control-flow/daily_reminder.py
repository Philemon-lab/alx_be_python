task = input("Enter your task:")
priority = input("priority (high/medium/low)").lower()
time_bound = input("Is this time bound? (yes/no)")

match priority:
    case "high":
        reminder = f"{task} is a high priority task."
    case "medium":
        reminder = f"{task} is medium priority task."
    case "low":
        reminder = f"{task} is a low priority task."
    case _:
        reminder = f"{task} has an unknown priority level"

if time_bound == "yes" and priority in ["high", "medium"]:
        reminder += "That requires immediate attention today.!"
else:
    reminder += "Consider competing it when you have free time."
print(f"nReminder:", reminder)