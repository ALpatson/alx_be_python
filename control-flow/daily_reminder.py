"""Instructions:

Prompt for a Single Task:

Ask the user to input a task description and save it into a task variable
Prompt for the task’s priority (high, medium, low) and save it into a priority variable
In a time_bound variable, Ask if the task is time-bound (yes or no)
Process the Task Based on Priority and Time Sensitivity:

Use a Match Case statement to react differently based on the task’s priority.
Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
Provide a Customized Reminder:

Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
A message should be ‘that requires immediate attention today!’"""

# task_reminder.py

task = input("Enter your task description: ")
priority = input("What's the priority of the task (high, medium, low): ").lower()
time_bound = input("Is your task time-bound (yes or no): ").lower()

match priority:
    case "high":
        message = f"Note: '{task}' is a high priority task. Consider completing it as soon as possible."
    case "medium":
        message = f"Note: '{task}' is a medium priority task. Try to schedule time for it soon."
    case "low":
        message = f"Note: '{task}' is a low priority task. You can plan it for later."
    case _:
        message = f"Note: '{task}' has an unknown priority. Please check again."

if time_bound == "yes":
    message += " This task requires immediate attention today!"

print(message)
