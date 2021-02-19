import json
from difflib import get_close_matches

data = json.load(open("./../data.json"))

def translate(w):
    w = w.lower()
    y = w.capitalize()
    if w in data:
        return data[w]
    elif y in data:
        return data[y]
    elif w.upper() in data:
        return data[w.upper()]
    elif  len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn== "N":
            return "The word doesn't exist.Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist.Please double check it"

word = input("Enter Word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)