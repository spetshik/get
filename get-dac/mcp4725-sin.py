import time
import signal_generator
import mcp4725_driver as mcp
 
dynamic_range = 5.0
frequency = 30.0
sampling_frequency = 500.0
 
def set_number_fixed(self, number):
    if not isinstance(number, int):
        return
    if not (0 <= number <= 4095):
        return
    cmd = 0x40
    high = (number >> 4) & 0xFF
    low = (number & 0x0F) << 4
    self.bus.write_i2c_block_data(self.address, cmd, [high, low])
 
mcp.MCP4725.set_number = set_number_fixed
 
try:
    dac = mcp.MCP4725(dynamic_range, address=0x61, verbose=False)
    start_time = time.time()
    while True:
        current_time = time.time() - start_time
        amplitude = signal_generator.get_sin_wave_amplitude(frequency, current_time)
        voltage = amplitude * dynamic_range
        dac.set_voltage(voltage)
        signal_generator.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()