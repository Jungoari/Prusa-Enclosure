// Simple WS2812/3-pin LED strip demo using Adafruit_NeoPixel
#include <Adafruit_NeoPixel.h>

// Adjust these to match your wiring
const uint8_t LED_PIN = 6;
const uint16_t LED_COUNT = 30;
const uint8_t PWM_LED_PIN = 9;  // Separate single LED on PWM-capable pin

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.show();  // Clear on start
  pinMode(PWM_LED_PIN, OUTPUT);
  analogWrite(PWM_LED_PIN, 0);
}

void loop() {
  pwmFade(0, 255, 5, 8);  // Breathe the PWM LED once
  colorWipe(strip.Color(255, 0, 0), 25);   // Red
  colorWipe(strip.Color(0, 255, 0), 25);   // Green
  colorWipe(strip.Color(0, 0, 255), 25);   // Blue
  rainbowCycle(5);
}

// Fills the strip one pixel at a time
void colorWipe(uint32_t color, uint8_t wait) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, color);
    strip.show();
    delay(wait);
  }
}

// Smooth rainbow across the strip
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;
  for (j = 0; j < 256 * 5; j++) {  // 5 cycles
    for (i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Maps a position (0-255) to an RGB color
uint32_t wheel(byte wheelPos) {
  wheelPos = 255 - wheelPos;
  if (wheelPos < 85) {
    return strip.Color(255 - wheelPos * 3, 0, wheelPos * 3);
  }
  if (wheelPos < 170) {
    wheelPos -= 85;
    return strip.Color(0, wheelPos * 3, 255 - wheelPos * 3);
  }
  wheelPos -= 170;
  return strip.Color(wheelPos * 3, 255 - wheelPos * 3, 0);
}

// Simple brightness breathing on a single PWM LED
void pwmFade(uint8_t minVal, uint8_t maxVal, uint8_t step, uint16_t wait) {
  if (step == 0) {
    step = 1;
  }
  for (int16_t v = minVal; v <= maxVal; v += step) {
    analogWrite(PWM_LED_PIN, v);
    delay(wait);
  }
  for (int16_t v = maxVal; v >= minVal; v -= step) {
    analogWrite(PWM_LED_PIN, v);
    delay(wait);
  }
}
