# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:12:59 2025

@author: User
"""

#LABORATORIO 

import numpy as np #Operaciones matematicas 
import matplotlib.pyplot as plt #Graficas y dibujos
import wfdb  #Para carga de señales fisiológicas y manipularlos 
from scipy import fftpack
#A

x = np.array ([1,0,1,6,9,4,7,0,0,6])
h = np.array ([5,6,0,0,7,6,8])

y = np.convolve(x,h)
n = np.arange(len(y))
print("CONVOLUCION: ", y)

plt.stem(n,y)
plt.xlabel("y[n]")
plt.ylabel("n")
plt.title("convolución y[n]")
plt.show()

# B

Ts = 1.25e-3 #tiempo de muestreo 
n = np.arange (9) # rango de n 0 ≤ 𝑛 < 9, 0 ≤ 𝑛 < 9
T = n*Ts # valores de tiempo

X1 = np.cos(2*np.pi*100*n*Ts)  #𝑥1[𝑛𝑇𝑠] = cos(2𝜋100𝑛𝑇𝑠)
X2 = np.sin(2*np.pi*100*n*Ts)  #𝑥2[𝑛𝑇𝑠] = sin(2𝜋100𝑛𝑇𝑠) 

C = np.correlate(X1, X2, 'full') #De manera predeterminada, el modo es "completo". Esto devuelve la convolución en cada punto de superposición
print("Correlación: ", C)


plt.plot(C)
#plt.xlabel('Retraso')
#plt.ylabel('Correlación')
plt.title('Correlación')
plt.show()


plt.plot(T, X1, label='X1[nTs]')
plt.plot(T, X2, label='X2[nTs]')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Representacion Grafica y Secuencial')
plt.legend()
plt.style.context('dark_background')
plt.show()


#C


señal, datos = wfdb.rdsamp('emg_healthy') #Leemos informacion
record = wfdb.rdrecord('emg_healthy') #Nos da informacion sobre la señal

n = datos['sig_len']#llamar longitud de verctor datos, cuantos puntos tiene la señal
c = señal[:] #canal que vamos a usar 2
fr = datos ['fs'] #Frecuencia

tm=1/fr #tiempo de muestreo
s=señal.flatten() #para que la señal este unidimencional, para que no salga en forma de matrix
t = np.linspace(0, 1, fr, endpoint=False) #Crea una lista de tiempos para cada punto de la señal

media = np.mean(señal)
mediap = sum(s)/np.size(s)
print("Media Programada: ",mediap)
print("Media Predefinida: ",media)
d_e = np.std(señal) #desviacion estandar
d_ep= np.sqrt(sum((x - mediap) ** 2 for x in s) / len(s))
print("Desviación estándar Programada:", d_ep)
print("Desviación Predefinida:",d_e)
cv = d_e/media
print("Coeficiente de variación:", cv)

N = len(t) #longitud de la lista. Numero de muestras 
F = np.fft.fft(señal)
NN = len(s)

frecuencias = np.fft.fftfreq(N, 1/fr)
espectro = np.fft.fft(señal)/N
magnitud = 2 * np.abs(espectro)[:N//2]
m = np.abs(F)


plt.plot(frecuencias[:N//2], magnitud)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de la señal')
plt.show()


Y = fftpack.fft(señal)
f = fftpack.fftfreq(NN)*fr
plt.plot(f, np.abs(Y))
plt.title('Transformada de Fourier')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.show()


plt.plot(señal)
plt.title('Señal en el tiempo')
plt.xlabel('Tiempo [s]')
plt.ylabel('Magnitud')
plt.show()

#senal ruido gaussiano
ruido = np.random.normal(0, d_e, señal.shape)
señal_ruidosa = señal + ruido
# Convertir a una dimensión
señal_ruidosa = señal_ruidosa.flatten()
t = np.arange(señal_ruidosa.shape[0]) * tm 

plt.plot(t, señal_ruidosa) 

plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [mV]")
plt.title("Señal con Ruido Gaussiano")
plt.show()

#calcular SNR GAUSSIANO 
Pseñal = np.mean(señal**2)
Pruido = np.mean(ruido**2)
SNR = 10 * np.log10(Pseñal / Pruido)

print("SNR gaussiano:", SNR, "dB")

#senal ruido impulso
probabilidad_ruido = 0.1  # Ajusta este valor según la cantidad de ruido que desees
mascara_ruido = np.random.rand(*señal.shape) < probabilidad_ruido
señal_ruidosai = señal.copy()  # Crea una copia para no modificar la señal original
señal_ruidosai[mascara_ruido] = np.random.choice([np.min(señal), np.max(señal)], size=mascara_ruido.sum())
señal_ruidosai = señal_ruidosai.flatten()
t = np.arange(señal_ruidosai.shape[0]) * tm 
plt.plot(t, señal_ruidosai)
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [mV]")
plt.title("Señal con Ruido de Impulso")
plt.show()

# --- CALCULAR SNR IMPULSO ---
# Aplanar señal y mascara_ruido
señal_plana = señal.flatten()
mascara_ruido_plana = mascara_ruido.flatten()

  # 1. Estima la señal "limpia" restando el ruido de la señal ruidosa
señal_estimada_limpia = señal_ruidosai - (señal_ruidosai - señal_plana) * mascara_ruido_plana 
  # 2. Calcula la potencia de la señal original
Pseñal = np.mean(señal**2)
  # 3. Calcula la potencia del ruido de impulso
Pruido_impulso = np.mean((señal_ruidosai - señal_estimada_limpia)**2)
  # 4. Calcula la SNR
SNR_impulso = 10 * np.log10(Pseñal / Pruido_impulso)

print("SNR del ruido de impulso:", SNR_impulso, "dB")

#senal ruido artefacto 
duracion_artefacto = int(0.1 * fr)  # Duración en muestras (0.1 segundos en este ejemplo)
amplitud_artefacto = 2 * np.max(señal)  # Amplitud del artefacto
artefacto = amplitud_artefacto * np.exp(-np.arange(duracion_artefacto) / (duracion_artefacto / 5))  # Decaimiento exponencial, ruido pico repentino
posicion_artefacto = int(0.5 * len(señal))  # Posición del artefacto en la señal
señal_ruidosaa = señal.copy()
# Expandir las dimensiones de 'artefacto' para que coincidan con la sección de 'señal_ruidosaa'
artefacto_expandido = np.broadcast_to(artefacto[:, np.newaxis], (duracion_artefacto, señal.shape[1]))  
señal_ruidosaa[posicion_artefacto:posicion_artefacto + duracion_artefacto] += artefacto_expandido  
señal_ruidosaa = señal_ruidosaa.flatten()
t = np.arange(señal_ruidosaa.shape[0]) * tm 

plt.plot(t, señal_ruidosaa)
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [mV]")
plt.title("Señal con Artefacto")
plt.show()
# --- CALCULAR SNR ARTEFACTO ---
# 1. Estima la señal "limpia" restando el artefacto
señal_estimada_limpia = señal_ruidosaa.copy()
señal_estimada_limpia[posicion_artefacto:posicion_artefacto + duracion_artefacto] -= artefacto 
# 2. Calcula la potencia de la señal original
Pseñal = np.mean(señal**2)
# 3. Calcula la potencia del ruido de artefacto
Pruido_artefacto = np.mean((señal_ruidosaa - señal_estimada_limpia)**2)
# 4. Calcula la SNR
SNR_artefacto = 10 * np.log10(Pseñal / Pruido_artefacto)

print("SNR del ruido de artefacto:", SNR_artefacto, "dB")



