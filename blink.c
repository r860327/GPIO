#include <wiringPi.h>
int main ()
{
    wiringPiSetup () ;
    pinMode (0, OUTPUT) ;
    for (;;)
    {
        digitalWrite(0, HIGH) ; delay(1500) ;
        digitalWrite(0,  LOW) ; delay(1500) ;
    }
}

