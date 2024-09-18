class Jedi:
    def __init__(self, name, lightsaber_color, rank):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank

    def introduce(self):
        print(f"I am {self.name}, a {self.rank} Jedi. My lightsaber is {self.lightsaber_color}.")

    def force_push(self):
        print(f"{self.name} uses Force Push!")


# Create a Jedi object
slicer = Jedi("Skibidi Slicer", "red", "Master")
slicer.introduce()
slicer.force_push()

carson = Jedi("Carson Pugh", "Purple", "Initiate")
carson.introduce()
carson.force_push()

