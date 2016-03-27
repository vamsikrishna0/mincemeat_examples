###Find count, sum and stddev of data by reading from a file

import mincemeat
import sys
import math
import time

filename = sys.argv[1]

f = open(filename, 'r')

#Getting data from files
data = {}
i ,j = 0, 0
for line in f:
   if line.strip(): 
       i = i +1
       if i%10 == 0:
         j = j+1
       if j in data:
         data[j].append(line)
       else:
         data[j] = [line]     

datasource = data

#Map function
def mapfn(k, v):
    import time
    add, count, sum_sq = 0, 0, 0
    dat = {}
    for p in v:
        w = int(p)
        #time.sleep(1)
        #print w
        add = add + w
        count = count + 1
        sum_sq = sum_sq + (w * w)
    
    dat["sum"] = add
    dat["count"] = count
    dat["sum_sq"] = sum_sq
    for i in dat:
      yield i, dat[i]

#Reduce function
def reducefn(k, vs):
    add = sum(vs)
    return add

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

add = s.run_server(password="changeme")

#Standard deviation formula
stddev = math.sqrt((add["sum_sq"]/add["count"]) - ((add["sum"]/add["count"]) ** 2))
add["stddev"] = stddev
del add["sum_sq"]

for i in add.keys():
  print str(i)+":"+str(add[i])


