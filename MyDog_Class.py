class MyDog:
    def __init__(self, breed, name, age, color):
        self.isAsleep = False
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color

    def walk(self):
        print(f"{self.name} is walking")

    def eat(self, food):
        print(f"{self.name} is eating {food}!")

    def sleep(self):
        self.isAsleep = True
        print(f"{self.name} is sleeping!")

    def wake_up(self):
        self.isAsleep = False
        print(f"{self.name} is waking up!")

    def info(self):
        print(f"{self.breed} {self.name} {self.age} {self.color}")


dog1 = MyDog("golden", "dog_1", 2, "orange")
dog2 = MyDog("beagle", "dog_2", 1, "white")

dog1.walk()
dog1.sleep()

dog2.eat("food")
dog2.sleep()

dog1.wake_up()
dog1.sleep()

dog1.info()
dog2.info()










