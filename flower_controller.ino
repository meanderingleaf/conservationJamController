#define photo_pin A0
#define pressure_pin A1
#define water_pin A3


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int photo_value = analogRead(photo_pin);
  Serial.print("Photo: ");
  Serial.println(photo_value);

  delay(1000);

  // put your main code here, to run repeatedly:
  int pressure_value = analogRead(pressure_pin);
  Serial.print("Pressure: ");
  Serial.println(pressure_value);

  delay(1000);

  // put your main code here, to run repeatedly:
  int water_value = analogRead(water_pin);
  Serial.print("Water: ");
  Serial.println(water_value);

  delay(1000);
  

  
}
