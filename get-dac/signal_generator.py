import numpy as np
import time
 
def get_sin_wave_amplitude(freq, time_val):
    
    
    raw_sin = np.sin(2 * np.pi * freq * time_val)
    
    
    normalized_sin = (raw_sin + 1) / 2
    
    return normalized_sin
 
def wait_for_sampling_period(sampling_frequency):
    
    
    period = 1.0 / sampling_frequency
    
    
    time.sleep(period)