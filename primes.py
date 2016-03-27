###Find all the primes between 2 and 10 million

import mincemeat

#Breaking up the data to feed it to map jobs
data = {}
for i in range(1, 701):
  data[i] = i* 10000

for j in range(1, 31):
  data[700 +j] = 7000000 + j *100000

#Map function
def mapfn(k, v):
  x = v - 9999
  if x <2:
    x = 2
  for i in xrange(x, v):
    y = 2
    p = str(i)
    if p == p[::-1]:
      while i % y != 0:
        y = y+1
      if y == i:
        yield k, i

#Reduce function
def reducefn(k, vs):
  return vs

s = mincemeat.Server()
s.datasource = data
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

p = []
for x in results.keys():
  for i in results[x]:  
    p.append(i)

p.sort()
print p

