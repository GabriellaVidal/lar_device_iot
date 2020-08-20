from machine import Pin
from rodas import Rodas
carrinho = Rodas()
# from sensorColor import SensorColor
# sensorA = SensorColor(36, 14)
# sensorB = SensorColor(39, 12)
rodaEsquerda = Pin(13,Pin.IN) #d7
rodaDireita = Pin(14,Pin.IN) #d5
tempoGirar = 2
tempoFrente = tempoRe = 2
execucao = mensagemEmExecucao = False
alinhado = False
desalinhado = True

def recebeMensagem(topic, msg): # recebe mensagem chama movimento
  global desalinhado
  print((topic, msg.decode("utf-8")))

  msg_replace = msg.decode("utf-8").replace(']','').replace('[','')
  msg_array = msg_replace.replace('"','').split(",")
  print(msg_array)
  mensagemEmExecucao = True
  for x in msg_array:
    if topic == b'esp/rele1' and x == 'up':
      # print('ESP received, rele1 to on')
      if(desalinhado == False):
        movimentar('frente', tempoFrente)
      else:
        alinhar()
        movimentar('frente', tempoFrente)
      desalinhado = True

    if topic == b'esp/rele1' and x == 'down':
      # print('ESP received, rele1 to re')
      if(desalinhado == False):
        movimentar('re', tempoFrente)
      else:
        alinhar()
        movimentar('re', tempoFrente)
      desalinhado = True

    if topic == b'esp/rele1' and x == 'right':
      # print('ESP received, rele1 to direita')
      desalinhado = True
      movimentar('dir', tempoGirar)

    if topic == b'esp/rele1' and x == 'left':
      # print('ESP received, rele1 to direita')
      desalinhado = True
      movimentar('esq', tempoGirar)

    if topic == b'esp/rele1' and x == 'stop':
      # print('ESP received, rele1 to off')
      carrinho.parar();

def movimentar(comando, tempo): #movimento
  global desalinhado, execucao
  now=time.time()
  timer = 0
  print('entrou')
  while timer != tempo:
    end = time.time()
    timer = round(end-now)
    if(comando == 'frente'):
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
  carrinho.parar()
  execucao = False

def alinhar():
  global desalinhado, execucao,rodaEsquerda, rodaDireita
  
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
  # _thread.start_new_thread(alinhar, ())
  alinhar()
except OSError as e:
  restart_and_reconnect()
while True:
  try:
    client.check_msg()
    # if (time.time() - last_message) > message_interval:
    #   write on 'Hello' topic 
    #   msg = b'Oi #%d' % counter
    #   client.publish(topic_pub, msg)
    #   last_message = time.time()
    #   counter += 1
  except OSError as e:
    restart_and_reconnect()
