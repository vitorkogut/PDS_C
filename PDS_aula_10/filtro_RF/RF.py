import numpy 
import matplotlib.pyplot as plt
from scipy import signal as sf

Xa = numpy.zeros(4999)
Ya = numpy.zeros(4999)

Fs = int(input("Fs: "))
Fca = int(input("Fcb: "))
Fca = float(Fca/Fs)
Bw = int(input("Bw: "))
M = int(4/(Bw/Fs))

Ha = numpy.zeros(M)


for i in range(len(Ha)):
    if(i - M/2) == 0:
        Ha[i] = 2 * numpy.pi * Fca
    if(i - M/2) != 0:
        Ha[i] = numpy.sin(2 * numpy.pi * Fca * (i - M/2)) / (i - M/2)
    Ha[i] = Ha[i] * (0.54 - 0.46 * numpy.cos(2 * numpy.pi * i / M))

SUM = 0

for i in range(len(Ha)): 
    SUM += Ha[i]

for i in range(len(Ha)):
    Ha[i] = Ha[i]/SUM



for j in range(100,4999):
    Ya[j] = 0
    for i in range(len(Ha)):
        Ya[j] = Ya[j] + Xa[j - i] * Ha[i]


for k in range(M):
    Ha[k] = Ha[k] * -1
    if( k == M/2):
        Ha[k] = 1 - Ha[k]




X = numpy.zeros(4999)
Y = numpy.zeros(4999)

fc = int(input("Fca: "))
fc = float(fc/Fs)


H = numpy.zeros(M)


for i in range(len(H)):
    if(i - M/2) == 0:
        H[i] = 2 * numpy.pi * fc
    if(i - M/2) != 0:
        H[i] = numpy.sin(2 * numpy.pi * fc * (i - M/2)) / (i - M/2)
    H[i] = H[i] * (0.54 - 0.46 * numpy.cos(2 * numpy.pi * i / M))

SUM = 0

for i in range(len(H)): 
    SUM += H[i]

for i in range(len(H)):
    H[i] = H[i]/SUM



for j in range(100,4999):
    Y[j] = 0
    for i in range(len(H)):
        Y[j] = Y[j] + X[j - i] * H[i]



Rf = numpy.zeros(M)

for l in range(M):
    Rf[l] = H[l] + Ha[l]



plt.subplot(2, 2, 1)
plt.title("Pb")
plt.plot(H, 'r')
plt.grid()

plt.subplot(2, 2, 2)
plt.title("Pa")
plt.plot(Ha, 'r')
plt.grid()

plt.subplot(2, 2, 3)
plt.title("Rf")
plt.plot(Rf, 'r')
plt.grid()

plt.tight_layout()
plt.show()


with open("Coef_RF.dat", "w") as f:
    for s in Rf:
        f.write(str(s) +",\n")

