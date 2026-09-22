class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    
    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    def heal(self,points):

        self.health= self.health+ points

        print(f"{self.name} heals {points} points. New health: {self.health}." )

        
    

    # TODO: Define attack method and implement it

    # TODO: Define heal method and implment it
     

# TODO: Create superhero instance
Catwomen= SuperHero("Catwoman", "Agility", 120)

Catwomen.attack()
Catwomen.heal(10)

# TODO: Use the attack() and heal() method
