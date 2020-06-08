import wave
import numpy as np
import scipy.signal as signal
f_min = 17000
framerate = 44100
t = np.arange(0,1,1.0/framerate)
n = 5
T = 1/n #秒为单位
# from 0 to 4
k = np.arange(5)
k = k.repeat(framerate/n)
t_prim = t - k*T 
B = 3000 #Hz 带宽
f_cos = np.cos(2*np.pi*f_min*t_prim+np.pi*B*(t_prim**2)/T)
# f_cos is the 实数域数值大小 or wave_data

wave_data = f_cos.astype(np.short)


wave_file = wave.open('/Users/dada/Downloads/fmcw.wav','wb')
wave_file.setnchannels(1)
wave_file.setsampwidth(2)
wave_file.setframerate(framerate)
print(type(wave_file))
wave_file.writeframes(wave_data.tostring())
wave_file.close()

