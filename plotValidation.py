from array import array
import numpy as np
import matplotlib.pyplot as plt

x = array('f',[])
x0 = array('f',[])
x1 = array('f',[])
r = array('f',[])
r_min = array('f',[])
x_index=2
x0_index=0
x1_index=1
r_index=3 
r_min_index=7

f = open('results_BESS_TEV.dat')
for line in f : 
    line = line[:-1]
    line = line.replace(' ','')
    words = line.split('&')
    x.append(float(words[x_index]))
    r.append(float(words[r_index]))
    r_min.append(float(words[r_min_index]))
    x0.append(float(words[x0_index]))
    x1.append(float(words[x1_index]))
    #print words

r_scaled = map(lambda a,b,c,d,e:(b+c)*(e-d),x,r,r_min,x0,x1)
r_norm = map(lambda a,b,c:(b+c)*a**2.5,x,r,r_min)

#print x
print r_scaled

print "integral of scale rates:",sum(r_scaled)

plt.plot(x,r_scaled)
#plt.plot(x,r_norm)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('momentum')
plt.ylabel('Rate/m^2/s/sr')
#plt.legend(['rate/GeV','rate'])
plt.show()

