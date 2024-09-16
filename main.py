# This is the starter file for the Create Your Jedi Class lab.
# Students will create their own jedi_lastname_firstname.py file with their custom Jedi class.

print("Welcome to the Jedi Academy!")

# Example of a Jedi class that students will extend in their own file
class Jedi:
    def __init__(self, name, lightsaber_color, rank):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank

    def introduce(self):
        print(f"I am {self.name}, a {self.rank} Jedi. My lightsaber is {self.lightsaber_color}.")

    def force_push(self):
        print(f"{self.name} uses Force Push!")

# Example Jedi
obiwan = Jedi("Obi-Wan Kenobi", "blue", "Master")
obiwan.introduce()
obiwan.force_push()
