import wave
import numpy as np

f_min = 20000
framerate = 48000
t = np.arange(0, 1, 1.0 / framerate)
n = 5
T = 1 / n  # 秒为单位
# from 0 to n-1
k = np.arange(n)
k = k.repeat(framerate / n)
t_prim = t - k * T
B = 2000  # Hz 带宽
f_cos = np.cos(2 * np.pi * f_min * t_prim + np.pi * B * (t_prim ** 2) / T) * 10000  # 10000提升响度
# f_cos is the 实数域数值大小 or wave_data
# f_cos = wave_data = signal.chirp(t, f_min, 1, 1000, method='linear') * 10000
# chirp波

# f_min_right = 19500
# f_right = np.cos(2 * np.pi * f_min_right * t_prim + np.pi * B * (t_prim ** 2) / T) * 10000

wave_data = f_cos.astype(np.short)
# wave_data_right = f_right.astype(np.short)

wave_file = wave.open('output/test2.wav', 'wb')
wave_file.setnchannels(1)
wave_file.setsampwidth(2)
wave_file.setframerate(framerate)
print(type(wave_file))

empty_data = np.zeros(shape=(10), dtype='short')
wave_file.writeframes(empty_data.tobytes())

for i in range(0,1):
    wave_file.writeframes(wave_data.tobytes())


# for l, r in zip(wave_data, wave_data_right):
#     wave_file.writeframes(l.tobytes())
#     wave_file.writeframes(r.tobytes())

wave_file.close()
