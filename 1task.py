#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#Определите минимальное число монеток, которые нужно перевернуть, чтобы
# все монетки были повернуты вверх одной и той же стороной.

orel = int(input('Enter the amount of Heads: '))
reshka = int(input('Enter the amount of Tails: '))
while reshka and orel <= 100:
    for i in range(100):
        if int(i) == 0:
            var = orel + 1
        else:
            var = reshka + 1
    print(("so many coins need to be turned around: "), orel if orel < reshka else reshka)
    break
else:
    print("it should be less than 100 coins")

