class jedi:
    def __init__(self, name, lightsaberColor, rank):
        self.name = name
        self.lightsaberColor = lightsaberColor
        self.rank = rank

    def intro(self):
        print(f"i'm {self.name}. i'm a {self.rank} jedi, and my lightsaber is {self.lightsaberColor}.")

    def forcePush(self):
        print(f"{self.name} uses force push !")


obiwan = jedi("obi-wan kenobi","blue","master")
obiwan.intro()
obiwan.forcePush()

sonymeister = jedi("sonia","non-existent","master")
sonymeister.intro()
sonymeister.forcePush