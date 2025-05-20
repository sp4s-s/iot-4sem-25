#!/bin/bash

# Run first.py and read its output line by line
python irm.py | while read -r line; do
    if [ "$line" = "0" ]; then
        echo "Detected 0 → Running second.py..."
        python new.py
	pkill -f irm.py
        break
    fi
done
