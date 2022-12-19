class Zoo :
    __animals = 0

    def __init__(self, name) :
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name) :
        if species == 'mammal' :
            self.mammals.append(name)
        elif species == 'fish' :
            self.fishes.append(name)
        elif species == 'bird' :
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species) :

        if species == 'mammal' :
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == 'fishe' :
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == 'bird' :
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
animals = int(input())
zoo = Zoo(zoo_name)

for animal in range(animals) :
    species, name = input().split()
    zoo.add_animal(species,name)

needed_species = input()
print(zoo.get_info(needed_species))
