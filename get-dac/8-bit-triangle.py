import time
import r2r_dac as r2r
 
def triangle(freq, t):
    period = 1.0 / freq
    x = (t % period) / period
    if x < 0.5:
        return 2.0 * x
    return 2.0 * (1.0 - x)
 
amplitude = 2.0
frequency = 10.0
sampling_frequency = 1000.0
 
dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, False)
 
try:
    start = time.perf_counter()
    while True:
        t = time.perf_counter() - start
        voltage = triangle(frequency, t) * amplitude
        dac.set_voltage(voltage)
        time.sleep(1.0 / sampling_frequency)
finally:
    dac.deinit()
