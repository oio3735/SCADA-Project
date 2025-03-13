import sqlite3
import json
import smtplib
from email.mime.text import MIMEText
import paho.mqtt.client as mqtt

ALERT_THRESHOLD = {"pressure": 400, "temperature": 150, "flow_rate": 80}

def send_alert(sensor, value):
    msg = MIMEText(f"ALERT! {sensor} exceeded limit: {value}")
    msg["Subject"] = "Diamondback SCADA Alert"
    msg["From"] = "your-email@example.com"
    msg["To"] = "engineer@example.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your-email@example.com", "your-app-password")
        server.sendmail(msg["From"], msg["To"], msg.as_string())

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO sensors (pressure, temperature, flow_rate) VALUES (?, ?, ?)", 
                   (data["pressure"], data["temperature"], data["flow_rate"]))
    
    conn.commit()
    
    # Check for alerts
    for sensor, value in data.items():
        if value > ALERT_THRESHOLD[sensor]:
            send_alert(sensor, value)
    
    conn.close()

MQTT_BROKER = "broker.hivemq.com"
TOPIC = "diamondback/sensors"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(TOPIC)
client.on_message = on_message
client.loop_forever()