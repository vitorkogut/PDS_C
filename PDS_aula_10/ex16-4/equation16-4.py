import numpy 
import matplotlib.pyplot as plt

M = int(input("M:"))
K = int(input("K:"))
fc = float(input("Fc:"))
a = M/2
h = numpy.zeros(M)

for i in range(len(h)):
     if(i==a): 
          h[i] = (2*numpy.pi*fc)*K
     else: 
          h[i] = K * (numpy.sin(2*numpy.pi*fc*(i-a))/(i-a)) * ((0.42 - 0.5 * numpy.cos((2*numpy.pi)*i/M)) + 0.08*numpy.cos((4*numpy.pi*i)/M))
   
plt.plot(h, 'r')
plt.grid()

plt.tight_layout()
plt.show()
 
with open('sinc.pcm', 'wb') as fid:
    numpy.array(h, dtype=numpy.int16).tofile(fid)
fid.close()
