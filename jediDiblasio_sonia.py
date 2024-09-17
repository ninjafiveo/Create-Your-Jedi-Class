class Jedi:
    def __init__(self, name, lightsaberColor, rank):
        self.name = name
        self.lightsaberColor= lightsaberColor
        self.rank = rank

    def introduce(self):
        print(f"i'm {self.name}. i'm a {self.rank} jedi, and my lightsaber is {self.lightsaberColor}.")

    def force_push(self):
        print(f"{self.name} uses force push !")

# Example Jedi
obiwan = Jedi("Obi-Wan Kenobi", "blue", "master")
obiwan.introduce()
obiwan.force_push()

sony = Jedi("sonia", "n/a", "master")
sony.introduce()
sony.force_push()
