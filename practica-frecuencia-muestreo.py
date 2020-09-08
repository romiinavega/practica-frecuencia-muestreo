import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave

import matplotlib.pyplot as plt 

sonido = SinSignal(freq=440, amp=1, offset=0)
wave_sonido = sonido.make_wave(duration=1, start=0, framerate=44100)

decorate(xlabel="Amplitud")
decorate(xlabel="Tiempo (s)")

#wave_sonido.plot()
#plt.show()

wave_sonido.write("sonido_original.wav")

print(type(wave_sonido))
print("Inicio: " + str(wave_sonido.start))
print("Duracion: " + str(wave_sonido.duration))
print("Frecuencia de muestreo: " + str (wave_sonido.framerate))

wave_sonido.framerate = wave_sonido.framerate / 2

wave_sonido.write("sonido_modificado.wav")

print("Frecuencia de muestreo modificada: " + str (wave_sonido.framerate))

decorate(xlabel="Tiempo (s)")
decorate(xlabel="Amplitud")
#wave_sonido.plot()
#plt.show()

campana = read_wave("dsp-recursos/18871__zippi1__sound-bell-440hz.wav")
segmento_campana = campana.segment(8,1)
decorate(xlabel="Tiempo (s)")
decorate(xlabel="Amplitud")
segmento_campana.plot()
plt.show()

segmento_campana.write("campana_original.wav")

segmento_campana.framerate = segmento_campana.framerate / 2

segmento_campana.write("campana_modificada.wav")