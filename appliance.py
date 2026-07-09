# appliance.py

class Appliance:
    """
    Base class representing a general household appliance.
    Demonstrates:
    - Encapsulation: Keeping important data private with getter and setter methods.
    """
    appliance_id: int = 0
    appliance_name: str = ""

    def __init__(self, appliance_id: int, appliance_name: str, power_consumption_rate: float):
        self.appliance_id = appliance_id
        self.appliance_name = appliance_name
        
        # Encapsulated private attributes (prefixed with __ to make them private in Python)
        self.__power_consumption_rate = power_consumption_rate  # in kW
        self.__status = False                                   # False: OFF, True: ON
        self.__usage_hours = 0.0                                # in hours

    def turn_on(self):
        """Turns the appliance ON."""
        self.__status = True

    def turn_off(self):
        """Turns the appliance OFF."""
        self.__status = False

    def get_status(self) -> str:
        """Returns the status of the appliance as a string ('ON' or 'OFF')."""
        return "ON" if self.__status else "OFF"

    def is_on(self) -> bool:
        """Helper method to check if the appliance is currently ON (returns True/False)."""
        return self.__status

    def set_usage_hours(self, hours: float):
        """Sets the usage hours. Includes input validation to prevent negative values."""
        if hours < 0:
            raise ValueError("Usage hours cannot be negative.")
        self.__usage_hours = hours

    def get_usage_hours(self) -> float:
        """Returns the usage hours."""
        return self.__usage_hours

    def get_power_rate(self) -> float:
        """Returns the power consumption rate in kW."""
        return self.__power_consumption_rate

    def calculate_energy_usage(self) -> float:
        """
        Calculates energy usage in kilowatt-hours (kWh).
        Energy (kWh) = Power (kW) * Time (hours).
        Energy is only consumed if the appliance is turned ON.
        """
        if not self.__status:
            return 0.0
        return self.__power_consumption_rate * self.__usage_hours

    def get_appliance_details(self) -> str:
        """Returns a formatted string containing basic details of the appliance."""
        return (f"ID: {self.appliance_id} | Name: {self.appliance_name:<16} | "
                f"Status: {self.get_status():<3} | Power Rate: {self.__power_consumption_rate:>4} kW | "
                f"Usage: {self.__usage_hours:>5.2f} hrs")
