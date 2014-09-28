#!coding: utf-8
# PEP - как правильно писать питоновский код
# здесь о функции неизвестно
# pass пустой оператор
# функция как объект
# функцию можно передавать присваивать
def this_is_my_function():
    print "Function"
    return "return_value"

f = this_is_my_function

s = f()
print s