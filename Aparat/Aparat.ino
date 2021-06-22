
#define p1 5
#define p2 6
#define p3 7
#define p4 8
#define p5 9
#define p6 10
#define pON 12

int incomingByte;
int pin;
int mode;
int pinCount;

void setup(){
  Serial.begin(9600);
  pinMode(p1, OUTPUT);
  pinMode(p2, OUTPUT);
  pinMode(p3, OUTPUT);
  pinMode(p4, OUTPUT);
  pinMode(p5, OUTPUT);
  pinMode(p6, OUTPUT);
  pinMode(pON,OUTPUT);
  
  pinCount = 6;
}

void loop(){
  if(Serial.available() > 0){
    digitalWrite(pON,HIGH);
    incomingByte = Serial.parseInt();
    pin = ((incomingByte - incomingByte % 10) / 10) + 4;
    mode = incomingByte % 10;
    
    if(mode != 0 && mode != 1){
      mode = 0;
    }
    if(pin <= pinCount + 4){
      Serial.println(pin);
      Serial.println(mode);
      digitalWrite(pin, mode);
    }
  }
}
