###Find all the primes between 2 and 10 million

import mincemeat
import math

#Finding primes less than sqrt(10 mil)
primes = []
p = int(math.sqrt(10000000)) + 1 
for i in xrange(2, p):
  y = 2
  while i % y != 0:
    y = y+1
  if y == i:
    primes.append(i)

#Breaking up the data to feed it to map jobs
data = {}

for i in range(1, 101):
  data[i] = (i* 100000, primes)
  

#Map function
def mapfn(k, (v, primes)):
  import math
  #All the numbers starting with an even number are ignored
  if (int(str(v-1)[0]) % 2 ==0 and not (v == 10000000)):
    return 
    
  x = v - 99999
  if x <2:
    x = 2
  
  #Checking for palindrome first and then checking for prime
  for i in xrange(x, v):
    stri = str(i)
    if stri == stri[::-1]:
      test = False
      primesqrt = int(math.sqrt(i))+1
      for m in primes:
        if (m < primesqrt and i % m == 0):
          test = True
          break
      
      if not test:
        yield "primes", i

#Reduce function
def reducefn(k, vs):
  return vs

s = mincemeat.Server()
s.datasource = data
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")


print results["primes"], len(results["primes"])

