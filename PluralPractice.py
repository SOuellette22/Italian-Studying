import random as r

wordsAll = [# Male section of words
            ["Amico", "Amici"], ["Ragazzo", "Ragazzi"], ["Bambino", "Bambini"],
            ["Frantello", "Frantelli"], ["Cappuccino", "Cappuccini"], ["Gatto", "Gatti"],
            ["Giorno", "Giorni"], ["Libro", "Libri"], ["Albergo", "Alberghi"],
            ["Piatto", "Piatti"], ["Zio", "Zii"], ["Zaino", "Zaini"],
            ["Professore", "Professori"], ["Studente", "Studenti"], ["Dottore", "Dottori"],
            ["Padre", "Padri"], ["Bicchiere", "Bicchieri"], ["Latte", "Latti"],
            ["Cane", "Cani"], ["Mese", "Mesi"], ["Cinema", "Cinema"],
            ["Caffe\'", "Caffe\'"], ["Te\'", "Te\'"]
            
            # Female section fo words
            ["Amica", "Amice"], ["Ragazza", "Ragazze"], ["Bambina", "Bambine"],
            ["Sorella", "Sorelle"], ["Pizza", "Pizze"], ["Piazza", "Piazze"],
            ["Settimana", "Settimane"], ["Penna", "Penne"], ["Camera", "Camere"],
            ["Tazza", "Tazze"], ["Zia", "Zie"], ["Macchina", "Macchine"],
            ["Professoressa", "Professoresse"], ["Studentessa", "Studentesse"], ["Dottoressa", "Dottoresse"],
            ["Madre", "Madri"], ["Classe", "Classi"], ["Classe", "Classi"],
            ["Notte", "Notti"], ["Foto", "Foto"], ["Bici", "Bici"],
            ["Televisione", "Televisioni"], ["Stazione", "Stazioni"], ["Informazione", "Informazioni"],
            ["Lezione", "Lezioni"], ["Stagione", "Stagioni"], ["Universita\'", "Universita\'"],
            ["Citta\'", "Citta\'"]
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
    a = input("What is the plural version of this word?\n")
    if (a.lower() == wordsAll[i][1] or 
        a.upper() == wordsAll[i][1]):
        print("Correct!!!")
        correct += 1
    else:
        print("Wrong")

print("You got a " + str(round((correct / count) * 10000) / 100) + "% with " + str(correct) + " correct out of " + str(count))