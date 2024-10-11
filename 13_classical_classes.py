"""
Task 0: Class We Do

Create a class for a video game character, that tracks it health,
    - Create method for damage and healing

Then create a subclass called 'Player' that has more health
    - Create a method for healing
"""

class Character:
    health = 20

    def __init__(self, name):
        self.name = name

    def damage(self, dmg=1):
        self.health = self.health - dmg


class Player(Character):
    health = 50

    def heal(self):
        if self.health < 50:
            self.health = self.health + 1


enemy1 = Character("Balthazar")
enemy1.damage()
print(f"Enemy health is {enemy1.health}")

player1 = Player("Ashley")
player1.damage(5)
player1.heal()
print(f" Player health {player1.health}")


"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("Hi, my name is " + self.name + " and I am ", self.age, " years old.")

greeting = Person("Fred", 30)

greeting.intro()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

    
dog_sound = Dog()
cat_sound = Cat()

dog_sound.speak()
cat_sound.speak()




"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, owner="Bob", amount=6):
        self.balance = self.balance + amount
        print(f"Hi {owner}! You deposited ${amount}. Your new balance is: ${self.balance}")


    def withdraw(self, owner="Bob", amount=4):
        self.balance = self.balance - amount
        print(f"Hi {owner}! You withdrew ${amount}. Your new balance is: ${self.balance}")

transaction = BankAccount("Bob", 50)

transaction.deposit("Charlie", 14)
transaction.withdraw()

