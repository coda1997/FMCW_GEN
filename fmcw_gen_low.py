import wave
import numpy as np

f_min = 17500
framerate = 48000
t = np.arange(0, 1, 1.0 / framerate)
n = 30
T = 1 / n  # 秒为单位
# from 0 to n
k = np.arange(n)
k = k.repeat(framerate / n)
t_prim = t - k * T
B = 1500  # Hz 带宽
f_cos = np.cos(2 * np.pi * f_min * t_prim + np.pi * B * (t_prim ** 2) / T) * 10000  # 10000提升响度
# f_cos is the 实数域数值大小 or wave_data
# f_cos = wave_data = signal.chirp(t, f_min, 1, 1000, method='linear') * 10000
# chirp波

wave_data = f_cos.astype(np.short)

wave_file = wave.open('output/fmcw_low.wav', 'wb')
wave_file.setnchannels(1)
wave_file.setsampwidth(2)
wave_file.setframerate(framerate)
print(type(wave_file))

for i in range(0,10):
    wave_file.writeframes(wave_data.tobytes())



wave_file.close()
