Run new.py File
runs for 2 secs

for 10 times
bash 

for i in {1..10}; do
  python new.py
done

Repeat for n times

Other files
 - en.py for just 1 run ( 2 sec )
 - pump.py for until keyboard interrupt
 - new.py  run for 1 run ( 2 sec ) with timer  



⚡ Relay Module Pinout (Standard)

| Relay Pin        | Connect To               |
|------------------|--------------------------|
| IN               | GPIO pin on Pi (e.g., GPIO 17) |
| GND              | Pi GND                   |
| VCC              | Pi 5V                    |

---

⚡ Relay Output (Screw Terminal)

| Relay Terminal   | Connect To               |
|------------------|--------------------------|
| COM (Common)     | Battery +                |
| NO (Normally Open)| Motor + lead             |
| NC (Normally Closed)| (Leave unconnected)      |

---

**Note:** Motor GND goes directly to Battery GND.