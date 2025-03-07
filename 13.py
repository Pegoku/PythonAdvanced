from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        return f"Soc un {self.especie} de {self.edat} anys."

class Cavall(Animal):
    def xerrar(self):
        return "Hiii"

    def mourem(self):
        return "Galopar"

class Dofi(Animal):
    def xerrar(self):
        return "Cliquet"

    def mourem(self):
        return "Nedar"

class Abella(Animal):
    def xerrar(self):
        return "Bzzz"

    def mourem(self):
        return "Volar"

    def picar(self):
        return "Picar"

class Huma(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        return "Hola"

    def mourem(self):
        return "Caminar"

class Fiet(Huma):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares

    def nompares(self):
        return f"Els meus pares són: {', '.join(self.pares)}"

class Centaure(Cavall, Huma):
    def __init__(self, especie, edat, nom):
        Cavall.__init__(self, especie, edat)
        Huma.__init__(self, especie, edat, nom)

    def xerrar(self):
        return "Hiii i Hola"

    def mourem(self):
        return "Galopar i Caminar"

class Xou:
    def xerrar(self):
        return "Xou Xou"

    def mourem(self):
        return "Moure's"

    def quisoc(self):
        return "Soc un Xou"

animals = [
    Cavall("Cavall", 5),
    Dofi("Dofi", 8),
    Abella("Abella", 1),
    Huma("Huma", 30, "Joan"),
    Fiet("Huma", 10, "Pere", ["Joan", "Maria"]),
    Centaure("Centaure", 15, "Hèrcules"),
    Xou()
]

for animal in animals:
    print(animal.quisoc())
    print(animal.xerrar())
    print(animal.mourem())
    print()