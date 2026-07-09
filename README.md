# Smart Eco-Home Energy Tracker 🌍🌱

An interactive console-based Object-Oriented Programming simulator written in Python. This simulator tracks, manages, and optimizes the electricity consumption of various smart home appliances, including a **Smart Fridge**, **Air Conditioner**, **Washing Machine**, and **EV Charger**. 

The project is structured to demonstrate core **Object-Oriented Programming (OOP)** principles: Classes & Objects, Encapsulation, Inheritance, and Polymorphism.

---

## 📖 Table of Contents
1. [Project Overview](#-project-overview)
2. [Key Features](#-key-features)
3. [Project Architecture](#-project-architecture)
4. [OOP Concepts Demonstrated](#-oop-concepts-demonstrated)
5. [Electricity & Cost Calculations](#-electricity--cost-calculations)
6. [Getting Started & Installation](#-getting-started--installation)
7. [Sample Usage Walkthrough](#-sample-usage-walkthrough)
8. [Troubleshooting & Editor Support](#-troubleshooting--editor-support)

---

## 📝 Project Overview

The **Smart Eco-Home Energy Tracker** mimics a modern smart home energy dashboard. Users can toggle appliances on and off, simulate usage hours, modify settings (like thermostat temperatures or washing modes), view a comprehensive breakdown of power usage, estimate electricity bills, and receive real-time, eco-friendly energy-saving suggestions.

This project is structured specifically to make the separation of concerns and OOP design principles clear and easily comprehensible, making it ideal for academic submissions, coding projects, or learning portfolios.

---

## 🚀 Key Features

- **Interactive Console Menu**: A user-friendly command loop that handles inputs and validates user parameters gracefully.
- **Dynamic Energy Calculation**: Computes energy usage based on active appliance status and custom settings.
- **Custom Appliance Configurations**:
  - **Smart Fridge**: Adapts its energy usage if target temperature falls below 3°C (+15% load).
  - **Air Conditioner**: Adjusts efficiency dynamically depending on whether it is run below 22°C (+25% load) or above 26°C (-10% load).
  - **Washing Machine**: Accounts for power multipliers across different washing modes (Quick: 80%, Normal: 100%, Heavy: 130%).
  - **EV Charger**: Regulates energy consumption based on current car battery level (Boost under 20%, Normal up to 80%, trickle charge/low load above 80%).
- **🌱 Eco Suggestions**: Generates real-time green alerts advising users on how they can modify settings (e.g. adjust AC/Fridge temperatures or charge status) to lower their bills and Carbon footprint.

---

## 📂 Project Architecture

```text
smart-eco-home-energy-tracker/
│
├── main.py                 # Application entrypoint & terminal menu controller
├── appliance.py            # Base Appliance class definitions
├── smart_fridge.py         # Subclass for fridge-specific calculations
├── air_conditioner.py      # Subclass for climate control calculations
├── washing_machine.py      # Subclass for cycle modes and multipliers
├── ev_charger.py           # Subclass for battery charging levels
├── energy_tracker.py       # Manager class aggregating appliances
├── README.md               # Project documentation and guide
└── .gitignore              # Ignores byte-caches and local folders
```

### File Responsibilities

1. **`appliance.py`**:
   Contains the base class `Appliance`. Declares core private variables (`__power_consumption_rate`, `__status`, and `__usage_hours`) and exposes public methods (`turn_on()`, `turn_off()`, getter and setter methods).
2. **`smart_fridge.py`**:
   Implements `SmartFridge` inheriting from `Appliance`. Manages the fridge target temperature and implements custom energy scaling.
3. **`air_conditioner.py`**:
   Implements `AirConditioner` inheriting from `Appliance`. Governs temperature-dependent climate loads.
4. **`washing_machine.py`**:
   Implements `WashingMachine` inheriting from `Appliance`. Governs washing cycle multipliers (Quick, Normal, Heavy).
5. **`ev_charger.py`**:
   Implements `EVCharger` inheriting from `Appliance`. Governs battery-level charging behavior.
6. **`energy_tracker.py`**:
   Implements the container class `EnergyTracker` to manage lists of appliances, aggregate total load calculations, output reports, and compile green suggestions.
7. **`main.py`**:
   Runs the interactive program loop, displays the command menu, collects user values, validates types safely, and interfaces with the tracker.

---

## 📐 OOP Concepts Demonstrated

### 1. Classes and Objects
Classes serve as blueprints for objects. The base class `Appliance` is a blueprint, and individual appliances (like the `SmartFridge` or `AirConditioner` instances) are concrete objects with discrete properties.
```python
# Instantiating concrete objects from classes
tracker.appliances.append(SmartFridge(1, "Smart Fridge", 0.15, 4.0))
tracker.appliances.append(AirConditioner(2, "Air Conditioner", 1.5, 24.0))
```

### 2. Encapsulation
Important data is kept secure using private variables (prefixed with `__` in Python). Subclasses and external controllers cannot alter the appliance status, power rate, or usage hours directly. Instead, they must invoke interface methods such as `set_usage_hours()`, `turn_on()`, or `get_power_rate()`.
```python
# Encapsulation inside appliance.py
class Appliance:
    def __init__(self, appliance_id: int, appliance_name: str, power_consumption_rate: float):
        self.appliance_id = appliance_id
        self.appliance_name = appliance_name
        self.__status = False       # Encapsulated state (private)
```

### 3. Inheritance
Reusability is achieved through class hierarchy. Subclasses like `SmartFridge` and `EVCharger` inherit common properties and methods (`turn_on()`, `turn_off()`, `set_usage_hours()`) from the parent `Appliance` class.
```python
# Inheritance syntax in smart_fridge.py
class SmartFridge(Appliance):
    def __init__(self, appliance_id: int, appliance_name: str, ...):
        super().__init__(appliance_id, appliance_name, power_consumption_rate)
```

### 4. Polymorphism
The base class `Appliance` defines the interfaces `calculate_energy_usage()` and `get_appliance_details()`. Each child class overrides these methods to execute specialized logic. When `EnergyTracker` compiles reports, it iterates over all appliances and calls these methods polymorphically:
```python
# Polymorphic execution
for appliance in self.appliances:
    # Resolves dynamically to SmartFridge, AirConditioner, or EVCharger implementation
    energy = appliance.calculate_energy_usage() 
```

---

## ⚡ Electricity & Cost Calculations

- **Total Consumption Formula**: 
  $$\text{Energy Usage (kWh)} = \text{Power Rating (kW)} \times \text{Usage Hours (h)} \times \text{Multiplier (Subclass Condition)}$$
- **Billing Rate**: Default electricity rate is **₹8.00 per kWh**.
- **Estimated Bill**: 
  $$\text{Total Bill (₹)} = \text{Total Consumption (kWh)} \times \text{Electricity Rate}$$

---

## 💻 Getting Started & Installation

### 1. Prerequisites
Verify Python 3 is installed in your system:
```bash
python --version
```

### 2. Run the Application
Navigate to the project directory and execute the runner script:
```bash
python main.py
```

---

## 📊 Sample Usage Walkthrough

### 1. Show All Appliances (Option 1)
```text
============================== SMART HOME APPLIANCES ==============================
ID: 1 | Name: Smart Fridge     | Status: OFF | Power Rate: 0.15 kW | Usage:  0.00 hrs | Target Temp:  4.0°C
ID: 2 | Name: Air Conditioner  | Status: OFF | Power Rate:  1.5 kW | Usage:  0.00 hrs | AC Temp: 24.0°C
ID: 3 | Name: Washing Machine  | Status: OFF | Power Rate:  0.5 kW | Usage:  0.00 hrs | Cycle Mode: Normal
ID: 4 | Name: EV Charger       | Status: OFF | Power Rate:  7.0 kW | Usage:  0.00 hrs | Connected EV Battery:  50.0%
===================================================================================
```

### 2. Show Energy Report (Option 6)
```text
========================= ENERGY UTILIZATION REPORT =========================
Appliance Name       | Status | Usage (Hrs)  | Energy Usage (kWh)
---------------------------------------------------------------------------
Smart Fridge         | ON     | 10.00        | 1.72              
Air Conditioner      | ON     | 5.00         | 9.38              
Washing Machine      | ON     | 2.00         | 1.30              
EV Charger           | ON     | 4.00         | 23.80             
---------------------------------------------------------------------------
TOTAL HOME ENERGY CONSUMPTION:               | 36.20              kWh
ESTIMATED BILL (at ₹8.00/kWh):               | ₹289.60           
=============================================================================
```

---

## 🛠️ Troubleshooting & Editor Support

### UTF-8 Terminal Encoding
To allow printing checkmarks (`✔️`) and leaves (`🌍🌱`) cleanly on Windows Command Prompt/PowerShell, the system automatically configures output streaming to UTF-8:
```python
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
```

### Pylance Type-Checking Warnings
If you see static type warnings in VS Code (Pylance/Pyright):
- All class fields (`appliance_id`, `appliance_name`, and subclass properties) are declared at the class level and fully initialized.
- If your editor cache is out-of-sync, open the Command Palette (`Ctrl+Shift+P`) and choose **`Developer: Reload Window`** or **`Python: Restart Language Server`** to reload type definitions.
