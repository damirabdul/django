#!coding: utf-8
# декораторы (что то типа AOP)

#это декоратор
def sandwich(somefood):  # функция объект

    def wrapper():
        print "Bread"
        somefood()
        print "Bread"

    return wrapper


def food():
    print "Meat"

food()

food = sandwich(food)

food()


