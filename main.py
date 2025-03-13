from mqtt_listener import start_mqtt_listener
from database import create_table

if __name__ == "__main__":
    print("🚀 Starting SCADA Monitoring System...")
    
    # Ensure the database table exists before receiving data
    create_table()
    
    # Start MQTT Listener (runs indefinitely)
    start_mqtt_listener()