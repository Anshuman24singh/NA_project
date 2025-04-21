import time

host = "192.168.2.1"
print(f"Connecting to {host} via SSH...")
time.sleep(1)
print("Connected!")

print("\nSending command: show ip interface brief")
time.sleep(1)

output = """
Interface              IP-Address      OK? Method Status   Protocol
GigabitEthernet0/0     192.168.2.1     YES manual up       up
GigabitEthernet0/1     10.0.0.2        YES manual up       up
"""

print("\nCommand Output:\n")
print(output)

print("\nSSH connection closed.")
