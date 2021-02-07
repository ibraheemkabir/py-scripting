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
mysum = sum(grades)
length = len(grades)
mean = mysum/length
print(mean)