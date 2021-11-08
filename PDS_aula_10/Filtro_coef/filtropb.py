import numpy 
import matplotlib.pyplot as plt
from scipy import signal as sf

X = numpy.zeros(4999)
Y = numpy.zeros(4999)
H = numpy.zeros(100)

fc = 0.14
M = 100

for i in range(M):
    if(i - M/2) == 0:
        H[i] = 2 * numpy.pi * fc
    if(i - M/2) != 0:
        H[i] = numpy.sin(2 * numpy.pi * fc * (i - M/2)) / (i - M/2)
    H[i] = H[i] * (0.54 - 0.46 * numpy.cos(2 * numpy.pi * i / M))

SUM = 0

for i in range(M): 
    SUM += H[i]

for i in range(M):
    H[i] = H[i]/SUM



for j in range(100,4999):
    Y[j] = 0
    for i in range(M):
        Y[j] = Y[j] + X[j - i] * H[i]



print(H)

plt.subplot(2, 2, 1)
plt.title("X")
plt.plot(X, 'r')
plt.grid()

plt.subplot(2, 2, 2)
plt.title("Y")
plt.plot(Y, 'r')
plt.grid()

plt.subplot(2, 2, 3)
plt.title("H")
plt.plot(H, 'r')
plt.grid()

plt.tight_layout()
plt.show()


with open("PDS_aula_10/Filtro_coef/Coef_PB.dat", "w") as f:
    for s in H:
        f.write(str(s) +",\n")

H = []
with open("PDS_aula_10/Filtro_coef/Coef_PB.txt", "r") as f:
  for line in f:
    H.append(float(line.strip()))