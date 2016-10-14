#include <OneWire.h>
#include <DHT11.h>

#define PIN_HUMIDITY1 A0
#define PIN_HUMIDITY2 A1
#define PIN_LIGHT     A2

#define PIN_TEMPERATURE 2
#define PIN_DHTXX1      3
#define PIN_DHTXX2      4

#define PIN_RELAY_LIGHT 8
#define PIN_RELAY_WIND  9
#define PIN_RELAY_WATER 10

#define USE_SECOND_TEMPERATURE_SENSOR false
#define USE_SECOND_DHTXX_SENSOR false


OneWire temp(PIN_TEMPERATURE);
byte temp_addr[2][8];

DHT11 dht1(PIN_DHTXX1);

#if USE_SECOND_DHTXX_SENSOR
DHT11 dht2(PIN_DHTXX2);
#endif

float ext1_h_old, ext1_t_old, ext2_h_old, ext2_t_old;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  temp.search(temp_addr[0]);

#if USE_SECOND_TEMPERATURE_SENSOR
  temp.search(temp_addr[1]);
#endif

  pinMode(PIN_RELAY_LIGHT, OUTPUT);
  pinMode(PIN_RELAY_WIND, OUTPUT);
  pinMode(PIN_RELAY_WATER, OUTPUT);
  digitalWrite(PIN_RELAY_LIGHT, LOW);
  digitalWrite(PIN_RELAY_WIND, LOW);
  digitalWrite(PIN_RELAY_WATER, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  int analog0 = analogRead(PIN_HUMIDITY1);
  int analog1 = analogRead(PIN_HUMIDITY2);
  int analog2 = analogRead(PIN_LIGHT);

  float humitat1 = (1023 - analog0)/1024.0*100;
  float humitat2 = (1023 - analog1)/1024.0*100;
  float llum = (1023 - analog2)/1024.0*100;

  float ext1_h, ext1_t, ext2_h, ext2_t;

  if (dht1.read(ext1_h, ext1_t) == 0) {
    ext1_h_old = ext1_h;
    ext1_t_old = ext1_t;
  }

#if USE_SECOND_DHTXX_SENSOR
  if (dht2.read(ext2_h, ext2_t) == 0) {
    ext2_h_old = ext2_h;
    ext2_t_old = ext2_t;
  }
#endif



  Serial.print(ext1_h_old); //id 0
  Serial.print("|");
#if USE_SECOND_DHTXX_SENSOR
  Serial.print(ext2_h_old); //id 1
#else
  Serial.print("00.00");
#endif
  Serial.print("|");
  Serial.print(humitat1); //id 2
  Serial.print("|");
  Serial.print(humitat2); //id 3
  Serial.print("|");
  Serial.print(ext1_t_old); //id 4
  Serial.print("|");
#if USE_SECOND_DHTXX_SENSOR
  Serial.print(ext2_t_old); //id 5
#else
  Serial.print("00.00");
#endif
  Serial.print("|");
  Serial.print(getTemp(0)); //id 6
  Serial.print("|");
#if USE_SECOND_TEMPERATURE_SENSOR
  Serial.print(getTemp(1)); //id 7
#else
  Serial.print("00.00");
#endif
  Serial.print("|");
  Serial.print(llum);
  Serial.print("\n");

  while (Serial.available()) {
    char c = Serial.read();

    switch(c) {
      case 'a':
        digitalWrite(PIN_RELAY_LIGHT, LOW);
        break;

      case 'b':
        digitalWrite(PIN_RELAY_LIGHT, HIGH);
        break;

      case 'c':
        digitalWrite(PIN_RELAY_WIND, LOW);
        break;

      case 'd':
        digitalWrite(PIN_RELAY_WIND, HIGH);
        break;

      case 'e':
        digitalWrite(PIN_RELAY_WATER, LOW);
        break;

      case 'f':
        digitalWrite(PIN_RELAY_WATER, HIGH);
        break;
    }

  }

  delay(5000);

}
