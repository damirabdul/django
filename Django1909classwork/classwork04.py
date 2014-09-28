#!coding: utf-8
def d(day=20,month=9,year = 2014):
   # print "Date is : "+ str(day) + \
   #       "-" + str(month) + "-" + str(year)  # wrong!!
   print "Date is: %s-%s-%s" % (day,month,year)


d(year=2010)