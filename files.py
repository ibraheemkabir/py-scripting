import time
import os
import pandas

while True:
    if os.path.exists("./../temps_today.csv"):
        data = pandas.read_csv("./../temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("file does not exist")
            
while True:
    if os.path.exists("./../friuts.txt"):
        with open("./../friuts.txt") as file:
            print(file.read())
    else:
        print("file does not exist")
    time.sleep(10)



myfile = open("./../fruits.txt")

print(myfile.read())

content = myfile.read()

myfile.close()

with open('./../fruits.txt') as myfile:
    content = myfile.read()
    
print(content)

with open('./../vegetables.txt',"w") as myfile:
    myfile.write('tomato\ncucumeber\ntomato2\n')
    myfile.write('garlic')

with open('./../vegetables.txt',"a") as myfile:
    myfile.write('garlic')
with open('./../vegetables.txt',"a") as myfile:
    myfile.write('garlic')
