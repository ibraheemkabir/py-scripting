from __future__ import print_function
import datetime

x = 10
y = '10'
print(x+x)
print(y+y)

u = 10
i = '30'

sum1 = u + u
sum2 = i + i

print(x+x)
print(y+y)
print(sum1,sum2)

print(type(x))
mynow = datetime.datetime.now()
print(mynow)
'hello'.upper()

grades = [9.1,8.8,7.5]
student_grades = {'marry':9.1,"sim":8.9}
grades.count(9.1)
mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum/length

monday_temperatures = (1,4,5)

tup = 'tuple is an ordered collection of objects'

tuesday_temperatures = [9.1, 8.8, 7.5]

seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]

seconds.remove(1.4534345567, 1.023458894, 1.10001399445)

tuesday_temperatures.index(8.8)
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]

tuesday_temperatures[1:2]
tuesday_temperatures[1:]
tuesday_temperatures[-1]

mystring = 'hello'

mystring[0]

print(serials[0], serials[2], serials[5])
print(monday_temperatures)
print(mean)