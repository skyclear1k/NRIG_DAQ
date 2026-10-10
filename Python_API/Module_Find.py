"""
This example shows how to connect using Pymodbus, query module 
identification registers, and check for a specific module (such as VDN).
"""
from pymodbus.client import ModbusTcpClient

ip_address = "192.168.1.40"
port = 502
module_to_find = "ISN"

# Initialize and connect the Modbus TCP client
client = ModbusTcpClient(ip_address, port=port)
client.connect()

found_module = None

# Pymodbus is a low-level protocol client and does not have a built-in 
# .find() method. Module identification requires reading the specific 
# Modbus registers assigned to each slot in the MAQ20 memory map.
# Example: Iterate through slot base addresses to read module identity registers
slot_base_addresses = [100, 200, 300, 400]  # Adjust based on MAQ20 register map manual

for slot_idx, base_addr in enumerate(slot_base_addresses):
    response = client.read_holding_registers(address=base_addr, count=4)
    
    if not response.isError():
        registers = response.registers
        # Convert register values to ASCII or match against known device ID codes
        # decoded_name = ''.join(chr(reg >> 8) + chr(reg & 0xFF) for reg in registers)
        
        # Simulating check for demonstration purposes:
        # if module_to_find in decoded_name:
        #     found_module = {"slot": slot_idx, "model": decoded_name, "data": registers}
        #     break
        pass

# Check if module was not found and raise an error matching the original logic
if found_module is None:
    raise ValueError("Module not found")

print(found_module)

client.close()