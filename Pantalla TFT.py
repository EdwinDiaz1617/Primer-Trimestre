import machine
from time import sleep
import ujson
from math import sin, cos, radians
from ST7735 import TFT, TFTColor
from machine import SPI, Pin
from sysfont import sysfont
# Configuración de pines y pantalla
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft = TFT(spi, 16, 17, 18)
# Inicialización de la pantalla TFT
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)

h = "Edwin"
c = "Completo"

for i in range(11):
    
    tft.text((15, 30), h, TFT.WHITE, sysfont)  
    tft.text((15, 80), str(i), TFT.WHITE, sysfont) 
    sleep(0.5)
        
if i == 10:
    tft.text((15, 100), c ,TFT.WHITE, sysfont)  
    sleep(2)