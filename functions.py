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



student_grades = {"Mary":9.1,"Mari":9.2,"Mari3":9.3}
print(mean(student_grades))