###Find the passwords from the hashed value (using md5)

import mincemeat
import sys

from itertools import product
from string import ascii_lowercase

hash2crack = sys.argv[1]

#Generating all possible passwords
x = ascii_lowercase
for i in range(10):
  x = x + str(i)

keywords4 = [''.join(i) for i in product (x, repeat = 4)]
keywords3 = [''.join(i) for i in product (x, repeat = 3)]
keywords2 = [''.join(i) for i in product (x, repeat = 2)]
keywords1 = [''.join(i) for i in product (x, repeat = 1)]

keywords = keywords1 + keywords2 + keywords3 + keywords4

#Making them into lists 
lists = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
r = lists(keywords, 46656)

for i in r:
  i.append(hash2crack)
  
data = dict(enumerate(r))

#Map function
def mapfn(k, v):
    import hashlib
    
    for i in v: 
      p = hashlib.md5(i).hexdigest()      
      if p[:5] == v[-1]:
        print p[:5]
        yield "actual", i    

#Reduce function
def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = data
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
