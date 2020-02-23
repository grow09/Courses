class Person(object):
    def Person(self, fullName, age):
        self.fullName = fullName
        self.age = age

    def Person_(self, *args):
        self.fullName = "Игорь"
        self.age = 20

    def move(self):
        return "%s ходит" % self.fullName

    def talk(self):
        return "%s говорит" % self.fullName


if __name__ == "__main__":
    p1 = Person()
    p1.Person("gRow", 21)
    p2 = Person()
    p2.Person("Alex", 22)
    print(p1.move())
    print(p2.talk())
    p3 = Person()
    p3.Person_()
    print(p3.move())

