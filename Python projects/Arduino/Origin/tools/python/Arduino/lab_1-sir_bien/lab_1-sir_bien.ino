// Exercise 1.1

// void setup() {
//   // put your setup code here, to run once:
//   pinMode (9, OUTPUT);
//   Serial.begin (115200) ;
//   digitalWrite (9, HIGH);



// }

// void loop() {
//   // put your main code here, to run repeatedly:
 
// }

// Exercise 1.2

// void setup() {
//   // put your setup code here, to run once:
//   pinMode (9, OUTPUT);
//   Serial.begin (115200) ;
//   digitalWrite (9, HIGH);
//   delay(2000);
//   digitalWrite(9, LOW);



// }

// void loop() {
//   // put your main code here, to run repeatedly:
 
// }

// Exercise 1.3

// void setup() {
//   // put your setup code here, to run once:
//   pinMode (9, OUTPUT);
//   Serial.begin (115200) ;
//   digitalWrite (9, HIGH);
//   digitalWrite (11, HIGH);
//   delay(5000);
//   digitalWrite(9, LOW);
//   delay(3000);
//   digitalWrite(11, LOW);



// }

// void loop() {
//   // put your main code here, to run repeatedly:
 
// }

// Exercise 1.4

int i = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode (10, OUTPUT);
  Serial.begin (115200) ;
  for (i = 0; i < 5; i++) 
  {
    digitalWrite(10, HIGH); // turn the LED on (HIGH is the voltage level)
    delay(1000); // wait for a second
    digitalWrite(10, LOW); // turn the LED off by making the voltage LOW)
    delay(1000); // wait for a second
  
  }
}

void loop() {
  // put your main code here, to run repeatedly:
 
}
