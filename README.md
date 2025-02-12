# LAB-2-PDS
# Análisis de Señales Fisiológicas  

## Introducción  
Este proyecto realiza el análisis de señales fisiológicas mediante técnicas de procesamiento digital de señales. Se incluyen cálculos estadísticos, transformadas de Fourier, correlaciones y análisis de la relación señal-ruido (SNR). Se utiliza Python con bibliotecas como `numpy`, `matplotlib` y `wfdb`.  

---

## Procesamiento de Señales  

### Convolución  
La convolución es una operación matemática que combina dos señales para producir una tercera. En este caso, se realiza la convolución de dos arreglos:  

```python
x = np.array([1,0,1,6,9,4,7,0,0,6])
h = np.array([5,6,0,0,7,6,8])
y = np.convolve(x, h)

```
#### Gráfica de la Convolución:

![image](https://github.com/user-attachments/assets/6c1f61bc-24e1-4b34-8737-ac16214c070a)

### Transformada de Fourier
Se aplica la Transformada de Fourier para analizar la señal en el dominio de la frecuencia:

```python
Y = fftpack.fft(señal)

```
#### Gráfica de la Transformada de Fourier:
![image](https://github.com/user-attachments/assets/9b9a56ee-a4a8-4ac2-81cb-ce6000562951)

### Espectro de la Señal
Se obtiene el espectro de la señal para visualizar la distribución de la energía en función de la frecuencia:

```python
plt.plot(frecuencias[:N//2], magnitud)

```
#### Gráfica del espectro:
![image](https://github.com/user-attachments/assets/ed32cd72-8830-467c-b03d-b5bc94d06a2e)


### Correlación
La correlación entre señales se calcula como:

```python
C = np.correlate(X1, X2, 'full')

```
#### Gráfica de la Correlación:
![image](https://github.com/user-attachments/assets/13a2d306-ed0b-40a8-857b-ed4bf6d42cc5)

## Resultados de los Cálculos Estadísticos
#### Media Programada:
0.00019983090837593647
### Media Predefinida:
0.0001998309083759337
#### Desviación estándar Programada:
0.08157616604538678
#### Desviación Predefinida:
0.08157616604538541
#### Coeficiente de variación:
408.2259681866606

## Análisis de SNR
#### SNR Gaussiano:
-0.053828336362555604 dB
#### SNR del Ruido de Impulso:
-10.637644470920284 dB
#### SNR del Ruido de Artefacto:
2.267634877200096 dB

### Interpretación de los Valores de SNR
##### Un SNR Gaussiano cercano a cero:
indica que la potencia del ruido es similar a la de la señal original, lo que sugiere una señal con ruido significativo.
##### El SNR del Ruido de Impulso es negativo: 
indica que el ruido tiene más potencia que la señal, afectando gravemente la calidad de la misma.
##### El SNR del Ruido de Artefacto es positivo: 
aunque relativamente bajo, lo que indica que la señal aún tiene un nivel aceptable de ruido, pero con posibilidad de mejora mediante filtrado.

## Tecnicas manuales
para lograr una mejor comprensión de la convolución y como se gráficaba, se llevo a cabo esta operación, junto a su gráfica, de manera manual, en este caso se utilizo el codigo y cédula de una de las compañeras del grupo

![image](https://github.com/user-attachments/assets/f35ae1d0-464e-4bab-b52a-0cee3b6dcf78)
![image](https://github.com/user-attachments/assets/1d900a23-d1f6-4c13-8015-e0a7e16d0fae)

## LICENCIAS Y RECOMENDACIONES 
Este código se encuentra bajo la Licencia MIT. Se permite su uso, modificación y distribución con la debida atribución al autor.

## Recomendaciones para su uso
Se recomienda utilizar Python 3.8 o superior.
Instalar las dependencias requeridas:

```python
pip install numpy matplotlib wfdb scipy

```
Asegurar que los archivos de señales fisiológicas estén disponibles en el directorio adecuado.

## Contacto 
Para consultas o contribuciones, contactar al autor a través de GitHub.
