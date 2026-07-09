from appliance import Appliance


class AirConditioner(Appliance):
    def __init__(self, appliance_id, name, power_rate, temperature):
        super().__init__(appliance_id, name, power_rate)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"AC temperature set to {self.temperature}°C.")

    def calculate_energy_usage(self):
        energy = self.get_power_rate() * self.get_usage_hours()

        if self.temperature < 22:
            energy = energy + (energy * 0.25)
        elif self.temperature > 26:
            energy = energy - (energy * 0.10)

        return energy

    def get_details(self):
        return super().get_details() + f" | Temperature: {self.temperature}°C"