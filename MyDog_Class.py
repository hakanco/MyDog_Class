import datetime

class MyDog:
    def __init__(self, breed, name, age, color, home_address):
        self.isAsleep = False
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.home_address = home_address

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

    @staticmethod
    def from_birthyear(birthyear):
        today_year = datetime.datetime.now().year
        return today_year - birthyear

    # @classmethod
    def move(self, destination):
        self.home_address = destination
        return f"We moved to {self.home_address}"

    @staticmethod
    def checkup_needed(age):
        return ((age - 1) % 3) == 0


dog1 = MyDog("golden", "dog_1", 2, "orange", "New York")
dog2 = MyDog("beagle", "dog_2", 1, "white", "Dallas")

# dog3 = MyDog.from_birthyear(2017) # "dog3", 5, "black", "LA",
# dog4 = MyDog.from_birthyear(2015) # "dog4", 4, "yellow", "LA"

dog1.info()
print(dog1.move("Dallas"))
# dog3.info()
# dog4.info()

# dog3.home_address

dog1.walk()
dog1.sleep()

dog2.eat("food")
dog2.sleep()

dog1.wake_up()
dog1.sleep()

dog1.info()
dog2.info()




