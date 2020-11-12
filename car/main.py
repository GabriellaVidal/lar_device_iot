from utime import ticks_ms, sleep_ms
from machine import Pin

from rodas import Rodas
carrinho = Rodas()
rodaEsquerda = Pin(13,Pin.IN) #d7
rodaDireita = Pin(14,Pin.IN) #d5

from sensorColor import SensorColor
sensor = SensorColor(0, 12)

tempoGirar = 1100
tempoFrente = tempoRe = 1100
execucao = mensagemEmExecucao = False
alinhado = False
desalinhado = True
led = Pin(2, Pin.OUT)

def recebeMensagem(topic, msg): # recebe mensagem chama movimento
  global desalinhado, topic_sub, topic_pub
  print((topic, msg.decode("utf-8")))

  msg_replace = msg.decode("utf-8").replace(']','').replace('[','')
  msg_array = msg_replace.replace('"','').split(",")
  print(msg_array)
  print(topic_sub)
  print(client)
  
  mensagemEmExecucao = True
  for x in msg_array:
    if topic == topic_sub and x == 'up':
      # print('ESP received, rele1 to on')
      if(desalinhado == False):
        movimentar('frente', tempoFrente)
      else:
        alinhar()
        movimentar('frente', tempoFrente)
      desalinhado = True
      client.publish(topic_pub, b"feito")

    if topic == topic_sub and x == 'down':
      # print('ESP received, rele1 to re')
      if(desalinhado == False):
        movimentar('re', tempoFrente)
      else:
        alinhar()
        movimentar('re', tempoFrente)
      desalinhado = True
      client.publish(topic_pub, b"feito")

    if topic == topic_sub and x == 'right':
      # print('ESP received, rele1 to direita')
      desalinhado = True
      movimentar('dir', tempoGirar)
      client.publish(topic_pub, b"feito")

    if topic == topic_sub and x == 'left':
      # print('ESP received, rele1 to direita')
      desalinhado = True
      movimentar('esq', tempoGirar)
      client.publish(topic_pub, b"feito")

    if topic == topic_sub and x == 'stop':
      # print('ESP received, rele1 to off')
      carrinho.parar();
      client.publish(topic_pub, b"feito")

    if topic == topic_sub and x == 'finalizado':
      cor = sensor.readSensor()
      client.publish(topic_pub, cor)
      # client.publish(topic_pub, b"feito")
      blink();
  # client.publish(topic_pub, b"feito")

def blink():
  for i in range(3):
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)

def movimentar(comando, tempo): #movimento
  global desalinhado, execucao, rodaEsquerda, rodaDireita
  # now=time.time()
  now=ticks_ms()
  timer = tempo
  print('entrou')
  while timer <= tempo:
    # end = time.time()
    end = ticks_ms()
    timer = end-now
    print('tempo----------', tempo)
    print('timer----------', timer)
    print('end----------', end)
    print('now----------', now)
    # print('linha preta----------', rodaEsquerda.value() == 1 and rodaDireita.value() == 1)
    # print('executando----------', execucao)
    if(comando == 'frente'):
      # if execucao == True and rodaEsquerda.value() == 1 and rodaDireita.value() == 1:
        # break
      # else:
      print('frente')
      carrinho.frente()
    if(comando == 're'):
      print('re')
      carrinho.re()
    if(comando == 'dir'):
      print('dir')
      carrinho.direita()
    if(comando == 'esq'):
      print('esq')
      carrinho.esquerda()
    execucao = True
  print('saiu')
  carrinho.parar()
  execucao = False

def alinhar():
  global desalinhado, rodaEsquerda, rodaDireita
  
  while desalinhado == True:
    # print('rodaEsquerda', rodaEsquerda.value())
    # print('rodaDireita', rodaDireita.value())
    # time.sleep(4)
    while rodaEsquerda.value() == rodaDireita.value() and desalinhado == True:
      if rodaEsquerda.value() == 0 and rodaDireita.value() == 0:
        carrinho.frente()
      if rodaEsquerda.value() == 1 and rodaDireita.value() == 1:
        carrinho.parar()
        desalinhado = False
        time.sleep(2)
    while rodaEsquerda.value() != rodaDireita.value() and desalinhado == True:
      if rodaEsquerda.value() == 1 and rodaDireita.value() == 0:
        carrinho.esquerda()
      if rodaEsquerda.value() == 0 and rodaDireita.value() == 1:
        # carrinho.parar()
        carrinho.direita()

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
  client.set_callback(recebeMensagem)
  client.subscribe(topic_sub)
  alinhar()
  # cor = sensor.readSensor()
  # print('cor-----------------', cor)
except OSError as e:
  restart_and_reconnect()
while True:
  # cor = sensor.readSensor()
  # print(cor)
  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()
