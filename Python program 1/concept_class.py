class AiAgent:
    def __init__(self, name, role, goal):
        self.name = name
        self.role = role
        self.goal = goal
        self.memory = []

    def introduce(self):
        print(f"Hi, I am {self.name}, a {self.role} agent. My goal is to {self.goal}.")
        
    def add_to_memory(self, info):
        self.memory.append(info)

    def recall_memory(self):
        if self.memory:
            print("Recalling memory:")
            for item in self.memory:
                print(f"- {item}")
        else:
            print("No memories to recall.")
# Example usage
trader_agent = AiAgent("Alice", "trader", "maximize profits")
research_agent = AiAgent("Bob", "researcher", "discover new insights")
trader_agent.add_to_memory("Bought 100 shares of XYZ at $10.")
research_agent.add_to_memory("Found a new correlation between market trends.")

trader_agent.introduce()
trader_agent.recall_memory()

research_agent.introduce()
research_agent.recall_memory()