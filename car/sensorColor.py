import time
from machine import Pin, ADC
import neopixel
class SensorColor:
    def __init__ (self):
    	self.red = 0
    	self.green = 0
    	self.blue = 0
    	self.ldrA = ADC(Pin(36))
    	self.ldrA.atten(ADC.ATTN_11DB)
    	self.npA = neopixel.NeoPixel(Pin(14), 1)

    def changeColor(self, color):
    	if (color == 'G'):
    		self.npA[0] = (0, 255, 0) #green
    	elif (color == 'R'): 
    		self.npA[0] = (255, 0, 0) #red
    	elif (color == 'B'): 
    		self.npA[0] = (0, 0, 255) #blue
    	self.npA.write()
    def readSensor(self):
    	self.changeColor('R')
    	time.sleep_ms(100)
    	self.red = self.ldrA.read()
    	print('red ', self.red)

    	self.changeColor('G')
    	time.sleep_ms(100)
    	self.green = self.ldrA.read()
    	print('green ', self.green)

    	self.changeColor('B')
    	time.sleep_ms(100)
    	self.blue = self.ldrA.read()
    	print('blue ', self.blue)

    	if (self.red > self.green and self.red > self.blue and self.red > 3000):
    		print("------------ VERMELHO ----------")
    	elif (self.green > self.red and self.green > self.blue and self.green > 3400):
    		print("------------ VERDE ----------")
    	elif(self.blue > self.red):
    		print("------------ AZUL ----------")
    	elif(self.red > self.green and self.red > self.blue):
    		print("------------ preto ----------")
    	else:
    		print("------------ NDA ----------")
			