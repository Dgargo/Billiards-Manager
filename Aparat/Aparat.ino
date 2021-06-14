int pin
int mode
int incomingByte
int pinCount

void setup(){
  Serial.begin(9600);
   for(var i = 5 ;i<11 :i++){
    pinMode(i,OUTPUT);
    }
    pinCount = 6;
  }

void loop(){
  if(Serial.available()>0){
    incomingByte = Serial.parseInt();
    pin =((incomingByte-incomingByte%10)/10)+4;
    mode = incomingByte%10;

    if(mode !=0 && mode!=1){
      mode = 0;
      }
    if(pin <= pinCount+4){
      digitalWrite(pin,mode);
      }
      
    }
  }
