#!coding: utf-8
class Student:
    def __init__(self,name):
        self.name = name
    def f(self):
        self.__age = 20
    def g(self):
        print self.__age
    def __str__(self):
        return "Student:"+ self.name
    def __call__(self):
        print "Calling "+self.name

s = Student("RomaPasha")
s.f()
s.g()
print dir(s)
print s
s()
#print s._Student__age # не рекомендуется