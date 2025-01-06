import network
import espnow
import machine
from time import sleep

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
            
        elif msg == b'ledOff':
            print("Turning off LED")
            led_pin.off()
           
       else:
            print(f"Unknown message! {msg}") 
