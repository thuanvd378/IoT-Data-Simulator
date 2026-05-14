import time
import random
import json
from datetime import datetime

def generate_sensor_data():
    """Sinh dữ liệu giả lập cho cảm biến IoT"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "device_id": "sensor_01",
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 80.0), 2),
        "heart_rate": random.randint(60, 100)
    }
    return data

def main():
    print("🚀 Khởi động IoT Data Simulator...")
    try:
        while True:
            data = generate_sensor_data()
            print(f"[DATA] {json.dumps(data)}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n🛑 Đã dừng Simulator.")

if __name__ == "__main__":
    main()
