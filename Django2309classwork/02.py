#!coding: utf-8

lst = [i*i for i in xrange(10)]
print lst

#maximum = max([int(raw_input()) for i in xrange(int(raw_input()))])
#print maximum

lst2 = [i*i for i in xrange(10) if i % 2]
print lst2

s = [1,2,3,4]
if 3 in s:
    print "YES"

s = "Suleyman"

if "man" in s:
    print "YES"