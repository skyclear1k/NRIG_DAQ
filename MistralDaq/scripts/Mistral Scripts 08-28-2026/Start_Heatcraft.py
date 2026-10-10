from maq20 import MAQ20
from maq20.modules.diol import DIOL
import time
import datetime
#from pymodbus.client import ModbusTcpClient # using pymodbus 3.9.2
from maq20 import utilities as utils
from openpyxl import Workbook
from pymodbus.client import ModbusTcpClient # using pymodbus 3.9.2

Gateway = ModbusTcpClient('192.168.1.50')      #default is port 502
Gateway.connect()
"""
maq20 = MAQ20(ip_address="192.168.1.30", port=502)
iout  = maq20.find("S0118905-05")
diol1 = maq20.find("S0000000-00")
vout  = maq20.find("S0156303-06")

def get_bit(value, bit_index):
    return (value >> bit_index) & 1
def get_bits(value, start_bit, bit_length):
    mask = (1 << bit_length) - 1
    return (value >> start_bit) & mask
"""

Gateway.write_register(address=2, value = 0, device_id=1)  #Turns off all
time.sleep(1)
print("start program")
Gateway.write_register(address=2, value = 0b10, device_id=1)  # Set latch to enable program
time.sleep(1)
Gateway.write_register(address=2, value = 0, device_id=1)  #Turns off setbit
print("running")