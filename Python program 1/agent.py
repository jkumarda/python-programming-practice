agent_memory = {
    "name" : "Nexus",
    "tasks":["greet user", "ask for inputs"]
}

print(f"{agent_memory['name']}: is online and ready to assit!!")
new_task = input("Hi user enter your new task.")
if new_task.strip():
    agent_memory['tasks'].append(new_task)
    print("Task added suucessfully!")
else:
    print("No task entered. Skipping...")

print(f"All tasks to be done by {agent_memory['name']} are the following:")

for index, task in enumerate(agent_memory["tasks"],1):
    print(f"{index}. {task}")
