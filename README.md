# SYN Flood Tool

## Overview
The **SYN Flood Tool** is a Python-based graphical application built using **Tkinter** and **Scapy** that allows you to launch a SYN flood attack on a specified target IP or hostname and port. This tool sends TCP SYN packets to the target to overwhelm the system with traffic. It is designed to simulate a SYN flood DoS attack for educational purposes only.

### Key Features
- **SYN Flood Attack**: Uses the Scapy library to send SYN packets to a target IP and port.
- **Configurable Attack Parameters**: Adjust the request frequency and the number of concurrent threads used to send packets.
- **Graphical User Interface (GUI)**: Built with Tkinter, providing an easy-to-use interface for launching and stopping attacks.
- **Real-Time Logs**: Displays a live log of the attack progress in the GUI.

## Tools, Languages, and Libraries Used
- **Python**: The primary programming language used for building the tool.
- **Tkinter**: Used to create the graphical user interface (GUI).
- **Scapy**: A powerful Python library for packet manipulation and network analysis, used to send the SYN packets.
- **Threading**: Used to send packets concurrently across multiple threads to simulate a more aggressive attack.
- **Socket**: Utilized for resolving hostnames to IP addresses.


## How to Use

### Enter Attack Parameters:
- **Target IP or Hostname**: Enter the target IP address or hostname.
- **Target Port**: Enter the target port (e.g., 80 for HTTP).
- **Request Frequency**: Set how often packets should be sent, with a range of 0.001 to 0.1 seconds.
- **Number of Concurrent Threads**: Specify the number of threads (1-500) for sending packets simultaneously.

### Start the Attack:
Click the **"Start Attack"** button to initiate the SYN flood attack.

### Stop the Attack:
Click the **"Stop Attack"** button to halt the attack and stop sending SYN packets.

## Disclaimer
This tool is intended for **educational purposes only**. Use responsibly and only on systems that you have permission to test. Do not perform SYN flood attacks on any network or server without authorization, as this is illegal and can result in criminal charges.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/syn-flood-tool.git
   cd syn-flood-tool

2. Create a Virtual Environment
   ```bash
   python -m venv .venv

   
