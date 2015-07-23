#!/bin/bash

if [ $# -lt 1 ]; then
    echo 'usage: ./daily_up.sh <room>'
    exit -1
fi

source /home/pi/blinds/config.sh

echo "Wait until it is later than ${EARLIEST_UP}:00"
while [ `TZ=":Europe/Berlin" date '+%H'` -lt ${EARLIEST_UP} ]; do
   sleep 300
done

delay=`shuf -i 1-${MAX_WAITING_TIME} -n 1`
echo "Wait ${delay} seconds."
sleep ${delay}

python /home/pi/blinds/blinds.py -i $1 -d up
