Crontabs 

$ crontab -e
>>

0 2 * * * /home/pi/iot/log/jtcloud.sh >> /home/pi/jcloud_upload.log 2>&1
0 2 * * * /home/pi/iot/log/f1.sh >> /home/pi/bioMetrics.log 2>&1

