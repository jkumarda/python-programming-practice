agent_name = "Jarvis"

user_name = input("Enter your name:")

if user_name.strip():
    print(f"[{agent_name}]: Hello, {user_name}! I am here to assit you.")
else:
    print(f"[{agent_name}]: I didn't catch your name. Anyway I am here to help you.")


print("System Status: Online and waiting for commands.")