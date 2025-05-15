import rclpy
from rclpy.node import Node
import serial
import time

class PlantBot(Node):
    def __init__(self):
        super().__init__('plant_bot_node')
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        time.sleep(2)  # Wait for serial to initialize
        self.timer = self.create_timer(5.0, self.read_moisture)

    def read_moisture(self):
        try:
            self.ser.write(b'R')  # Request moisture data
            time.sleep(0.5)
            moisture = self.ser.readline().decode().strip()
            self.get_logger().info(f"Soil Moisture: {moisture}")

            if moisture.isdigit() and int(moisture) > 800:
                self.ser.write(b'W')  # Trigger servo to water
                self.get_logger().info("Soil dry – Watering plant")
            else:
                self.get_logger().info("Soil moisture is adequate")
        except Exception as e:
            self.get_logger().error(f"Error reading from serial: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = PlantBot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
