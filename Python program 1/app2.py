# Initialize our agent's memory
agent_memory = {
    "name": "Nexus",
    "tasks": ["Initialize system", "Greet user"] # This is a List inside a Dictionary!
}

print(f"--- {agent_memory['name']} Agent Online ---")

# 1. Show the current tasks
print(f"Current Task List: {agent_memory['tasks']}")

# 2. Let the user add a new task
new_task = input("What new task should I add to my list? ")

# 3. Use .append() to add the item to the end of the list
if new_task.strip():
    agent_memory['tasks'].append(new_task)
    print("Task added successfully!")
else:
    print("No task entered. Skipping...")

# 4. Final report using a 'for loop' to go through the list
print(f"\nUpdated Task Schedule for {agent_memory['name']}:")
for index, task in enumerate(agent_memory['tasks'], 1):
    # This prints the number and the task name
    print(f"{index}. {task}")
