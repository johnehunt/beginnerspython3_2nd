def night_out(p):
    p.eat()
    p.drink()
    p.sleep()


class Person:
    def eat(self): print('Person - Eat')

    def drink(self): print('Person - Drink')

    def sleep(self): print('Person - Sleep')


class Employee(Person):
    def eat(self): print('Employee - Eat')

    def drink(self): print('Employee - Drink')

    def sleep(self): print('Employee - Sleep')


class SalesPerson(Employee):
    def eat(self): print('SalesPerson - Eat')

    def drink(self): print('SalesPerson - Drink')


class Dog:
    def eat(self): print('Dog - Eat')

    def drink(self): print('Dog - Drink')

    def sleep(self): print('Dog - Sleep')


