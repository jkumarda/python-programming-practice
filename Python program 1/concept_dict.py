agent_profile = {
    "name": "Alpha-1",
    "role": "Research Assistant",
    "version": "1.0",
    "capabilities": ["Data Analysis", "Report Generation", "Task Management"],
    "status": "Active"
}
print(f"Agent Name: {agent_profile['name']}")
print(f"Role: {agent_profile['role']}")
print(f"Version: {agent_profile['version']}")
print(f"Capabilities: {', '.join(agent_profile['capabilities'])}")

print(f"Status: {agent_profile.pop('status')}")  # This removes 'status' from the dictionary and prints it
print(f"Updated Agent Profile: {agent_profile}")
print(f"Status : {agent_profile.get('status', 'Status information not available')}")  # This will show a default message since 'status' was removed

agent_profile['status'] = "Active"  # Re-adding status to the dictionary
print(f"Re-added Status: {agent_profile['status']}")

for key, value in agent_profile.items():
    print(f"{key.capitalize()}: {value}")

agent_profile['capabilities'].append("Machine Learning")  # Adding a new capability to the list
print(f"Updated Capabilities: {', '.join(agent_profile['capabilities'])}")

agent_profile["status"] ="Back and Better than ever!"  # Updating the status value
print(f"Updated Status: {agent_profile['status']}")
