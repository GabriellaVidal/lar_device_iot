import time
from machine import Pin, ADC
import neopixel
class SensorColor:
    def __init__ (self, pinADC, pinDG):
    	self.red = 0
    	self.green = 0
    	self.blue = 0

    	self.sensorLDR = ADC(Pin(pinADC))
    	self.sensorLDR.atten(ADC.ATTN_11DB)
    	self.sensorNP = neopixel.NeoPixel(Pin(pinDG), 1)

    def changeColor(self, color):
    	if (color == 'G'):
    		self.sensorNP[0] = (0, 255, 0) #green
    	elif (color == 'R'): 
    		self.sensorNP[0] = (255, 0, 0) #red
    	elif (color == 'B'): 
    		self.sensorNP[0] = (0, 0, 255) #blue
    	self.sensorNP.write()

    def readSensor(self):
    	self.changeColor('R')
    	time.sleep_ms(100)
    	self.red = self.sensorLDR.read()
    	# print('red ', self.red)

    	self.changeColor('G')
    	time.sleep_ms(100)
    	self.green = self.sensorLDR.read()
    	# print('green ', self.green)

    	self.changeColor('B')
    	time.sleep_ms(100)
    	self.blue = self.sensorLDR.read()
    	# print('blue ', self.blue)

    	if (self.red > self.green and self.red > self.blue and self.red > 3000):
    		return "------------ VERMELHO ----------"
    		# print("------------ VERMELHO ----------")
    	elif (self.green > self.red and self.green > self.blue and self.green > 3400):
    		return "------------ VERDE ----------"
    	elif(self.blue > self.red):
    		return "------------ AZUL ----------"
    	elif(self.red > self.green and self.red > self.blue):
    		return "------------ PRETO ----------"
    	else:
    		return "------------ NDA ----------"
			