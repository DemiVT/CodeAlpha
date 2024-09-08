
# Network Security Projects

This repository contains several network security projects:

1. **Basic Network Sniffer**
2. **Phishing Awareness Training Web App**
3. **Secure Coding Review**
4. **Network Intrusion Detection System (Snort)**

## Table of Contents

- [Basic Network Sniffer](#basic-network-sniffer)
- [Phishing Awareness Training Web App](#phishing-awareness-training-web-app)
- [Secure Coding Review](#secure-coding-review)
- [Network Intrusion Detection System (Snort)](#network-intrusion-detection-system-snort)

## Basic Network Sniffer

### Description
A Python-based network sniffer that captures and analyzes network traffic using the Scapy library.

### Requirements
- Python 3.x
- Scapy

### Installation

1. Install Scapy:
   ```bash
   pip install scapy
   ```

2. Save the following code as `sniffer.py`:

   ```python
   from scapy.all import sniff

   def packet_callback(packet):
       print(f"Packet: {packet.summary()}")

   def start_sniffing(interface):
       print(f"Sniffing on interface {interface}...")
       sniff(iface=interface, prn=packet_callback, store=0)

   if __name__ == "__main__":
       import sys
       if len(sys.argv) != 2:
           print("Usage: python sniffer.py <interface>")
           sys.exit(1)
       interface = sys.argv[1]
       start_sniffing(interface)
   ```

### Usage
Run the sniffer with:
   ```bash
   sudo python sniffer.py <interface>
   ```

Replace `<interface>` with your network interface name (e.g., `eth0`, `wlan0`).

## Phishing Awareness Training Web App

### Description
A Flask-based web application designed to educate users about phishing attacks and prevention.

### Requirements
- Python 3.x
- Flask

### Installation

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Save the following code as `app.py`:

   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   @app.route('/examples')
   def examples():
       return render_template('examples.html')

   @app.route('/tips')
   def tips():
       return render_template('tips.html')

   @app.route('/reporting')
   def reporting():
       return render_template('reporting.html')

   if __name__ == "__main__":
       app.run(debug=True)
   ```

3. Create HTML templates in the `templates` folder:
   - `index.html`
   - `examples.html`
   - `tips.html`
   - `reporting.html`

### Usage
Run the Flask app with:
   ```bash
   python app.py
   ```

## Secure Coding Review

### Description
A static code analysis using Bandit to identify potential security vulnerabilities.

### Requirements
- Python 3.x
- Bandit

### Installation

1. Install Bandit:
   ```bash
   pip install bandit
   ```

2. Save the following code as `app.py`:

   ```python
   def unsafe_function(user_input):
       query = f"SELECT * FROM users WHERE name='{user_input}'"
       execute_query(query)
   ```

### Usage
Run Bandit with:
   ```bash
   bandit -r app.py
   ```

## Network Intrusion Detection System (Snort)

### Description
Set up and configure Snort to monitor network traffic for suspicious activity.

### Requirements
- Snort

### Installation

1. Install Snort:
   ```bash
   sudo apt-get update
   sudo apt-get install snort
   ```

2. Configure Snort by editing `/etc/snort/snort.conf`.

3. Save your custom rules in `/etc/snort/rules/local.rules`.

### Usage
Run Snort with:
   ```bash
   sudo snort -A console -c /etc/snort/snort.conf -i eth0
   ```

Replace `/etc/snort/snort.conf` with the path to your Snort configuration file and `eth0` with your network interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Scapy for network sniffing.
- Flask for web development.
- Bandit for static code analysis.
- Snort for network intrusion detection.

