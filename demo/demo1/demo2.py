class Animal(object):
    def eat(self):
        print('动物要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Peopl(object):
    def eat(self):
        print('人都吃')


def fun(animal):
    animal.eat()


fun(Dog())
fun(Peopl())
fun(Animal())