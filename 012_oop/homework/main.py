# Your classes go here
class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species


    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

class Mammal(Animal):

    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.__fur_color = fur_color

    def fur_color(self):
        return self.__fur_color


class Bird(Animal):

    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.__wing_span = wing_span

    def wing_span(self):
        return self.__wing_span

class Reptile(Animal):

    def __init__(self, name, species, scale_type):
        super().__init__(name, species)
        self.__scale_type = scale_type

    def scale_type(self):
        return self.__scale_type


class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def list_animals(self):
        for animal in self.__animals:
            print(f'{animal.name} ({animal.species})')

    def count_animals(self):
        return len(self.__animals)

    def get_animals_by_species(self, species):
        species_list = []
        for animal in self.__animals:
            if animal.species == species:
                species_list.append(animal)
        return species_list

    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.name == name:
                self.__animals.remove(animal)
                return
        print(f'Animal with name {name} is not in Zoo')

    def feed_animals(self):
        for animal in self.__animals:
            if isinstance(animal, Mammal):
                print(f'Feeding {animal.name} ({animal.species}). It has {animal.fur_color()} fur.')
            elif isinstance(animal, Bird):
                print(f'Feeding {animal.name} ({animal.species}). It has {animal.wing_span()}mm wide wings.')
            elif isinstance(animal, Reptile):
                print(f'Feeding {animal.name} ({animal.species}). It has {animal.scale_type()} scales.')


# You can use code below for testing purpouses if you want
if __name__ == "__main__":
    zoo = Zoo()

    lion = Mammal('Simba', 'Lion', 'Golden')
    eagle = Bird('Baldy', 'Eagle', 100)
    python = Reptile('Monty', 'Python', 'Diamond')
    royal_python = Reptile('Muscle', 'Python', 'Triangle')

    zoo.add_animal(lion)
    zoo.add_animal(eagle)
    zoo.add_animal(python)
    zoo.add_animal(royal_python)

    print('Zoo animals:')
    zoo.list_animals()

    print('Feeding animals:')
    zoo.feed_animals()

    print('Removing animal:')
    zoo.remove_animal("Baldy")

    print('Zoo animals after removing:')
    zoo.list_animals()

    print('Total number of animals', zoo.count_animals())

    print('List all reptiles:')
    reptiles = zoo.get_animals_by_species('Python')
    for reptile in reptiles:
        print(f'{reptile.name} ({reptile.species})')