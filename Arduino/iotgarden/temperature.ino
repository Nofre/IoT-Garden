

String getTemp(int sensor) {
  byte data[12];
  char buf[7];

  if ( OneWire::crc8( temp_addr[sensor], 7) != temp_addr[sensor][7]) return " ";
  if ( temp_addr[sensor][0] != 0x10) return " ";

  temp.reset();
  temp.select(temp_addr[sensor]);
  temp.write(0x44,1);         // start conversion, with parasite power on at the end

  delay(1000);     // maybe 750ms is enough, maybe not

  temp.reset();
  temp.select(temp_addr[sensor]);    
  temp.write(0xBE);         // Read Scratchpad

  for (int i = 0; i < 9; i++) {  // we need 9 bytes
    data[i] = temp.read();
  }

  int TReading = (data[1] << 8) + data[0];
  int SignBit = TReading & 0x8000;  // test most sig bit
    
  if (SignBit) {  // negative
    TReading = (TReading ^ 0xffff) + 1; // 2's comp
  }
    
  int Tc_100 = (TReading*100/2);    

  int Whole = Tc_100 / 100;  // separate off the whole and fractional portions
  int Fract = Tc_100 % 100;

  sprintf(buf, "%d.%d",Whole, Fract);

  return buf;
}
