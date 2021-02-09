response = ''

def sentence_maker(phrase):
    interrogatives = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        result.append(sentence_maker(user_input))

temps = [221,234,340,230]

new_temp=[temp/10 for temp in temps]
new_temp2=[temp/10 for temp in temps if temp != -9999]
new_temp3=[temp/10 if temp != -9999 else 0 for temp in temps ]

def mean(*args):
    return sum(args)/len(args)

def mean2(**args):
    return args

print(mean2(a=1,b=2))
print(" ".join(results))