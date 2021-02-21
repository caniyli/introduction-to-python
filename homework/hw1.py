#Hw1: Generating a 3x3 matrix with 9 random prime numbers

matrix = [[0,0,0],[0,0,0],[0,0,0]]
primenum = []
prime = True

#0-100 arasındaki asal sayılar liste haline getirildi
for i in range(2,100):
    for j in range(2,i):
        if i%j == 0:
            prime = False
    if prime==True:
        primenum.append(i)
    else:
        prime = True

#Elde edilen asal sayılar 3x3 matrix haline getirildi
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = primenum[(i*3)+j]

#Matrix ekrana yazdırıldı 
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = " ")
    print()

