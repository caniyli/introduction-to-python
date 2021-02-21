'''
Hw3:Write two functions.
The name of the first function is prime_first
The name of the second function is prime_second
You must use these two functions inside the for loop. Ensure that the for loop takes values between 0-1000
Press the prime numbers between 0-500 on the screen with the prime_first function
Press the prime numbers between 500-1000 on the screen with the prime_second function
'''

def prime_first(num):
    prime = True
    if(num <= 1):
        return
    for i in range(2,num):
        if(num % i==0):
            prime = False
            return
    if prime == True:
        print(f"{num} prime_first ile ekrana yazdırıldı")

def prime_second(num):
    prime = True
    for i in range(2,num):
        if(num % i==0):
            prime = False
    if prime == True:
        print(f"{num} prime_second ile ekrana yazdırıldı")

for i in range(0,1001):
    if(i<=500):
        prime_first(i)
    else:
        prime_second(i)

