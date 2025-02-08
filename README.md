### **Networking Stress-Testing Tool**

### **Overview**  
  The **Networking Stress-Testing Tool** is a Python-based application developed to simulate SYN flood attacks, a common denial-of-service (DoS) attack method. Designed with a graphical user interface (GUI) using Tkinter and enhanced with packet manipulation capabilities via Scapy, this tool allows users to simulate stress testing on networks for educational and penetration testing purposes.

> **⚠️ Disclaimer:** This tool is intended for **educational purposes only**. It should be used responsibly and only on systems you have explicit permission to test. Performing SYN flood attacks on unauthorized networks or servers is illegal and may lead to severe legal consequences.

### **Key Features**  
  - **SYN Flood Attack Simulation**: Uses the Scapy library to simulate SYN flood attacks by sending SYN packets to a target IP and port.  
  - **Customizable Parameters**: Adjust the attack parameters, such as request frequency and number of concurrent threads, to simulate different attack intensities.  
  - **Intuitive GUI**: Built with Tkinter to offer a user-friendly interface that makes launching and stopping attacks easy.  
  - **Real-Time Logs**: View live progress of the attack and monitor the results through the GUI, providing immediate feedback on the attack’s impact.

### **Tools, Languages, and Libraries Used**  
  - **Python** – The primary language used for tool development.  
  - **Tkinter** – Framework for building the graphical user interface (GUI).  
  - **Scapy** – Python library used for creating and sending SYN packets to target systems.  
  - **Threading** – Enables sending packets concurrently across multiple threads to simulate a more aggressive attack.  
  - **Socket** – Used for resolving hostnames to IP addresses, facilitating attack targeting.

