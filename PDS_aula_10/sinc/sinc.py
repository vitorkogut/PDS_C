import numpy 
import matplotlib.pyplot as plt


#data = numpy.memmap("PDS_aula_10/sinc/degrauun.pcm", dtype='h', mode='r')
data = numpy.ones(120)
Fc = float(input("Fc:"))

saida = numpy.ones(120)

pointer = 1

for pointer in range(len(data)):
    saida[pointer] = ((numpy.sin(2*numpy.pi*Fc*pointer))/(pointer*numpy.pi))

plt.plot(saida,'r')
plt.show()


with open('sinc.pcm', 'wb') as fid:
    numpy.array(saida, dtype=numpy.int16).tofile(fid)
fid.close()
