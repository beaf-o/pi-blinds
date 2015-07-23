#!/bin/bash

if [ $# -lt 1 ]; then
    echo 'usage: ./daily_down.sh <room>'
    exit -1
fi

source /home/pi/blinds/config.sh

echo "Wait until it is later than ${LATEST_DOWN}:00"
while [ `TZ=":Europe/Berlin" date '+%H'` -lt ${LATEST_DOWN} ]; do
    sleep 300
done

delay=`shuf -i 1-${MAX_WAITING_TIME} -n 1`
echo "Wait ${delay} seconds."
sleep ${delay}
python /home/pi/blinds/blinds.py -i $1 -d down
