class Jedi:
    def __init__(self, name, lightsaber_color,rank):
        self.name= name
        self.lightsaber_color = lightsaber_color
        self.rank=-rank

    def introduce(self):
        print(f"I am{self.name}, a {self.rank} Jedi.  My lightsaber is {self.lightsaber_color}.")

    def force_push(self):
        print(f"{self.name}uses Force push!")


# Create a jedi object 
obiwan = Jedi("Obi-Wan Kenobi", "blue","Master")
obiwan.introduce()
obiwan.force_push 

buchanan =Jedi("richi", "purple","Master")