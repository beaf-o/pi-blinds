#!/usr/bin/python

import wiringpi2
import sys, getopt
import os
import time
from voltage import Voltage

class Blinds():
    def __init__(self, room, direction):
	self.room = room
	self.direction = direction
	
    def switch(self):
	background = False
	if self.direction in ("up", "down"):
            canSwitch = voltage.canSwitch()
	    print('Can switch: ' + str(canSwitch))
	    if canSwitch == True:
		cmd = '/home/pi/blinds/blinds.sh '  + self.room + ' ' + self.direction
		if background == True:
		    cmd += ' &'
                os.system(cmd)
            else:
                print 'Manual switch (' + str(self.room) + ') is not set to neutral. Software switch not possible.'
                #sys.exit()
        else:
            print 'Direction: ' + self.direction + ' is not supported.'

def printUsage():
    print 'blinds.py -i,--id <id> -d,--direction <direction>'

if __name__ == "__main__":
    if len(sys.argv) < 3:
	print 'Too few arguments'
        printUsage()
        sys.exit()

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv,"hi:d:",["id=","direction="])
    except getopt.GetoptError:
        self.printUsage()
        sys.exit(2)

    room = ''
    direction = ''

    for opt, arg in opts:
        if opt == '-h':
            printUsage()
            sys.exit()
        elif opt in ("-i", "--id"):
            id = arg
        elif opt in ("-d", "--direction"):
            direction = arg

    print 'id: "' + id + '"'
    print 'Direction: "' + direction + '"'

    rooms = {"wz": ["wz1", "wz2"], "sz": ["sz"], "all": ["wz1", "wz2", "sz"]}
    if id in rooms.keys():
	for room in rooms[id]:
	    blinds = Blinds(room, direction)
	    voltage = Voltage(room, direction)
	    blinds.switch()
    else:
	blinds = Blinds(id, direction)
        voltage = Voltage(id, direction)
        blinds.switch()
