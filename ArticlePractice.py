import random as r

wordsAll = [# Male section of words Singular
            ["Amico", "un", "l\'", "M"], ["Ragazzo", "un", "il", "M"], ["Bambino", "un", "il", "M"],
            ["Frantello", "un", "il", "M"], ["Cappuccino", "un", "il", "M"], ["Gatto", "un", "il", "M"],
            ["Giorno", "un", "il", "M"], ["Libro", "un", "il", "M"], ["Albergo", "un", "l\'", "M"],
            ["Piatto", "un", "il", "M"], ["Zio", "uno", "lo", "M"], ["Zaino", "uno", "lo", "M"],
            ["Professore", "un", "il", "M"], ["Studente", "uno", "lo", "M"], ["Dottore", "un", "il", "M"],
            ["Padre", "un", "il", "M"], ["Bicchiere", "un", "il", "M"], ["Latte", "un", "il", "M"],
            ["Cane", "un", "il", "M"], ["Mese", "un", "il", "M"], ["Cinema", "un", "il", "M"],
            ["Caffe\'", "un", "il", "M"], ["Te\'", "un", "il", "M"], ["Alto", "un", "l\'", "M"],
            ["Simpatico", "un", "il", "M"], ["Sportivo", "uno", "lo", "M"], ["Pigro", "un", "il", "M"],
            ["Timido", "un", "il", "M"], ["Bravo", "un", "il", "M"], ["Creativo", "un", "il", "M"],
            ["Onesto", "un", "l\'", "M"], ["Estroverso", "un", "l\'", "M"],
            
            # Male section of words Plural
            ["Amici", "i", "M"], ["Ragazzi", "i", "M"], ["Bambini", "i", "M"],
            ["Frantelli", "i", "M"], ["Cappuccini", "i", "M"], ["Gatti", "i", "M"],
            ["Giorni", "i", "M"], ["Libri", "i", "M"], ["Alberghi", "gli", "M"],
            ["Piatti", "i", "M"], ["Zii", "gli", "M"], ["Zaini", "gli", "M"],
            ["Professori", "i", "M"], ["Studenti", "gli", "M"], ["Dottori", "i", "M"],
            ["Padri", "i", "M"], ["Bicchieri", "i", "M"], ["Latti", "i", "M"],
            ["Cani", "i", "M"], ["Mesi", "i", "M"], ["Cinema", "i", "M"],
            ["Caffe\'", "i", "M"], ["Te\'", "i", "M"],
            
            # Female section fo words
            ["Amica", "un\'", "l\'", "F"], ["Ragazza", "una", "la", "F"], ["Bambina", "una", "la", "F"],
            ["Sorella", "una", "la", "F"], ["Pizza", "una", "la", "F"], ["Piazza", "una", "la", "F"],
            ["Settimana", "una", "la", "F"], ["Penna", "una", "la", "F"], ["Camera", "una", "la", "F"],
            ["Tazza", "una", "la", "F"], ["Zia", "una", "la", "F"], ["Macchina", "una", "la", "F"],
            ["Professoressa", "una", "la", "F"], ["Studentessa", "una", "la", "F"], ["Dottoressa", "una", "la", "F"],
            ["Madre", "una", "la", "F"], ["Classe", "una", "la", "F"], ["Classe", "una", "la", "F"],
            ["Notte", "una", "la", "F"], ["Foto", "una", "la", "F"], ["Bici", "una", "la", "F"],
            ["Televisione", "una", "la", "F"], ["Stazione", "una", "la", "F"], ["Informazione", "un\'", "l\'", "F"],
            ["Lezione", "una", "la", "F"], ["Stagione", "una", "la", "F"], ["Universita\'", "un\'", "l\'", "F"],
            ["Citta\'", "una", "la", "F"], ["Alta", "un\'", "l\'", "F"],
            ["Simpatica", "una", "la", "F"], ["Sportiva", "una", "la", "F"], ["Pigra", "una", "la", "F"],
            ["Timida", "una", "la", "F"], ["Brava", "una", "la", "F"], ["Creativa", "una", "la", "F"],
            ["Onesta", "un\'", "l\'", "F"], ["Estroversa", "un\'", "l\'", "F"],
            
            ["Amice", "le", "F"], ["Ragazze", "le", "F"], ["Bambine", "le", "F"],
            ["Sorelle", "le", "F"], ["Pizze", "le", "F"], ["Piazze", "le", "F"],
            ["Settimane", "le", "F"], ["Penne", "le", "F"], ["Camere", "le", "F"],
            ["Tazze", "le", "F"], ["Zie", "le", "F"], ["Macchine", "le", "F"],
            ["Professoresse", "le", "F"], ["Studentesse", "le", "F"], ["Dottoresse", "le", "F"],
            ["Madri", "le", "F"], ["Classi", "le", "F"], ["Classi", "le", "F"],
            ["Notti", "le", "F"], ["Foto", "le", "F"], ["Bici", "le", "F"],
            ["Televisioni", "le", "F"], ["Stazioni", "le", "F"], ["Informazioni", "le", "F"],
            ["Lezioni", "le", "F"], ["Stagioni", "le", "F"], ["Universita\'", "le", "F"],
            ["Citta\'", "le", "F"]
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
countP = 0
countS = 0

correctmf = 0
correctun = 0
correctil = 0
correctilPlural = 0

def guesting(flag, n):
    if (flag == "yes"):
        if (n == 3):
            a = input("What is the words gender:\n")
        elif (n == 1):
            a = input("What is the \"un\" article (un,uno,una,un\'):\n")
        elif (n == 2):
            a = input("What is the \"il\" article (il,lo,la,l\'):\n")
        if (wordsAll[i][n].lower() == a.lower()):
            print("Correct!!!\n")
            return True
        else:
            print("Wrong, it is " + wordsAll[i][n] + "\n")
            return False
        
def guestingPlurals(flag, n):
    if(flag == "yes"):
        if(n == 2):
            a = input("What is the words gender:\n")
        elif(n == 1):
            a = input("what is the the \"the\" article plural:\n")
        if(wordsAll[i][n].lower() == a.lower()):
            print("Correct!!!\n")
            return True
        else:
            print("Wrong, it is "  + wordsAll[i][n] + "\n")
            return False

print()

mfFlag = input("Do you want to study the gender of the words? Only yes or no\n")
print()
unFlag = input("Do you want to study the \"a/an\" articles (uno,un,una,un')? Only yes or no\n")
print()
ilFlag = input("Do you want to study the \"the\" articles (il,lo,la,l')? Only yes or no\n")
print()
pluralIlFlag = input("Do you want to study the plural \"the\" article (i, gli, le)? Only yes or no\n")

print()

for i in range(num):
    if (len(wordsAll[i]) == 4):
        countS += 1
        count += 1
        if(mfFlag == "yes"):
            print("Word num " + str(i + 1) + ": " + wordsAll[i][0])
            if(guesting(mfFlag, 3)):
                correctmf += 1
        if(unFlag == "yes"):
            print("Word num " + str(i + 1) + ": " + wordsAll[i][0])     
            if(guesting(unFlag, 1)):
                correctun += 1
        if(ilFlag == "yes"):      
            print("Word num " + str(i + 1) + ": " + wordsAll[i][0])
            if(guesting(ilFlag, 2)):
                correctil += 1
            
    if (len(wordsAll[i]) == 3):
        countP += 1
        count += 1
        if(mfFlag == "yes"):
            print("Word num " + str(i + 1) + ": " + wordsAll[i][0])
            if(guestingPlurals(mfFlag, 2)):
                correctmf += 1
        if(pluralIlFlag == "yes"):
            print("Word num " + str(i + 1) + ": " + wordsAll[i][0])
            if(guestingPlurals(pluralIlFlag, 1)):
                correctilPlural += 1

if (mfFlag == "yes"):
    print("You got a " + str(round((correctmf / count) * 10000) / 100) + "% with " + str(correctmf) + " correct out of " + str(count) + " for gendering words")
if (unFlag == "yes"):
    print("You got a " + str(round((correctun / countS) * 10000) / 100) + "% with " + str(correctun) + " correct out of " + str(countS) + " for \"un/una\" article")
if (ilFlag == "yes"):
    print("You got a " + str(round((correctil / countS) * 10000) / 100) + "% with " + str(correctil) + " correct out of " + str(countS) + " for \"lo/la\" article")
if (pluralIlFlag == "yes"):
    print("You got a " + str(round((correctilPlural / countP) * 10000) / 100) + "% with " + str(correctil) + " correct out of " + str(countP) + " for \"i/le\" plural article")