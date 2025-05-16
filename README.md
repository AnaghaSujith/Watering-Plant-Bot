# UE22EC342BC2-Anagha_Kinnera-WateringPlantBot

Watering PlantBot with ROS2 and Arduino

A simple plant-watering system that uses **ROS 2 (Python)** and **Arduino UNO** via **serial communication**. The system reads soil moisture and activates a servo motor to water the plant if the soil is dry.

---

## Components Used

| Component              | Quantity |
|------------------------|----------|
| Arduino UNO            | 1        |
| Soil Moisture Sensor   | 1        |
| Servo Motor (SG90/MG90)| 1        |
| Jumper Wires           | As needed|


## Connections

### Soil Moisture Sensor (Analog type)
- **VCC** → 5V (Arduino)
- **GND** → GND (Arduino)
- **AO**  → A0 (Arduino)

### Servo Motor
- **Signal** → Arduino digital pin 9
- **VCC** → 5V
- **GND** → GND



## Arduino Code (`plant_bot_arduino.ino`)

 Listens over serial for:
   `R` → Reads and returns soil moisture
   `W` → Activates servo to water plant



## ROS 2 Python Node (`plant_bot_ros.py`)

 Sends `'R'` to Arduino every 5 seconds
 Reads the moisture value
 If value > 800, sends `'W'` to water the plant


## Files in This Repository

```text
plantbot/
├── plant_bot_ros        
├── plant_bot_Arduino    
├── video                
└── README.md              
```


## How to run

### 1. Upload Arduino Code
- Open `arduino_node.ino` in Arduino IDE.
- Select your board and COM port.
- Upload the code.

### 2. Connect via USB
- Plug Arduino into PC (usually `/dev/ttyUSB0` or `COMx`).

### 3. Run ROS 2 Node
```bash
source /opt/ros/<distro>/setup.bash
ros2 run plant_bot plant_bot_node


