
float rango=2,ciclo=0,cambiodeciclo=0,valledetension=1023;
float ultimamedicion,picodetension,contadorvisualizacion,contadorciclo;
float capacitor,frecuencia;
void setup(){
  Serial.begin(9600),pinMode(A0, INPUT);}
void loop() 
{    long sensorValue = analogRead(A0); 
      if (micros()>contadorvisualizacion+10000000)
        {
         int frecuencia = contadorciclo; 
         capacitor=48000/(frecuencia);
         int ct=capacitor;

         Serial.println(ct);
         delay(500);
         rango=(2+((picodetension-valledetension)/5)),contadorvisualizacion=micros();
         picodetension=sensorValue, valledetension=sensorValue,contadorciclo=0;
        }   
      if (sensorValue>=(ultimamedicion+rango)){ ultimamedicion = sensorValue,ciclo=1; 
      if (sensorValue>picodetension){picodetension=sensorValue;} }
      if (sensorValue <= ( ultimamedicion-rango)){ ultimamedicion = sensorValue, ciclo=0;
      if (sensorValue<valledetension){valledetension=sensorValue;}}
      if (ciclo==1 && cambiodeciclo==0){cambiodeciclo=1,contadorciclo++;}
      if (ciclo==0 && cambiodeciclo==1){cambiodeciclo=0;}    
}
