n = 0
e = 0
d = 0

def isPrime(number):
 factor = 2
 while factor <= number // factor:
  if number % factor == 0:
   return 0
  factor += 1
 return number > 1
 
def getPrime(start):
 while True:
  if isPrime(start):
   return start
  start += 1
 return -1

def gcd(a, b):
 return a if b == 0 else gcd(b, a % b)

'''
(x * inv) % mod = 1 
x * inv = mod * alpha + 1 
inv = ((mod * alpha) + 1)/x
'''
def modinverse(x, mod):
 alpha = 1
 while True:
  value = mod * alpha + 1
  if value % x == 0:
   return value // x
  alpha += 1
  
def getEncryptedKey(eular):
 e = 2
 while e < eular:
  if gcd(e, eular) == 1:
   break
  e += 1
 return e
 
def fastPower(a, b, mod):
 result = 1
 while b != 0:
  if b % 2 == 1:
   result = (result * a) % mod
  b //= 2
  a = (a * a) % mod 
 return result

def encrypt(M, e, n):
 return fastPower(M, e, n) 

def decrypt(c, d, n):
 return fastPower(c, d, n)

def genKeys():
 global n, e, d
 start = 2**16
 p = getPrime(start)
 q = getPrime(p * p)
 n = p * q
 eular = (p-1) * (q-1)
 e = getEncryptedKey(eular)
 d = modinverse(e, eular)
 if e == d:
  d += eular

genKeys()
print(n, e, d)
