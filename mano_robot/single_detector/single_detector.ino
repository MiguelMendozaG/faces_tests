//detector individual arduino-dlib

#include <Servo.h>
Servo servo_1;  

// al presionar reset inicia la secuencia
void setup() {    
  Serial.begin(9600);

 servo_1.attach(3);
}
 
// ciclo infinito
void loop() {
  if(Serial.available()) {
    char in = Serial.read();


if(in == 'Q'){
   servo_1.write(120);

 }
 if (in == 'W'){
    servo_1.write(0);
  }
}
}
