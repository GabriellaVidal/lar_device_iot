# Complete project details at https://RandomNerdTutorials.com

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect() 

# ssid = 'LAR'
# password = 'LAR@1480'
# mqtt_server = '10.6.4.138'
ssid = 'brisa-1172954'
password = 'umezhftn'
mqtt_server = '192.168.1.4'
server_port=1883
mqtt_user=''
mqtt_password=''

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub_led = b'esp/led'
# topic_pub_led = b'esp/vivo'
# topic_sub = b'esp/rele1'
# topic_pub = b'esp/vivo'
topic_sub = b'ureto/sub'
topic_pub = b'ureto/pub'

last_message = 0
message_interval = 30
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())