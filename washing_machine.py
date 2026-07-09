# washing_machine.py
from appliance import Appliance

class WashingMachine(Appliance):
    """
    WashingMachine class inheriting from Appliance.
    Demonstrates:
    - Inheritance: Extends Appliance features.
    - Polymorphism: Overrides energy calculation and details representation.
    """
    appliance_id: int
    appliance_name: str
    washing_mode: str

    def __init__(self, appliance_id: int, appliance_name: str, power_consumption_rate: float, washing_mode: str = "Normal"):
        super().__init__(appliance_id, appliance_name, power_consumption_rate)
        self.appliance_id = appliance_id
        self.appliance_name = appliance_name
        self.washing_mode = washing_mode.strip().capitalize()
        if self.washing_mode not in ["Quick", "Normal", "Heavy"]:
            self.washing_mode = "Normal"

    def set_washing_mode(self, mode: str):
        """Sets the washing mode for the washing machine."""
        mode_formatted = mode.strip().capitalize()
        if mode_formatted not in ["Quick", "Normal", "Heavy"]:
            raise ValueError("Washing mode must be Quick, Normal, or Heavy.")
        self.washing_mode = mode_formatted

    def calculate_energy_usage(self) -> float:
        """
        Overrides the base energy calculation.
        - Quick mode: 80% energy consumption.
        - Normal mode: 100% energy consumption.
        - Heavy mode: 130% energy consumption.
        """
        base_energy = super().calculate_energy_usage()
        if self.washing_mode == "Quick":
            return base_energy * 0.80
        elif self.washing_mode == "Heavy":
            return base_energy * 1.30
        else:
            return base_energy

    def get_appliance_details(self) -> str:
        """Overrides base details to include washing-machine-specific cycle mode."""
        base_details = super().get_appliance_details()
        return f"{base_details} | Cycle Mode: {self.washing_mode}"
