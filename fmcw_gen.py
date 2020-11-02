import wave
import numpy as np


def _fmcw_gen(frequency_min, bandwidth, period_in_seconds, framerate,time_in_seconds, out_put_path):
    t = np.arange(0, 1, 1.0 / framerate)
    # 秒为单位
    period_in_seconds = round(2*period_in_seconds)
    time_in_seconds = round(time_in_seconds/2)
    T = 1 / period_in_seconds  
    # from 0 to n
    k = np.arange(period_in_seconds)
    k = k.repeat(framerate / period_in_seconds)
    
    t_prim = t - k * T
    
    # 10000提升响度
    f_cos = np.cos(2 * np.pi * frequency_min * t_prim + np.pi * bandwidth * (t_prim ** 2) / T) * 10000  
    f_sin = np.sin(-2 * np.pi * (frequency_min+bandwidth) * t_prim + np.pi * bandwidth * (t_prim ** 2) / T) * 10000
    f_out = np.zeros(framerate*2)
    offset = round(framerate/period_in_seconds)
    for i in range(0, framerate, offset):
        f_out[2*i:2*i+offset] = f_cos[i:i+offset]
        f_out[2*i+offset:2*i+2*offset] = f_sin[i:i+offset]
    wave_data = f_out.astype(np.short)
    wave_file = wave.open(out_put_path, 'wb')
    wave_file.setnchannels(1)
    wave_file.setsampwidth(2)
    wave_file.setframerate(framerate)
    
    for i in range(0,time_in_seconds):
        wave_file.writeframes(wave_data.tobytes())


if __name__ == "__main__":
    fmcw_low_freq = 17500
    fmcw_high_freq = 20500
    bandwidth = 1500
    time = 1000 # 1000 seconds
    periods = 10
    framerate = 44100
    fmcw_low_path = 'output/fmcw_low.wav'
    fmcw_high_path = 'output/fmcw_high.wav'
    _fmcw_gen(fmcw_low_freq, bandwidth, periods, framerate, time, fmcw_low_path)
    _fmcw_gen(fmcw_high_freq, bandwidth, periods, framerate, time, fmcw_high_path)

