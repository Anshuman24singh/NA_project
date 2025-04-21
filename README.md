# NA_project
🚀 Network Automation with Python and Cisco Packet Tracer
Automated SSH-based Router Access & Monitoring

📘 Project Overview
This project demonstrates how to automate router access using Python’s Paramiko library and simulate network routing and SSH configuration using Cisco Packet Tracer. It features:

A 2-router, 2-PC topology

Static routing between routers

SSH enabled on Router2

SSH access tested from PC1

Python script to simulate SSH automation with command output

🖥️ Network Topology
css
Copy code
[ PC1 ] → [ Router1 ] ←→ [ Router2 ] ← [ PC2 ]
PC1 (192.168.1.10) → connects to Router1 → connects to Router2 (192.168.2.1)

PC1 uses SSH to remotely access Router2

🛠️ Tools Used
Cisco Packet Tracer (v8.2+ recommended)

Python 3.x

Paramiko library (for SSH)

Windows / Linux Terminal

🧱 Folder Structure
graphql
Copy code
network-automation-project/
│
├── main.py                   # Automates SSH access to routers using CSV
├── router_ssh.py             # Simple single-device SSH demo script
├── device_list.csv           # List of routers to connect to via SSH
├── logs/                     # Output folder for captured command results
└── README.md                 # You're reading it 😄
📂 device_list.csv Format
Add your router/device info like this:

csv
Copy code
device_name,ip,username
Router2,192.168.2.1,admin
🐍 Python Script 1: router_ssh.py
A simple script to simulate connecting to Router2 and running a command.

bash
Copy code
python router_ssh.py
Outputs: show ip interface brief results (simulated or real).

🐍 Python Script 2: main.py
Connects to multiple routers (via CSV) and executes SSH commands.

Install dependencies first:

bash
Copy code
pip install paramiko
Then run:

bash
Copy code
python main.py
The script will:

Prompt you for the SSH password

Connect to each device listed in device_list.csv

Run show ip interface brief

Save output in logs/

✅ Expected Output
SSH login to 192.168.2.1

Command: show ip interface brief

Output saved in logs/ directory like: logs/Router2_20250421_143233.txt

