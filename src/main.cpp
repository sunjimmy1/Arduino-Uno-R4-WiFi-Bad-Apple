#include "Arduino_LED_Matrix.h"
#include "image.h"
ArduinoLEDMatrix matrix;

void setup()
{
  Serial.begin(115200);
  matrix.begin();
}

void loop()
{
  for (int i = 0; i < 1308; i++)
  {
    matrix.loadFrame(frames[i]);
    delay(1000 / 6);
  }
}