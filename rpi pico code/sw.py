from machine import Pin
from time import sleep

print('Microcontrollerslab.com')

led = Pin(0, Pin.OUT)    # 14 number in is Output
push_button = Pin(1, Pin.IN)  # 13 number pin is input

while True:
  
  logic_state = push_button.value()
  if logic_state == True:     # if push_button pressed
      led.value(1)             # led will turn ON
  else:                       # if push_button not pressed
      led.value(0)             # led will turn OFF