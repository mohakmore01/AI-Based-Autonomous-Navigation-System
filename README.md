# 🚗 AI-Based Autonomous Navigation System (Advanced)

## 📌 Overview

This project implements an **AI-Based Autonomous Navigation System** that combines **Computer Vision (YOLO)** and **Path Planning (A*)** to enable a virtual robot/vehicle to navigate autonomously in an environment with obstacles.

The system detects real-world objects using a camera, converts them into a navigable grid, and computes the optimal path using intelligent algorithms.

---

## 🎯 Problem Statement

Autonomous systems must safely navigate environments without human intervention. This project demonstrates how AI can:

* Detect obstacles in real-time
* Understand surroundings
* Plan optimal paths
* Avoid collisions

---

## 🌍 Industry Relevance

This project simulates core technologies used in:

* Self-driving cars (Tesla, Waymo)
* Warehouse robots (Amazon Robotics)
* Delivery robots and drones
* Industrial automation systems

---

## 🧠 Key Features

* 🎥 Real-time camera input
* 🧍 Object detection using YOLO
* 🧩 Grid-based environment mapping
* 📍 A* path planning algorithm
* 🚦 Obstacle avoidance
* 🖥️ Interactive simulation using Pygame

---

## 🛠️ Tech Stack

* Python
* OpenCV
* NumPy
* Pygame

---

## 📁 Folder Structure

```
AI-Autonomous-Navigation-System/
├── image/          # Contains layout.png and demo screenshots
├── src/            # Core logic (vision, simulation, astar)
│   │── __pycache__
│   └──  astar.py
├── main.py         # Main entry point to run the system
└── README.md       # Project documentation
```

---

## ⚙️ Installation

### 1. Clone Repository

```
git clone https://github.com/your-username/AI-Autonomous-Navigation-System.git
cd AI-Autonomous-Navigation-System
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

---

## ▶️ How to Run

```
python main.py
```

## 🧪 Results

### 🔹 Object Detection

### 🔹 Grid Mapping

![Grid](images/layout.png)

### 🔹 Final Path Planning

![Path](images/final_path.png)

---


## 🚀 Future Improvements

* Integration with ROS
* CARLA simulator support
* Lane detection system
* Reinforcement learning for navigation
* Multi-agent navigation
* Real robot deployment (Raspberry Pi / Jetson Nano)

---

## 📚 Learning Outcomes

* Understanding of autonomous systems pipeline
* Implementation of A* algorithm
* Hands-on with OpenCV and YOLO
* Simulation-based testing
* GitHub project structuring

---

## 💼 Resume Highlights

* Developed AI-based navigation system using YOLO and A*
* Implemented real-time obstacle detection and path planning
* Designed simulation environment for autonomous movement

---

## 👨‍💻 Author

**Mohak Rajendra More**
🎓 Pursuing a Degree in Mechatronics Engineering

---

## ⭐ If you found this useful, give it a star!
