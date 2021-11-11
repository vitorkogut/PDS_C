import numpy 
import matplotlib.pyplot as plt


#data = numpy.memmap("degrauun.pcm", dtype='h', mode='r')

M = int(input("M:"))
M = M+1

w = numpy.zeros(M)

w_hamming = numpy.zeros(M)

for pointer in range(len(w)):
     w[pointer] = 0.42 - (0.5 * (numpy.cos((2*numpy.pi*pointer)/M))) + (0.08 * (numpy.cos((4*numpy.pi*pointer)/M)))  


for i in range(len(w_hamming)):
     w_hamming[i] = 0.54 - (0.46 * (numpy.cos((2*numpy.pi*i)/M))) 



plt.subplot(2, 1, 1)
plt.title("Hamming")
plt.plot(w_hamming, 'r')
plt.grid()

plt.subplot(2, 1, 2)
plt.title("Black")
plt.plot(w, 'r')
plt.grid()

plt.tight_layout()
plt.show()
 
with open('hammingeblackman.pcm', 'wb') as fid:
    numpy.array(w, dtype=numpy.int16).tofile(fid)
fid.close()
