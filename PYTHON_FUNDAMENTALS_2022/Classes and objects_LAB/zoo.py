class Zoo:
    __animals = 0


    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):

        if species == "mammal":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)
        Zoo.__animals += 1


    def get_info(self, species_):
        self.species_ = species_
        result = ""
        if species_ == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species_ == "fish":
            result += f"Fish in {self.name}: {', '.join(self.fishes)}\n"
        elif species_ == "bird":
            result += f"Bird in {self.name}: {', '.join(self.birds)}\n"

        result += f" Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)
info = input()
print(zoo.get_info(info))




