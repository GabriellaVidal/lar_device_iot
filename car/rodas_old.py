from machine import Pin, PWM
class Rodas:
    def __init__ (self):
        ## Frequencia de trabalho do motor
        # O valor maximo e 1023 
        ## Os pinos para o Shield ESP 8266 fixos 
        # Para o motor A, esquerdo, os pinos sao:
        # 5 para velocidade e 0 para dire莽茫o 
        # self.PwmA = PWM(Pin(5), freq=1000 ,duty = 0)
        # self.DirA = Pin(0, Pin.OUT) 
        # Para o motor B, direito, os pinos sao:
        # 4 para velocidade e 2 para dire鑾絘o
        # self.PwmB = PWM(Pin(4), freq=1000 ,duty = 0)
        # self.DirB = Pin(2, Pin.OUT)
        # self.freqA = 1000
        # self.dutyA = 0
        # self.freqB = 1000 
        # self.dutyB = 0 

         ## Os pinos para o Shield ESP 8266 fixos 
        # Para o motor A, esquerdo, os pinos sao:
        # 5 para velocidade e 0 para dire莽茫o 
        # self.PwmA = PWM(Pin(5), freq=1000 ,duty = 0)
        # self.DirA = Pin(0, Pin.OUT) 
        # Para o motor B, direito, os pinos sao:
        # 4 para velocidade e 2 para dire鑾絘o
        # self.PwmB = PWM(Pin(4), freq=1000 ,duty = 0)
        # self.DirB = Pin(2, Pin.OUT)
        self.freqA = 1000
        self.dutyA = 300
        self.freqB = 1000 
        self.dutyB = 300 
        self.dutyB = 300 
        self.dutyOff = 700 #(misterio)
        self.PwmA = PWM(Pin(18), freq= self.freqA ,duty = 0)
        self.DirA = Pin(19, Pin.OUT)   
        self.PwmB = PWM(Pin(23), freq= self.freqB ,duty = 0)
        self.DirB = Pin(5, Pin.OUT)
     
    
    def frente(self):
        # print("frente") 
        self.PwmA.duty(self.dutyA) 
        self.PwmB.duty(self.dutyB)
        self.DirA.on() 
        self.DirB.on() 
        
    def re(self):
        # print("re") 
        self.PwmA.duty(self.dutyOff)
        self.PwmB.duty(self.dutyOff) 
        self.DirA.off() 
        self.DirB.off() 
     
    def esquerda(self):
        # print("esquerda") 
        self.PwmA.duty(self.dutyA)
        self.PwmB.duty(self.dutyOff) 
        self.DirA.on() 
        self.DirB.off() 
        
    def direita(self):
        # print("direita") 
        self.PwmA.duty(self.dutyOff)
        self.PwmB.duty(self.dutyB) 
        self.DirA.off() 
        self.DirB.on()  
        
    def parar(self):
        # print("parar") 
        self.PwmA.duty(0)
        self.PwmB.duty(0) 
        self.DirA.off() 
        self.DirB.off() 