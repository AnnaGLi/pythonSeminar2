8#ребуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.//
# В единственной строке входного файла INPUT.TXT записано единственное целое число N,
# не превышающее по абсолютной величине 10 в 4 степени.range (1, N)

n = int(input("Enter a number: "))
count = 0
result = 0
while n < 10 ** 4:
    if count <= n:
        result = result + count
        count = count + 1
        print(result)
else:
    print('Enter a smaller number')
