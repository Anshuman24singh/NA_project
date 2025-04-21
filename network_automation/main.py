import paramiko
import csv
import getpass
from datetime import datetime
import os


if not os.path.exists("logs"):
    os.makedirs("logs")


password = getpass.getpass("Enter SSH password for all devices: ")


with open("device_list.csv", "r") as f:
    reader = csv.DictReader(f)
    devices = [row for row in reader]


for device in devices:
    print(f"\nConnecting to {device['device_name']} ({device['ip']})...")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=device["ip"],
            port=22,
            username=device["username"],
            password=password
        )

        stdin, stdout, stderr = client.exec_command("show ip interface brief")
        output = stdout.read().decode()
        err = stderr.read().decode()

        filename = f"logs/{device['device_name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as log_file:
            log_file.write(output)

        print(f"Command executed successfully. Output saved to {filename}")
        if err:
            print("Errors:\n", err)

    except Exception as e:
        print(f"Connection to {device['device_name']} failed: {e}")
    finally:
        client.close()
