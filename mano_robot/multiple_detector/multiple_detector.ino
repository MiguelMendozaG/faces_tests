//detector multiple arduino-dlib

#include <Servo.h>
Servo servo_1;  
Servo servo_2;
Servo servo_3;
Servo servo_4;

// al presionar reset inicia la secuencia
void setup() {    
  Serial.begin(9600);

 servo_1.attach(3);
 servo_2.attach(5); 
 servo_3.attach(7);
 servo_4.attach(9);
}
 
// ciclo infinito
void loop() {
  if(Serial.available()) {
    char in = Serial.read();

if(in == 'B'){
   servo_1.write(120);
 servo_2.write(120);
 servo_3.write(120);
 servo_4.write(0);

}

if(in == 'Q'){

 servo_1.write(0);
 servo_2.write(0);
 servo_3.write(0);
 servo_4.write(60);

}
 if (in == 'H'){
     servo_1.write(120);
 servo_2.write(120);
 servo_3.write(0);
 servo_4.write(0);
  }
  }
}
