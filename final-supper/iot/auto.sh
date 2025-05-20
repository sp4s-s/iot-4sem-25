#!/bin/bash

# Run file1.py in background
python3 ~/iot/src/f1.py &
PID1=$!
sleep 10
kill $PID1

# Run file2.py in background
python3 ~/iot/src/dht1.py &
PID2=$!
sleep 5
kill $PID2

# Run file3.sh
bash ~/iot/src/sent.sh

