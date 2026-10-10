"""
Shows MAQ20 initialization and prints information about the system.
"""
from maq20 import MAQ20
ip_address = "192.168.1.40"

system0 = MAQ20(ip_address=ip_address, port=502)
# system0 = MAQ20(virtual_com=True, port="COM24")

print(system0)
print()
print("ip_address: ",ip_address)
print()

with open("output.txt", "w") as f:
    f.write(str(system0))


