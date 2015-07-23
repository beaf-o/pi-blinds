from ABE_DeltaSigmaPi import DeltaSigma
from ABE_helpers import ABEHelpers
import math

class Voltage:
    channelRoomMappings = {"up": {"wz1": 1, "wz2": 3, "sz": 5}, "down": {"wz1": 2, "wz2": 4, "sz": 6}}

    def __init__(self, room, direction):
	self.room = room
	self.direction = direction
	self.channel = self.channelRoomMappings[direction][room]
        
	i2c_helper = ABEHelpers()
	bus = i2c_helper.get_smbus()
	self.adc = DeltaSigma(bus, 0x68, 0x69, 18)

    def readVoltage(self, channel):
	#return 2
	return self.adc.read_voltage(channel)

    def canSwitch(self):
	if self.room in ("wz", "all"):
	    return True	

	voltage = self.readVoltage(self.channel)
	print('Channel ' + str(self.channel) + " carries " + str(voltage) + " Volts")
	
	if math.fabs(voltage) > 0.1:
	    return False
	else:
	    return True
