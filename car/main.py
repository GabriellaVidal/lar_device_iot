# Complete project details at https://RandomNerdTutorials.com
import mov
import time

def movimentar(topic, msg):
  print((topic, msg.decode("utf-8")))

  msg_replace = msg.decode("utf-8").replace(']','').replace('[','')
  msg_array = msg_replace.replace('"','').split(",")
  print(msg_array)

  for x in msg_array:

    if topic == b'esp/rele1' and x == 'up':
      print('ESP received, rele1 to on')
      temporizador('frente')

    if topic == b'esp/rele1' and x == 'down':
      print('ESP received, rele1 to re')
      temporizador('re')

    if topic == b'esp/rele1' and x == 'right':
      print('ESP received, rele1 to direita')
      temporizador('dir')

    if topic == b'esp/rele1' and x == 'left':
      print('ESP received, rele1 to direita')
      temporizador('esq')

    if topic == b'esp/rele1' and x == 'stop':
      print('ESP received, rele1 to off')
      mov.parar();

def temporizador(comando):
  now=time.time()
  timer = 0
  while timer != 10:
    end = time.time()
    timer = round(end-now)
    print(timer)
    print(comando)
    if(comando == 'frente'):
      mov.frente()
    if(comando == 're'):
      mov.re()
    if(comando == 'dir'):
      mov.dir()
    if(comando == 'esq'):
      mov.esq()
  mov.parar()

def connect():
  print('connect')
  global client_id, mqtt_server, topic_sub, server_port, mqtt_user, mqtt_password
  client = MQTTClient(client_id, mqtt_server, server_port, mqtt_user, mqtt_password)
  client.connect()
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect()
  client.set_callback(movimentar)
  client.subscribe(topic_sub)
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      # write on 'Hello' topic 
      msg = b'Oi #%d' % counter
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()
