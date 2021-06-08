import wave
import numpy as np


def _fmcw_gen(frequency_min, bandwidth, period_in_seconds, framerate, time_in_seconds, out_put_path):
    coe = 2
    T = 1 / period_in_seconds
    t = np.arange(0, T / 2, 1.0 / framerate)
    # 秒为单位
    t_prim = t
    bandwidth *= coe
    f_max = frequency_min + bandwidth / coe
    # 10000提升响度
    f_up = np.cos(2 * np.pi * frequency_min * t_prim + np.pi * bandwidth * (t_prim ** 2) / T) * 10000
    f_down = np.cos(2 * np.pi * f_max * t_prim - np.pi * bandwidth * (t_prim ** 2) / T) * 10000
    f_out = np.append(f_up, f_down)

    wave_data = f_out.astype(np.short)
    wave_file = wave.open(out_put_path, 'wb')
    wave_file.setnchannels(1)
    wave_file.setsampwidth(2)
    wave_file.setframerate(framerate)

    for i in range(0, time_in_seconds * period_in_seconds):
        wave_file.writeframes(wave_data.tobytes())


if __name__ == "__main__":
    fmcw_low_freq = 17500
    fmcw_high_freq = 20500
    bandwidth = 1500
    time = 1000  # 1000 seconds
    periods = 10
    framerate = 44100
    fmcw_low_path = 'output/fmcw_low.wav'
    fmcw_high_path = 'output/fmcw_high.wav'
    _fmcw_gen(fmcw_low_freq, bandwidth, periods, framerate, time, fmcw_low_path)
    _fmcw_gen(fmcw_high_freq, bandwidth, periods, framerate, time, fmcw_high_path)
