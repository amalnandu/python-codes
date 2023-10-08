
# Python program to print the prime numbers between a range


def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True    


prime=[]
def listPrime(low,high):
    for i in range(low,high):
        if(isPrime(i)):
            prime.append(i)


x=int(input("Enter the lower bound "))
y=int(input("Enter the higher bound "))
listPrime(x,y)
print(prime)        


