import numpy 
import matplotlib.pyplot as plt
from scipy import signal as sf
import math


def geraRF():
    Xb = numpy.zeros(4999)
    Yb = numpy.zeros(4999)

    Fs = int(input("Fs: "))
    fcb = int(input("fcb: "))
    fcb = float(fcb/Fs)
    Bw = int(input("Bw: "))
    M = int(4/(Bw/Fs))
    Hb = numpy.zeros(M)
    atenuacao = float(input("Atenuacao (1.0 = total, 0.0 = nao faz efeito): "))

    for i in range(len(Hb)):
        if(i - M/2) == 0:
            Hb[i] = 2 * numpy.pi * fcb
        if(i - M/2) != 0:
            Hb[i] = numpy.sin(2 * numpy.pi * fcb * (i - M/2)) / (i - M/2)
        Hb[i] = Hb[i] * (0.54 - 0.46 * numpy.cos(2 * numpy.pi * i / M))

    SUMb = 0

    for i in range(len(Hb)): 
        SUMb += Hb[i]

    for i in range(len(Hb)):
        Hb[i] = Hb[i]/SUMb

    for j in range(100,4999):
        Yb[j] = 0
        for i in range(len(Hb)):
            Yb[j] = Yb[j] + Xb[j - i] * Hb[i]


    ############################################################ PASSA ALTA

    X = numpy.zeros(4999)
    Y = numpy.zeros(4999)

    fc = int(input("Fc: "))
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

    for k in range(M):
        H[k] = H[k] * -1
        if( k == M/2):
            H[k] = 1 - H[k]


    ## calculo RF
    for l in range(len(H)):
        newH =  (round(float(H[l]),4) + round(float(Hb[l]),4)) * atenuacao
        #print( str(H[l])  + " + " + str(Hb[l]) + " = " + str(newH))  
        H[l] = newH

    return(H)


one = geraRF()
second = geraRF()


realSaida = []
for i in range(len(one)-1):
    realSaida.append( float(one[i]) + float(second[i]) )

#diplayer = realSaida
#[w, diplayer] = sf.freqz(diplayer, 1, 8000)
#plt.plot(w*8000/(2*numpy.pi), 20*numpy.log10(abs(diplayer)))
#plt.show()

with open("Coef_RF.dat", "w") as f:
    for i in range(len(realSaida)):
        f.write(str(realSaida[i]) +",\n")

