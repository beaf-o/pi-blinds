#!/usr/bin/python

import wiringpi2
#from ABE_ADCPi import ADCPi
#from ABE_helpers import ABEHelpers
import sys, getopt
import os
import time

#i2c_helper = ABEHelpers()
#bus = i2c_helper.get_smbus()
#adc = ADCPi(bus, 0x68, 0x69, 18)

#adc.read_voltage(1)
duration=10
void_interval=2
on=0
off=1

upPins = {"wz1":0, "wz2": 4, "sz": 15}
downPins = {"wz1": 1, "wz2": 14, "sz": 17}

script = 'python /home/pi/blinds/blinds.py'

#wiringpi2.wiringPiSetup()
#wiringpi2.wiringPiSetupSys()
#wiringpi2.wiringPiSetupGpio()

def printUsage():
  print 'blinds.py -r,--room <room> -d,--direction <direction>'

def checkArgLength():
  if len(sys.argv) < 3:
    print 'Too few arguments'
    printUsage()
    sys.exit()

# value in|out
def setPin(pinNumber, value):
  os.system('gpio export ' + str(pinNumber) + ' ' + str(value))

# value on|off
def writePin(pinNumber, value):
  os.system('gpio -g write ' + str(pinNumber) + ' ' + str(value))

def moveUp(room):
  pinUp = getUpPinByRoom(room)
  pinDown = getDownPinByRoom(room)
  
  #wiringpi2.pinMode(pinUp,1) # Set pin 6 to 1 ( OUTPUT )
  #wiringpi2.digitalWrite(pinUp,1) # Write 1 ( HIGH ) to pin 6
  #wiringpi2.digitalRead(6) # Read pin 6

  setPin(pinUp, 'out')
  setPin(pinDown, 'in')
  writePin(pinDown, off)
  time.sleep(1)

  print 'Enable relais via GPIO ' + str(pinUp) + ' for ' + str(duration) + ' seconds.'
  writePin(pinUp, on)

  time.sleep(duration)
  print 'Disable relais'
  os.system('gpio -g write ' + str(pinUp) + ' ' + str(off))
  time.sleep(1)

  print 'Tear down gpio pins'
  os.system('gpio export ' + str(pinUp) + ' in')

def moveDown(room):
  pinUp = getUpPinByRoom(room)
  pinDown = getDownPinByRoom(room)

  print('Set up gpio pins')
  setPin(pinUp, 'in')
  setPin(pinDown, 'out')
  writePin(pinUp, off)
  time.sleep(1)

  print('Enable relais via GPIO ' + str(pinDown) + ' for ' +  str(duration) + ' seconds.')
  writePin(pinDown, on)
  time.sleep(duration)
  print('Disable relais')
  writePin(pinDown, off)
  time.sleep(1)

  print('Tear down gpio pins')
  setPin(pinDown, 'in')

def getUpPinByRoom(room):
  return upPins[room]

def getDownPinByRoom(room):
  return downPins[room]

def main(argv):
  checkArgLength()

  room = ''
  direction = ''

  try:
    opts, args = getopt.getopt(argv,"hr:d:",["room=","direction="])
  except getopt.GetoptError:
    printUsage()
    sys.exit(2)
  
  for opt, arg in opts:
    if opt == '-h':
      printUsage()
      sys.exit()
    elif opt in ("-r", "--room"):
      room = arg
    elif opt in ("-d", "--direction"):
      direction = arg
   
  print 'Room: "' + room + '"'
  print 'Direction: "' + direction + '"'

  if room == "all":
    os.system(script + ' -r wz -d ' + direction)
    os.system(script + ' -r sz -d ' + direction)
    return

  if room == "wz":
    os.system(script + ' -r wz1 -d ' + direction)
    os.system(script + ' -r wz2 -d ' + direction)
    return

  if direction == "up":
    moveUp(room)
  elif direction == "down":
    moveDown(room)
  else:
    print 'Direction: ' + direction + ' is not supported.'

if __name__ == "__main__":
  main(sys.argv[1:])
