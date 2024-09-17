class jedi():
    def __init__(self, name, lightsaber_color, rank):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank

    def introduce(self):
        print(f"I am {self.name}, a {self.rank} Jedi. My lightsaber is {self.lightsaber_color}.")

    def force(self):
        print(f"{self.name}, May the force be with you.")
    


# The characters
jar_jar_binks = jedi("Jar Jar Binks", "Red", "Master")
jar_jar_binks.introduce()
jar_jar_binks.force()

din_djarin = jedi("Din Djarin", "Black", "Mandalorian")
din_djarin.introduce()
din_djarin.force()