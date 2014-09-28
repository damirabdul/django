#!coding: utf-8

for i in range(100):
	print i

while i<100:
	print i
	i += 1

#Первая много места
#в генераторе нет ретурна,есть yield

def f():
    i = 0
    while i < 100:
        yield i # вызывает работу до след yield
        i += 1

# Вместо этого
for i in xrange(100):
    print i
