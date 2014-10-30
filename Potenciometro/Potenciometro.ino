

int LED12;
int pot; 
int n = 0;
int estado = 0;
int z = 0;
int y = 0;
int anterior = 0;
int encender = 0;
int interval = 2000;
long prev_Millis = 0;
String cadena;
char datos_puerta;


void setup()
{
     Serial.begin (9600);
     pinMode(12,OUTPUT);
     pinMode(13,OUTPUT); 
     pinMode(8,INPUT); 
  
}

void loop()
{
      if (millis() > prev_Millis + interval)          //Este condicional nos lee cada cierto tiempo (interval) tanto el potenciometro como el estado del pin 12
      {
          pot = analogRead(0);                        //Segun el valor de este ultimo le añadimos "z" o "y" a la cadena de informacion mandada al txt
          LED12 = digitalRead(12);
          if (LED12 == HIGH)                          //El estado del PIN 12 nos indica si la bombilla esta apagada o encendida
          {
              cadena = String("z");
              cadena = cadena + pot;          
              if (z == 0)
              {
                z=1;
              }
          }
          if (LED12 == LOW)
          {
              cadena = String("y");
              cadena = cadena + pot;
              if (z == 1)
                z=0;
              
          }
          Serial.println(cadena);
          prev_Millis = millis();
      }
      
      estado = digitalRead(8);
    
      if (estado && anterior == 0)                  //Esta parte realiza el encendido/apagado del pin 12 mediante un solo pulsador conectado al pin 8
      {
       encender = 1 - encender;
       delay(30); 
      }
      
      anterior = estado;
      if (encender)
      {
        digitalWrite(12,HIGH);

      }
      else
      {
        digitalWrite(12,LOW);

      }
      datos_puerta = Serial.read();                //Aqui leemos datos escritos en el txt por el controlador de Web2py y actuamos en consecuencia
      if (datos_puerta == 'a')
        digitalWrite(13,HIGH);                     //Para abrir la puerta (PIN 13) recibiriamos una 'a' y para cerrarla una 'b'
        
      if (datos_puerta == 'b')
        digitalWrite(13,LOW);
            
}
