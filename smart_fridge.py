# smart_fridge.py
from appliance import Appliance

class SmartFridge(Appliance):
    """
    SmartFridge class inheriting from Appliance.
    Demonstrates:
    - Inheritance: Extends Appliance features.
    - Polymorphism: Overrides energy calculation and details representation.
    """
    appliance_id: int
    appliance_name: str
    target_temperature: float

    def __init__(self, appliance_id: int, appliance_name: str, power_consumption_rate: float, target_temperature: float = 4.0):
        super().__init__(appliance_id, appliance_name, power_consumption_rate)
        self.appliance_id = appliance_id
        self.appliance_name = appliance_name
        self.target_temperature = target_temperature

    def set_temperature(self, temperature: float):
        """Sets target temperature for the fridge."""
        self.target_temperature = temperature

    def calculate_energy_usage(self) -> float:
        """
        Overrides the base energy calculation.
        If target temperature is below 3.0°C, energy usage increases by 15%.
        """
        base_energy = super().calculate_energy_usage()
        if self.target_temperature < 3.0:
            return base_energy * 1.15
        return base_energy

    def get_appliance_details(self) -> str:
        """Overrides base details to include the fridge-specific target temperature."""
        base_details = super().get_appliance_details()
        return f"{base_details} | Target Temp: {self.target_temperature:>4.1f}°C"
