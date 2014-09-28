#!coding: utf-8
class A(object):  # у него нет родителя, то есть object
    def __init__(self):
        print "Parent"

    def f(self):
        print 1

class B(A): # наследование

    def __init__(self):
        super(B,self).__init__()# Вызов родительского конструктора
        print "Child"

    def f(self):
        super(B,self).f()
        print 2

b = B()
b.f()
