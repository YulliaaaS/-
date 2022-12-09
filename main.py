f = open("text.txt")

word_f = input("Введіть слово--> ")

p = False
for lines in f.read().split("\n\n"):
    if word_f in lines:
        print(f"---------\n{lines}")
        p = True
if p == False:
    print("Такого слова немає!")
