import random as r

verbsAll = [# order goes Io, Tu, Lui/Lei, Noi, Voi, Loro, Meaning
            ["Avere", "Ho", "Hai", "Ha", "Abbiamo", "Avete", "Hanno", "To Have"],
            ["Essere", "Sono", "Sei", "E\'", "Siamo", "Siete", "Sono", "To Be"]
            ["Parlare", "Parlo", "Parli", "Parla", "Parliamo", "Parlate", "Parlano", "To Speak"],
            ["Studiare", "Studio", "Studi", "Studia", "Studiamo", "Studiate", "Studiano", "To Live"],
            
            ]

num = input("How many words do you want to practice:\n")
if (not num.isdigit()):
    num = len(verbsAll)
else:
    if (int(num) <= len(verbsAll)):
        num = int(num)
    else:
        num = len(verbsAll)

r.shuffle(verbsAll)

count = 0
correct = 0

for i in range(num):
    print("Word num " + str(i + 1) + ": " + verbsAll[i][0])
    
    io = input("What is the \"io\" form of the word?\n")
    count += 1
    if (io.lower() == verbsAll[i][1].lower()):
        correct += 1
        print("Correct!!!" + "\n")
    else:
        print("Wrong, it is " + verbsAll[i][1] + "\n")
        
    tu = input("What is the \"tu\" form of the word?\n")
    count += 1
    if (tu.lower() == verbsAll[i][2].lower()):
        correct += 1
        print("Correct!!!" + "\n")
    else:
        print("Wrong, it is " + verbsAll[i][2] + "\n")
    
    luiLei = input("What is the \"lui\\lei\" form of the word?\n")
    count += 1
    if (luiLei.lower() == verbsAll[i][3].lower()):
        correct += 1
        print("Correct!!!" + "\n")
    else:
        print("Wrong, it is " + verbsAll[i][3] + "\n")
    
    noi = input("What is the \"noi\" form of the word?\n")
    count += 1
    if (noi.lower() == verbsAll[i][4].lower()):
        correct += 1
        print("Correct!!!" + "\n")
    else:
        print("Wrong, it is " + verbsAll[i][4] + "\n")
        
    voi = input("What is the \"voi\" form of the word?\n")
    count += 1
    if (voi.lower() == verbsAll[i][5].lower()):
        correct += 1
        print("Correct!!!" + "\n")
    else:
        print("Wrong, it is " + verbsAll[i][5] + "\n")
        
    loro = input("What is the \"loro\" form of the word?\n")
    count += 1
    if (loro.lower() == verbsAll[i][6].lower()):
        correct += 1
        print("Correct!!!" + "\n")
    else:
        print("Wrong, it is " + verbsAll[i][6] + "\n")

print("You got a " + str(round(((correct) / count) * 10000) / 100) + "% with " + str(correct) + " correct out of " + str(count))