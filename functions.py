def mean(mylist):
    if type(mylist) == dict:
        the_mean = sum(mylist.values())/len(mylist)
    else: 
        the_mean = sum(mylist) / len(mylist)
    return the_mean

def foo(ounce):
    ml = ounce * 29.57353
    return ml

isinstance(3,int)

def weather_Condtion(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"
    
name = input('please enter your name:')

message = "Hello %s" % name

for letter in 'hello':
    print(letter.titile())
    
print(message)

username = ''
while username != 'pypy':
    username = input("Enter username: ")
    
user_input = input('Enter temp:')