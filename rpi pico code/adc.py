import time
from machine import Pin

analog_value=machine.ADC(28)
conversion_factor=655.35
print('Microcontrollerslab.com')

while True:
  logic_state = analog_value.read_u16()
  print("ADC: ",logic_state)
  percentage=logic_state/conversion_factor
  print("ADC: ",percentage,"%")
  time.sleep(0.5)