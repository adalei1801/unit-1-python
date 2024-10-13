"""
Task 0: Class We Do

Create a class for a video game character, that tracks it health,
    - Create method for damage and healing

Then create a subclass called 'Player' that has more health
    - Create a method for healing
"""

class Character:
    # Creates class for character
    health = 20

    def __init__(self, name):
        # Function that initializes the name argument
        self.name = name

    def damage(self, dmg=1):
        # Creates function to calculate function and sets optional argument for damage
        self.health = self.health - dmg
        # Subtracts damage value from health value


class Player(Character):
    # Creates subclass for player from character
    health = 50

    def heal(self):
        # Function to calculate healing and health
        if self.health < 50:
            # Creates if statement for health being less than 50
            self.health = self.health + 1
            # Adds 1 to health value


enemy1 = Character("Balthazar")
# Assigns class to variable with argument value
enemy1.damage()
# Calls function using variable 
print(f"Enemy health is {enemy1.health}")

player1 = Player("Ashley")
# Assigns subclass to variable with argument variable
player1.damage(5)
# Calls function using variable and assigns value to argument
player1.heal()
# Calls function using variable
print(f" Player health {player1.health}")


"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

class Person:
    # Creates class called person to hold person name and age
    def __init__(self, name, age):
        # Function that initializes name and age
        self.name = name
        self.age = age
    
    def intro(self):
        # Function that holds the introduction statement
        print("Hi, my name is " + self.name + " and I am ", self.age, " years old.")

greeting = Person("Fred", 30)
# Assigns class to variable and assigns values to argumentd

greeting.intro()
# Calls function

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

class Animal:
    # Creates class for subclasses
    def speak(self):
        pass
    # Function that holds animal sounds in subclass


class Dog(Animal):
    # Creates subclass for Dog from Animal class
    def speak(self):
        print("woof")
        # Function that prints dog sound 

class Cat(Animal):
    # Creates subclass for Cat from Animal class
    def speak(self):
        print("meow")
        # Function that prints Cat sound

    
dog_sound = Dog()
cat_sound = Cat()
# Assigns subclasses to variables

dog_sound.speak()
cat_sound.speak()
# Calls subclasses functions



"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class BankAccount:
    # Creates class for bank account 
    def __init__(self, owner, balance):
        # Function that initializes owner and balance arguments
        self.owner = owner
        self.balance = balance

    def deposit(self, owner="Bob", amount=6):
        # Creates function that does desposits and sets optional arguments for owner and amount
        self.balance = self.balance + amount
        # Adds amount to balance and assigns the sum to variable
        print(f"Hi {owner}! You deposited ${amount}. Your new balance is: ${self.balance}")


    def withdraw(self, owner="Bob", amount=4):
        # Creates function that runs withdraws and sets optional arguments for owner and amount
        self.balance = self.balance - amount
        # Subtracts amount from the balance and assigns the difference to variable
        print(f"Hi {owner}! You withdrew ${amount}. Your new balance is: ${self.balance}")

transaction = BankAccount("Bob", 50)
# Assigns class to variable with argument values

transaction.deposit("Charlie", 14)
# Calls deposit function with argument values

transaction.withdraw()
# Calls withdraw function

