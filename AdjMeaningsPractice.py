import random as r

wordsAll = [# All words will be in there masculine forms is they can have both
            ["Alto", "Tall"], ["Simpatico", "Nice"], ["Sportivo", "Sporty"], 
            ["Pigro", "Lazy"], ["Timido", "Shy"], ["Bravo", "Good at"], 
            ["Creativo", "Creative"], ["Onesto", "Honest"], ["Estroverso", "Outgoing"],
            ["Fame", "Hungry"], ["Sete", "Thirsty"], ["Sonno", "Sleepy"],
            ["Caldo", "Hot"], ["Freddo", "Cold"], ["Ragione", "Right"],
            ["Intelligente", "Smart"], ["Socievole", "Social"], ["Responsabile", "Responsible"],
            ["Gentle", "Kind"], ["Giovane", "Young"], ["Sensible", "Sensitive"]
            ]

num = input("How many words do you want to practice:\n")
if (not num.isdigit()):
    num = len(wordsAll)
else:
    if (int(num) <= len(wordsAll)):
        num = int(num)
    else:
        num = len(wordsAll)

r.shuffle(wordsAll)

count = 0
correct = 0

for i in range(num):
    print("Word num " + str(i + 1) + ": " + wordsAll[i][0])
    count += 1
    a = input("What does this word mean?\n")
    if (a.lower() == wordsAll[i][1].lower()):
        print("Correct!!!")
        correct += 1
    else:
        print("Wrong")

print("You got a " + str(round((correct / count) * 10000) / 100) + "% with " + str(correct) + " correct out of " + str(count))