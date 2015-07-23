from ABE_DeltaSigmaPi import DeltaSigma
from ABE_helpers import ABEHelpers
    
i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = DeltaSigma(bus, 0x68, 0x69, 18)

while True:
  voltage = adc.read_voltage(1)
  v = voltage * 1000
  print('')
  #print('Channel 1: ' + str(v) + " Volts")
  print('Channel 1: ' + str(1000 * adc.read_voltage(1)) + " V")
  print('Channel 2: ' + str(1000 *adc.read_voltage(2)) + " V")
  print('Channel 3: ' + str(1000 * adc.read_voltage(3)) + " V")
  print('Channel 4: ' + str(1000 * adc.read_voltage(4)) + " V")
  print('Channel 5: ' + str(1000 * adc.read_voltage(5)) + " V")
  print('Channel 6: ' + str(1000 * adc.read_voltage(6)) + " V")
  print('Channel 7: ' + str(1000 * adc.read_voltage(7)) + " V")
  print('Channel 8: ' + str(1000 * adc.read_voltage(8)) + " V")
