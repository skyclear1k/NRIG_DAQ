"""
Shows Pymodbus TCP client initialization and reading holding registers.
"""
from pymodbus.client import ModbusTcpClient

ip_address = "192.168.1.40"
port = 502

# Initialize the Modbus TCP client
client = ModbusTcpClient(ip_address, port=port)
client.connect()

print(f"Connected to Modbus device at IP: {ip_address}:{port}")
print()

# Example: Read holding registers (adjust address and count as needed for MAQ20)
# MAQ20 low-level registers can be read directly via Modbus function codes
response = client.read_holding_registers(address=0, count=10)

if not response.isError():
    system_info = str(response.registers)
    print("Registers:", system_info)
else:
    system_info = "Error reading from device"
    print(system_info)

print()
print("ip_address: ", ip_address)
print()

with open("output.txt", "w") as f:
    f.write(system_info)

client.close()