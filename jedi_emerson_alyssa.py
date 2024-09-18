class Jedi:
    def __init__ (name, lightsaber_color, rank):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank

def introduce(self):
    print(f"I'm {self.name}, a {self.rank} Jedi. My lightasber is {self.lightsaber_color}")

def force_push(self):
    print(f"{self.name} uses Force Push!")

obiwan = Jedi("Obi-Wan Kenobi", "blue", "master")
obiwan.introduce()
obiwan.force_push()

emerson = Jedi("Alyssa", "blue", "student")
emerson.introduce()
emerson.force_push

#Change?
