# Networking Stress-Testing Tool

## Overview
Developed a Python-based network security tool with a graphical interface (Tkinter) and packet manipulation capabilities (Scapy) to simulate SYN flood attacks for educational and penetration testing purposes.

### Key Features
- **SYN Flood Attack**: Uses the Scapy library to send SYN packets to a target IP and port.
- **Configurable Attack Parameters**: Allows adjustment of request frequency and the number of concurrent threads for packet transmission.
- **Graphical User Interface (GUI)**: Built with Tkinter for an intuitive interface to launch and stop attacks.
- **Real-Time Logs**: Displays live attack progress within the GUI.

## Tools, Languages, and Libraries Used
- **Python**: The primary programming language used for building the tool.
- **Tkinter**: Used to create the graphical user interface (GUI).
- **Scapy**: A powerful Python library for packet manipulation and network analysis, used to send the SYN packets.
- **Threading**: Used to send packets concurrently across multiple threads to simulate a more aggressive attack.
- **Socket**: Utilized for resolving hostnames to IP addresses.

## Disclaimer
This tool is intended for **educational purposes only**. Use responsibly and only on systems that you have permission to test. Do not perform SYN flood attacks on any network or server without authorization, as this is illegal and can result in criminal charges.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



   
