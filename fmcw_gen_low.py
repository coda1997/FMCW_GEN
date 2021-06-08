import wave
import numpy as np

coe = 2  # its a fixed value, no one should modified it if using saw-tooth FMCW wave
f_min = 17500
framerate = 48000
n = 10
T = 1 / n  # 秒为单位
t = np.arange(0, T / 2, 1.0 / framerate)
# from 0 to n
k = np.arange(1)
k = k.repeat(framerate / n)
# t_prim = t - k * T
t_prim = t
B = 1500 * coe  # 1500Hz 带宽

f_max = f_min + B / coe
f_cos = np.cos(2 * np.pi * f_min * t_prim + np.pi * B * (t_prim ** 2) / T) * 10000  # 10000提升响度
f_sin = np.cos(2 * np.pi * f_max * t_prim - np.pi * B * (t_prim ** 2) / T) * 10000
f_out = np.append(f_cos, f_sin)
# f_cos is the 实数域数值大小 or wave_data
# f_cos = wave_data = signal.chirp(t, f_min, 1, 1000, method='linear') * 10000
# chirp波

wave_data = f_out.astype(np.short)

wave_file = wave.open('test_sawtooth_fmcw.wav', 'wb')
wave_file.setnchannels(1)
wave_file.setsampwidth(2)
wave_file.setframerate(framerate)
print(type(wave_file))

for i in range(0, n * 10):
    wave_file.writeframes(wave_data.tobytes())

wave_file.close()
