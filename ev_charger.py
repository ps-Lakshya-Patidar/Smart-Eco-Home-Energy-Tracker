from appliance import Appliance


class EVCharger(Appliance):
    def __init__(self, appliance_id, name, power_rate, battery_percentage):
        super().__init__(appliance_id, name, power_rate)
        self.battery_percentage = battery_percentage

    def set_battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.battery_percentage = battery_percentage
            print(f"EV battery percentage set to {self.battery_percentage}%.")
        else:
            print("Battery percentage must be between 0 and 100.")

    def calculate_energy_usage(self):
        energy = self.get_power_rate() * self.get_usage_hours()

        if self.battery_percentage < 20:
            energy = energy + (energy * 0.20)
        elif self.battery_percentage > 80:
            energy = energy - (energy * 0.15)

        return energy

    def get_details(self):
        return super().get_details() + f" | Battery: {self.battery_percentage}%"