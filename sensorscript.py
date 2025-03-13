import time
import random
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"  # Public broker for testing
TOPIC = "diamondback/sensors"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER, 1883, 60)

while True:
    sensor_data = {
        "pressure": round(random.uniform(100, 500), 2),
        "temperature": round(random.uniform(50, 200), 2),
        "flow_rate": round(random.uniform(10, 100), 2)
    }
    client.publish(TOPIC, str(sensor_data))
    print(f"Sent: {sensor_data}")
    time.sleep(5)  # Simulate real-time data every 5 sec