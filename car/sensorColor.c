#include <Adafruit_NeoPixel.h>
#ifdef _AVR_
#include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif
#define PIN        A1
#define NUMPIXELS 1
#define COLOR_DELAY 5

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);


void setup() {
#if defined(_AVR_ATtiny85_) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif
  pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
  Serial.begin(115200);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
}

void changeColor(char color) {
  pixels.clear();
  for (int i = 0; i < NUMPIXELS; i++) {
    if (color == 'G') pixels.setPixelColor(i, pixels.Color(0, 255, 0));
    else if (color == 'R') pixels.setPixelColor(i, pixels.Color(255, 0, 0));
    else if (color == 'B') pixels.setPixelColor(i, pixels.Color(0, 0, 255));
  }
  pixels.show();
}

int red, green, blue;
void readSensor(){
  
  changeColor('R');
  delay(COLOR_DELAY);
  red = analogRead(A0);


  changeColor('G');
  delay(COLOR_DELAY);
  green = analogRead(A0);

  changeColor('B');
  delay(COLOR_DELAY);
  blue = analogRead(A0);

  
//  Serial.print("\n Vermelho: ");
//  Serial.print(red);
//  Serial.print("\n Verde: ");
//  Serial.print(green);
//  Serial.print("\n Azul: ");
//  Serial.print(blue);

  changeColor(' ');
//
  if (red > green && red > blue) Serial.print("------------ VERMELHO ----------");
  else if (green > red && green > blue) Serial.print("------------ VERDE ----------");
  else if (blue > red && blue > green) Serial.print("------------ AZUL ----------");
  else Serial.println("\n------------ NDA ----------");
  delay(50);
}

void loop() {
  Serial.println("sensor 1");
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  readSensor();
  delay(10);
  Serial.print("sensor 2");
  digitalWrite(2,LOW);
  digitalWrite(3,HIGH);
  readSensor();
  delay(100); 
}