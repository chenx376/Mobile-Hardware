/* Vibration Sensor (Shake Switch) - Testing with buzzer

   In this tutorial we will use one vibration sensor (or shake switch) 
   to make a beep sound from a buzzer while we shake our breadboard.
   
   Find more info and video here: http://bit.ly/1iDbc2Q
   
   Dev: Michalis Vasilakis - Date: 9/9/2015 - www.ardumotive.com       */
   
const int buzzer = 8; //Buzzer connected to pin 8 of Arduino uno / mega
int sensor;           //Variable to store analog value (0-1023)
int timestamp = 0;

void setup()
{
  Serial.begin(9600);      //Only for debugging
  pinMode(buzzer, OUTPUT);
  Serial.println("Begin");
  
}

void loop()
{
  sensor = analogRead(A0);  
  //While sensor is not moving, analog pin receive 1023~1024 value
  if (sensor<1022){
    tone(buzzer, 500);
//    Serial.print(timestamp);
//    Serial.print(" : ");
    Serial.println(sensor);
  }
  
  else{ 
    noTone(buzzer);
//    Serial.print(timestamp);
//    Serial.print(" : ");
    Serial.println(sensor);
  }
//  timestamp += 1;
  delay(100); //Small delay
}
