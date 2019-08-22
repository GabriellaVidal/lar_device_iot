# Complete project details at https://RandomNerdTutorials.com
import mov

def movimentar(topic, msg):
  print((topic, msg))
  if topic == b'esp/rele1' and msg == b'andar':
    print('ESP received, rele1 to on')
    mov.frente();

  if topic == b'esp/rele1' and msg == b're':
    print('ESP received, rele1 to re')
    mov.re();

  if topic == b'esp/rele1' and msg == b'andarDireita':
    print('ESP received, rele1 to direita')
    mov.dir();

  if topic == b'esp/rele1' and msg == b'andarEsquerda':
    print('ESP received, rele1 to direita')
    mov.esq();

  if topic == b'esp/rele1' and msg == b'parar':
    print('ESP received, rele1 to off')
    mov.parar();

  time.sleep(1);

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
    print(client.check_msg())
    if (time.time() - last_message) > message_interval:
      # write on 'Hello' topic 
      msg = b'Oi #%d' % counter
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()
