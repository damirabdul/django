#!coding: utf-8
# * - позиционые аргументы, ** - именованные аргументы
def f(*args,**kargs):
    for item in args:
        print item
    for item in kargs.keys():
        print item, kargs[item]

f(1,2)
f(1,2,3,4)
f(n = 2, m = 3)