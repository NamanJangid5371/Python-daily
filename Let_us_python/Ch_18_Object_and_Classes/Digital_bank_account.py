class Robot:
    # Class Attribute (Shared by the whole factory)
    population = 0 

    def __init__(self, name):
        # Instance Attribute (Unique to each product)
        self.name = name 
        Robot.population += 1

# Creating instances
bot1 = Robot("Wall-E")
bot2 = Robot("Eve")

print(Robot.population)  # Output: 2
print(bot1.population)   # Output: 2 (bot1 looks up to its creator class)