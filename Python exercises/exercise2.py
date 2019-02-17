import math

#What is the largest prime factor of the number 600851475143?

n=raw_input('Enter the integer you wish to find the prime factors of: ')

n = int(float(n))
L=[]

def too_small():
        """to be called for int < 4"""
        L.append(n)
        if n>0:
                L.append(1)
        return L

if n < 4: #alg only works for int > 4
        L = too_small()
        print L
        exit()

if n == 4: #because I'm lazy
        L.append(2)
        L.append(2)
        print L
        exit()

def primefactor():
        """prints list of all prime factors for int > 4"""
        test=True
        b=n
        while(test):
                i=2
                while((b%i!=0)&(i<(b/2))): #find next prime
                        i=i+1
                if i>=(b/2): #number is prime
                        L.append(b)
                        L.append(1)
                        test=False
                else: #number is not prime
                        a=(b/i)
                        L.append(i)
                        b=a
        return L

L = primefactor()
print L


exit()