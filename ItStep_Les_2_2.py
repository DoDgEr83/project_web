class Animal:
    def __init__(self, name, age, wight, sex):
        self.name = name
        self.sex = sex
        self.wight = wight
        self.age = age

    def great(self):
        pass

    def jump(self):
        print(f"{self.name} can jump")


class Dog(Animal):
    def great(self):
        print(f"{self.name} said Bau")


class Cat(Animal):
    def great(self):
        print(f"{self.name} said Miau")


cat = Cat("Max", 15, 18, 'm')
cat.great()
cat.jump()
