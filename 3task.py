#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
#Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 10**6).

n = int(input('enter a number: '))
i = 1
while i <= n:
    i = i + 1
    if n % i == 0:
        print(i)
        break


