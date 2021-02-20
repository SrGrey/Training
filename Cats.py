# The code below is my solution for test's task 
# this solution was not verified by advanced Python developer so could smell bad :P   But it looks working
#
# Task description:
''' Write the classes:

AbstractCat class, which is initialized with no arguments. Is able to:
*eat* eat. For every 10 units of food, the weight increases by 1 unit until it becomes 100, and does not grow further. If at one meal the amount of food is not a multiple of 10, the remainder is stored, and then added to the new meal.
- return a string representation as <Class name> (weight).

Kitten class, inherited from cat with weight argument. Knows how to meow subtly:
*meow* returns the string "meow ..."
It also knows how to sleep *sleep* returns the string Snore, repeated as many times as the number 5 fits in the weight.

Class Cat, inherited from a kitten with weight and name arguments. Knows how to meow loudly (meow):
"MEOW ..."
and return your name (get_name). Also knows how to catch mice:
*catch_mice** returns a string: Got it! '''

class AbstractCat:
    # grow limit
    max_weight = 100

    def __init__(self):
        self.food = 0
        self.weight = 0

    def eat(self, food=0):
        self.food += food
        self.weight = min(self.max_weight, self.food // 10)
        return self.weight

    def __str__(self):
        return  f'{self.__class__.__name__}  ({self.weight})'

class Kitten(AbstractCat):
    def __init__(self, weight = 0):
        self.weight = weight
        self.food = self.weight * 10
        
    # I could write founction *meow* for every class and it could be shortly, but I was experimenting with OOP´s Inheritance
    def meow(self):
        meow = 'meow...'
        if self.__class__ == Cat:
            return meow.upper()
        else:
            return meow

    def sleep(self):
        return 'Snore'*(self.weight // 5)

class Cat(Kitten):
    def __init__(self, weight, name):
        self.name = name
        self.weight = weight

    def get_name(self):
        return  f'{self.name}'

    def catch_mice(self):
        return 'Got it!'


abscat = AbstractCat()
abscat.eat(125)
abscat.eat(17)
print(abscat)
kit = Kitten(21)
print(kit.sleep())
cat = Cat(83, 'Molly')
print(cat.meow())
print(cat.get_name())
print('*'*100)
kit = Kitten(15)
kit.eat(24)
print(kit)
cat = Cat(41, 'Molly')
print(cat.catch_mice())
print(cat)
