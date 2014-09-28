#!coding: utf-8
import math

lst = range(10)

result_lst = map(math.exp, lst) # одной функций применили функцию к списку
print result_lst

#                      old version
#def check3(n):
#    return (n % 3 == 0)
#result_lst2 = filter(check3,lst)

#                      new version

result_lst2 = filter(lambda x: x % 3 == 0,lst)
print(result_lst2)

