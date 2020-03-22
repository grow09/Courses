from abc import abstractclassmethod, abstractmethod


class Animal(object):
    def Animal(self, name, food, location):
        self.name = name
        self.food = food
        self.location = location

    @abstractmethod
    def makeNoise(self):
        print("животное орёт")

    @abstractmethod
    def eat(self):
        print("животное ест")

    @abstractmethod
    def sleep(self):
        print("животное спит")

class Dog(Animal):
    def makeNoise(self):
        return "%s гавкает" % self.name

    def eat(self):
        return "%s ест %s" % (self.name, self.food)

    def sleep(self):
        return "%s спит %s" % (self.name, self.location)

class Cat(Animal):
    def makeNoise(self):
        return "%s мурчит" % self.name

    def eat(self):
        return "%s ест %s" % (self.name, self.food)

    def sleep(self):
        return "%s спит %s" % (self.name, self.location)

class Horse(Animal):
    def makeNoise(self):
        print("Иго-го")

    def eat(self):
        return "%s ест %s" % (self.name, self.food)

    def sleep(self):
        return "%s спит %s" % (self.name, self.location)

class Veterinar(Animal):
    def threatAnimal(self):
        return "%s ест %s и живёт %s" % (self.name, self.eat, self.location)



if __name__ == "__main__":
    animals = [
        ["Собака", "кость", "в будке"],
        ["Кот", "мышей", "в доме"],
        ["Конь", "травку", "на улице"]]
    for i in range(len(animals)):
        p3 = Veterinar()
        p3.Animal(animals[i][0], animals[i][1], animals[i][2])
        print(p3.threatAnimal())
