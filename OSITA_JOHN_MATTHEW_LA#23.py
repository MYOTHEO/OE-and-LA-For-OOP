class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()  
            print("This character is amazing!")
        return wrapper

character = AnimeCharacter("Naruto", "Rasenshuriken")

@character.introduce
def character_intro():
    print(f"I am {character.name} and I can use {character.ability}.")
character_intro()

