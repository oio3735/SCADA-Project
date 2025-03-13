Overview
This project is an MQTT-based SCADA Monitoring & Alert System designed for industrial automation. It:

Receives sensor data via MQTT (broker.hivemq.com)
Stores sensor data in an SQLite database (sensor_data.db)
Sends email alerts when sensor values exceed predefined thresholds
This system is optimized for oil & gas automation, but it can be adapted for any industry requiring remote monitoring.

Features
Real-time MQTT data collection
Automated database storage (SQLite)
Email alerts for critical values (SMTP via Gmail)
Configurable thresholds and settings

Installation & Setup
1. Clone the Repository
    git clone https://github.com/your-username/SCADA-Project.git
    cd SCADA-Project
2. Install Dependencies
    pip install -r requirements.txt
    (Ensure python-dotenv, paho-mqtt, and smtplib are installed.)
3. Set Up Environment Variables
    Create a config.env file in the project directory:
    EMAIL_USER=your-email@gmail.com
    EMAIL_PASS=your-16-character-app-password  # Get from Google App Passwords
    MQTT_BROKER=broker.hivemq.com
    Use a Gmail App Password, not your real password.
    Do not commit config.env to GitHub for security reasons.

Running the System
1. Start the MQTT Listener
    This script listens for incoming sensor data:
    python main.py
2. Send a Test MQTT Message
    To manually publish test sensor data, run:
    python sensorscript.py
    Or use the HiveMQ Web MQTT Client
    Broker: broker.hivemq.com
    Topic: diamondback/sensors
Example message:
    {"pressure": 410, "temperature": 160, "flow_rate": 85}
3. Check for Email Alerts
    If a sensor value exceeds the threshold, an email alert will be sent.
    Check your email inbox (or spam folder).

Contact & Contributions: Feel free to contribute, report issues, or fork the project.
Created by Ibrahim Oyewunmi.