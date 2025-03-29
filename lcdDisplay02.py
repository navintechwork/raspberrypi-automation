import os

import time

from RPLCD.i2c import CharLCD

# Initialize the LCD

lcd = CharLCD('PCF8574', 0x27) # Adjust the address if necessary

def get_ip_address():

    ip_address = os.popen('hostname -I').read().strip()

    return ip_address

# try:

while True:

    ip = get_ip_address()

    lcd.clear()

    lcd.write_string("IP Address:")

    lcd.crlf() # Move to the next line

    lcd.write_string(ip)

    time.sleep(5)