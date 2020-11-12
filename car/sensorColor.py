import time
from machine import Pin, ADC
import neopixel

class SensorColor:
    def __init__ (self, pinADC, pinDG):
    	self.red = 0
    	self.green = 0
    	self.blue = 0

    	# self.sensorLDR = ADC(Pin(pinADC))
        self.sensorLDR = ADC(pinADC)
    	# self.sensorLDR.atten(ADC.ATTN_11DB)
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
    	time.sleep_ms(5)
    	self.red = self.sensorLDR.read()
    	# print('red -------------', self.red)

    	self.changeColor('G')
    	time.sleep_ms(5)
    	self.green = self.sensorLDR.read()
    	# print('green ----------------------', self.green)

    	self.changeColor('B')
    	time.sleep_ms(5)
    	self.blue = self.sensorLDR.read()
    	# print('blue ----------------------------', self.blue)

    	if (self.red > self.green and self.red > self.blue):
    		return b"VERMELHO"
    		# print("------------ VERMELHO ----------")
        elif (self.green > self.red and self.green > self.blue
            and self.red>900 and self.green>900  and self.blue>800):
            return b"BRANCO"
    	elif (self.green > self.red and self.green > self.blue):
    		return b"VERDE"
    		# return "------------ VERDE ----------"
    	elif(self.blue > self.red and self.blue > self.green):
    		return b"AZUL"
    		# return "------------ AZUL ----------"
    	elif(self.red < self.green and self.green > self.blue):
    		return b"PRETO"
    		# return "------------ PRETO ----------"
    	else:
    		return b"NDA"
    		# return "------------ NDA ----------"
			