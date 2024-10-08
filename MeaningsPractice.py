import random as r

wordsAll = [# All words will be in there masculine forms is they can have both
            ["Alto", "Tall"], ["Simpatico", "Nice"], ["Sportivo", "Sporty"], 
            ["Pigro", "Lazy"], ["Timido", "Shy"], ["Bravo", "Good at"], 
            ["Creativo", "Creative"], ["Onesto", "Honest"], ["Estroverso", "Outgoing"],
            ["Fame", "Hungry"], ["Sete", "Thirsty"], ["Sonno", "Sleepy"],
            ["Caldo", "Hot"], ["Freddo", "Cold"], ["Ragione", "Right"],
            ["Intelligente", "Smart"], ["Socievole", "Social"], ["Responsabile", "Responsible"],
            ["Gentle", "Kind"], ["Giovane", "Young"], ["Sensible", "Sensitive"],
            ["Lunedi", "Monday"], ["Martedi", "Tuesday"], ["Mercoledi", "Wednesday"],
            ["Giovedi", "Thursday"], ["Venerdi", "Friday"], ["Sabato", "Saturday"],
            ["Domenica", "Sunday"], ["Oggi", "Today"], ["Domani", "Tomorrow"],
            ["Gennaio", "January"], ["Febbraio", "February"], ["Marzo", "March"],
            ["Aprile", "April"], ["Maggio", "May"], ["Giugno", "June"],
            ["Luglio", "July"], ["Agusto", "August"], ["Settembre", "September"],
            ["Ottobre", "October"], ["Novembre", "November"], ["Dicembre", "December"],
            ["Studente", "Student"], ["Caffe\'", "Coffee"], ["Professore", "Professor"],
            ["Ristorante", "Restaurant"], ["Notte", "Night"], ["Classe", "Class"],
            ["Stagione", "Season"], ["Informazione", "Information"], ["Stazione", "Station"],
            ["Dottore", "Doctor"], ["Cinema", "Movie Theater"], ["Foto", "Picture"],
            ["Bici", "Bike"], ["Amico", "Friend"], ["Libro", "Book"],
            ["Ragazzo", "Male"], ["Ragazza", "Female"]
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
        print("Correct!!!\n")
        correct += 1
    else:
        print("Wrong, it is " + wordsAll[i][1] + "\n")

print("You got a " + str(round((correct / count) * 10000) / 100) + "% with " + str(correct) + " correct out of " + str(count))