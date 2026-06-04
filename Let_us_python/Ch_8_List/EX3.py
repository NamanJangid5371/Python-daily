class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.bread = breed

    def bark(self):
        return f"{self.name} says Woof!"