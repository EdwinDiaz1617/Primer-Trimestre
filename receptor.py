import network
import espnow
import machine

from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColums = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColums)

lcd.display_off()





sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266

# Initialize ESP-NOW
esp = espnow.ESPNow()
esp.active(True)

led_pin = machine.Pin(23, machine.Pin.OUT)

while True:
    _, msg = esp.recv()
    if msg:             # msg == None if timeout in recv()
        if msg == b'ledOn':
            print("Turning on LED")
            led_pin.on()
            lcd.display_on()
            lcd.move_to(0,0)
            lcd.putstr("Conectado")
           
        elif msg == b'ledOff':
            print("Turning off LED")
            led_pin.off()
            lcd.display_on()
            lcd.move_to(0,0)
            lcd.putstr("Desconectado")
            
            
            
        else:
            print(f"Unknown message! {msg}") 