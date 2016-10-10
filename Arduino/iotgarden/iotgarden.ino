#include <OneWire.h>
#include <DHT11.h>


OneWire temp(2);
byte temp_addr[2][8];

DHT11 dht1(3);
DHT11 dht2(4);

float ext1_h_old, ext1_t_old, ext2_h_old, ext2_t_old;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  temp.search(temp_addr[0]);
  temp.search(temp_addr[1]);

  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  int analog0 = analogRead(A0);
  int analog1 = analogRead(A1);
  int analog2 = analogRead(A2);

  float humitat1 = (1023 - analog0)/1024.0*100;
  float humitat2 = (1023 - analog1)/1024.0*100;
  float llum = (1023 - analog2)/1024.0*100;

  float ext1_h, ext1_t, ext2_h, ext2_t;

  if (dht1.read(ext1_h, ext1_t) == 0) {
    ext1_h_old = ext1_h;
    ext1_t_old = ext1_t;
  }

  if (dht2.read(ext2_h, ext2_t) == 0) {
    ext2_h_old = ext2_h;
    ext2_t_old = ext2_t;
  }



  Serial.print(ext1_h_old); //id 0
  Serial.print("|");
  Serial.print(ext2_h_old); //id 1
  Serial.print("|");
  Serial.print(humitat1); //id 2
  Serial.print("|");
  Serial.print(humitat2); //id 3
  Serial.print("|");
  Serial.print(ext1_t_old); //id 4
  Serial.print("|");
  Serial.print(ext2_t_old); //id 5
  Serial.print("|");
  Serial.print(getTemp(0)); //id 6
  Serial.print("|");
  Serial.print(getTemp(1)); //id 7
  Serial.print("|");
  Serial.print(llum);
  Serial.print("\n");

  while (Serial.available()) {
    char c = Serial.read();

    switch(c) {
      case 'a':
        digitalWrite(7, LOW);
        break;

      case 'b':
        digitalWrite(7, HIGH);
        break;

      case 'c':
        digitalWrite(8, LOW);
        break;

      case 'd':
        digitalWrite(8, HIGH);
        break;

      case 'e':
        digitalWrite(9, LOW);
        break;

      case 'f':
        digitalWrite(9, HIGH);
        break;
    }

  }

  delay(5000);

}
