#!/bin/bash

if [ $# -lt 2 ]; then
        echo 'usage: ./blinds.sh <room> <direction>'
        exit -1
fi

. /home/pi/blinds/config.sh

room=$1
direction=$2

on=1
off=0

echo ""
echo "room: $room"
echo "direction: $direction"
echo ""

main() {
	if [ "$room" == "all" ]; then
                if  [ "$direction" == "up" ]; then
                	/home/pi/blinds/blinds.sh wz1 up &
			sleep $voidInterval
			/home/pi/blinds/blinds.sh wz2 up &
                        sleep $voidInterval
			/home/pi/blinds/blinds.sh sz up &
			sleep $voidInterval
                else
                	/home/pi/blinds/blinds.sh wz1 down &
			sleep $voidInterval
			/home/pi/blinds/blinds.sh wz2 down &
                        sleep $voidInterval
			/home/pi/blinds/blinds.sh sz down &
			sleep $voidInterval
                fi

		wait

		exit 0
        fi

	if [ "$room" == "wz" ]; then
                if  [ "$direction" == "up" ]; then
                        /home/pi/blinds/blinds.sh wz1 up &
			sleep $voidInterval
			/home/pi/blinds/blinds.sh wz2 up &
			sleep $voidInterval
                else
			/home/pi/blinds/blinds.sh wz1 down &
			sleep $voidInterval
			/home/pi/blinds/blinds.sh wz2 down &
			sleep $voidInterval
                fi

		wait

		exit 0
        fi

	pinUp=
	pinDown=

	if [ "$room" == "wz1" ]; then
		pinUp=$wz1_pinUp
		pinDown=$wz1_pinDown
	fi

	if [ "$room" == "wz2" ]; then
                pinUp=$wz2_pinUp
                pinDown=$wz2_pinDown
        fi

	if [ "$room" == "sz" ]; then
                pinUp=$sz_pinUp
                pinDown=$sz_pinDown
        fi

	if [ "$direction" == "up" ]; then
		moveUp
	else
		moveDown
	fi
}

moveUp() {
	echo "Set up gpio pins"
	gpio export $pinUp out
	gpio export $pinDown in
	gpio -g write $pinDown $off
	sleep 1

	echo "Enable relais via GPIO $pinUp for $duration seconds."
	gpio -g write $pinUp $on
	sleep $duration
	echo "Disable relais"
	gpio -g write $pinUp $off
	sleep 1

	echo "Tear down gpio pins"
	gpio export $pinUp in
}

moveDown() {
	echo "Set up gpio pins"
        gpio export $pinUp in
        gpio export $pinDown out
        gpio -g write $pinUp $off
        sleep 1

        echo "Enable relais via GPIO $pinDown for $duration seconds."
        gpio -g write $pinDown $on
        sleep $duration
        echo "Disable relais"
        gpio -g write $pinDown $off
        sleep 1

        echo "Tear down gpio pins"
        gpio export $pinDown in
}

main $?
