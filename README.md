# UE22EC342BC2-Anagha_Kinnera-WateringPlantBot

Watering PlantBot with ROS2 and Arduino

A simple plant-watering system that uses **ROS 2 (Python)** and **Arduino** via **serial communication**. The system reads soil moisture and activates a servo motor to water the plant if the soil is dry.

---

## 🧰 Components Used

| Component              | Quantity |
|------------------------|----------|
| Arduino UNO/Nano       | 1        |
| Soil Moisture Sensor   | 1        |
| Servo Motor (SG90/MG90)| 1        |
| Jumper Wires           | As needed|
| USB Cable              | 1        |
| Computer with ROS 2 installed | 1 |



## Connections

### Soil Moisture Sensor (Analog type)
**VCC** → 5V (Arduino)
**GND** → GND (Arduino)
**AO**  → A0 (Arduino)

### Servo Motor
**Signal** → D9 (Arduino pin 9)
**VCC** → 5V (use external power supply if needed)
**GND** → GND (shared with Arduino)



##  Arduino Code (`plant_bot_arduino.ino`)

 Listens over serial for:
   `R` → Reads and returns soil moisture
   `W` → Activates servo to water plant



##  ROS 2 Python Node (`plant_bot_ros.py`)

 Sends `'R'` to Arduino every 5 seconds
 Reads the moisture value
 If value > 800, sends `'W'` to water the plant



##  How to Run

### 1. Upload Arduino Sketch
- Open `plant_bot_arduino.ino` in Arduino IDE
- Select board and port, then upload

### 2. Run ROS 2 Node
- Make sure ROS 2 workspace is sourced:
  ```bash
  source /opt/ros/<your_ros_distro>/setup.bash
