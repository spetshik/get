import time
import pwm_dac as pwm
 
def triangle(freq, t):
    period = 1.0 / freq
    x = (t % period) / period
    if x < 0.5:
        return 2.0 * x
    return 2.0 * (1.0 - x)
 
amplitude = 2.0
frequency = 10.0
sampling_frequency = 1000.0
 
dac = pwm.PWM_DAC(12, 1000, 3.3, True)
 
try:
    start = time.perf_counter()
    while True:
        t = time.perf_counter() - start
        voltage = triangle(frequency, t) * amplitude
        dac.set_voltage(voltage)
        time.sleep(1.0 / sampling_frequency)
finally:
    dac.deinit()