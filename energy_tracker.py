# energy_tracker.py
from typing import List, Optional
from appliance import Appliance
from smart_fridge import SmartFridge
from air_conditioner import AirConditioner
from washing_machine import WashingMachine
from ev_charger import EVCharger

class EnergyTracker:
    def __init__(self):
        self.appliances: List[Appliance] = []
        self.electricity_rate = 8.0

    def add_default_appliances(self):
        self.appliances.append(SmartFridge(1, "Smart Fridge", 0.15, 4.0))
        self.appliances.append(AirConditioner(2, "Air Conditioner", 1.5, 24.0))
        self.appliances.append(WashingMachine(3, "Washing Machine", 0.5, "Normal"))
        self.appliances.append(EVCharger(4, "EV Charger", 7.0, 50.0))

    def show_all_appliances(self):
        print("\n============================== SMART HOME APPLIANCES ==============================")
        for appliance in self.appliances:
            details = getattr(appliance, "get_appliance_details", None)
            if callable(details):
                print(details())
            else:
                appliance_name = self.get_appliance_name(appliance)
                status = appliance.get_status() if hasattr(appliance, "get_status") else "Unknown"
                usage = appliance.get_usage_hours() if hasattr(appliance, "get_usage_hours") else 0.0
                print(f"{appliance_name} | {status} | {usage} hours")
        print("===================================================================================")

    def get_appliance_by_id(self, appliance_id: int) -> Optional[Appliance]:
        for appliance in self.appliances:
            if appliance.appliance_id == appliance_id:
                return appliance
        return None

    def get_appliance_name(self, appliance: Appliance) -> str:
        return getattr(appliance, "appliance_name", appliance.__class__.__name__)

    def turn_on_appliance(self, appliance_id: int):
        appliance = self.get_appliance_by_id(appliance_id)
        if appliance:
            appliance.turn_on()
            appliance_name = self.get_appliance_name(appliance)
            print(f"✔️ {appliance_name} is now turned ON.")
        else:
            print("❌ Error: Appliance ID not found.")

    def turn_off_appliance(self, appliance_id: int):
        appliance = self.get_appliance_by_id(appliance_id)
        if appliance:
            appliance.turn_off()
            appliance_name = self.get_appliance_name(appliance)
            print(f"✔️ {appliance_name} is now turned OFF.")
        else:
            print("❌ Error: Appliance ID not found.")

    def set_appliance_usage_hours(self, appliance_id: int, hours: float):
        appliance = self.get_appliance_by_id(appliance_id)
        if appliance:
            try:
                appliance.set_usage_hours(hours)
                appliance_name = self.get_appliance_name(appliance)
                print(f"✔️ Usage hours for {appliance_name} updated to {hours} hours.")
            except ValueError as e:
                print(f"❌ Error: {e}")
        else:
            print("❌ Error: Appliance ID not found.")

    def update_appliance_settings(self, appliance_id: int, new_value):
        appliance = self.get_appliance_by_id(appliance_id)
        if not appliance:
            print("❌ Error: Appliance ID not found.")
            return

        if isinstance(appliance, SmartFridge):
            appliance.set_temperature(new_value)
            appliance_name = getattr(appliance, "appliance_name", "Smart Fridge")
            print(f"✔️ Target temperature for {appliance_name} updated to {new_value}°C.")

        elif isinstance(appliance, AirConditioner):
            appliance.set_temperature(new_value)
            appliance_name = getattr(appliance, "appliance_name", "Air Conditioner")
            print(f"✔️ Temperature for {appliance_name} updated to {new_value}°C.")

        elif isinstance(appliance, WashingMachine):
            try:
                appliance.set_washing_mode(new_value)
                print(f"✔️ Washing mode for {appliance.appliance_name} updated to {appliance.washing_mode}.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif isinstance(appliance, EVCharger):
            try:
                appliance.set_battery_percentage(new_value)
                appliance_name = getattr(appliance, "appliance_name", "EV Charger")
                print(f"✔️ Connected EV Battery percentage for {appliance_name} updated to {new_value}%.")
            except ValueError as e:
                print(f"❌ Error: {e}")

    def calculate_total_energy_usage(self) -> float:
        total = 0.0
        for appliance in self.appliances:
            total += appliance.calculate_energy_usage()
        return total

    def estimate_electricity_bill(self) -> float:
        return self.calculate_total_energy_usage() * self.electricity_rate

    def show_energy_report(self):
        print("\n========================= ENERGY UTILIZATION REPORT =========================")
        print(f"{'Appliance Name':<20} | {'Status':<6} | {'Usage (Hrs)':<12} | {'Energy Usage (kWh)'}")
        print("---------------------------------------------------------------------------")
        for appliance in self.appliances:
            energy = appliance.calculate_energy_usage()
            name = getattr(appliance, "appliance_name", getattr(appliance, "name", "Unknown"))
            print(f"{name:<20} | {appliance.get_status():<6} | {appliance.get_usage_hours():<12.2f} | {energy:<18.2f}")
        print("---------------------------------------------------------------------------")
        total = self.calculate_total_energy_usage()
        bill = total * self.electricity_rate
        total_label = "TOTAL HOME ENERGY CONSUMPTION:"
        print(f"{total_label:<44} | {total:<18.2f} kWh")
        bill_label = f"ESTIMATED BILL (at ₹{self.electricity_rate:.2f}/kWh):"
        print(f"{bill_label:<44} | ₹{bill:<17.2f}")
        print("=============================================================================")

    def show_eco_suggestions(self):
        print("\n========== ECO SUGGESTIONS ==========")
        suggestions_found = False

        for appliance in self.appliances:
            if isinstance(appliance, AirConditioner):
                if appliance.temperature < 22.0:
                    print("Suggestion: Set AC temperature to 24°C to save energy.")
                    suggestions_found = True

            elif isinstance(appliance, SmartFridge):
                # SmartFridge may expose target temperature under different attribute names;
                # try common alternatives safely.
                fridge_temp = getattr(appliance, "target_temperature", None)
                if fridge_temp is None:
                    fridge_temp = getattr(appliance, "temperature", None)
                if fridge_temp is not None and fridge_temp < 3.0:
                    print("Suggestion: Increase fridge temperature to save power.")
                    suggestions_found = True

            elif isinstance(appliance, EVCharger):
                if appliance.battery_percentage > 80.0:
                    print("Suggestion: Stop EV charging after 80% to reduce power usage.")
                    suggestions_found = True

        total_energy = self.calculate_total_energy_usage()
        if total_energy > 20.0:
            print("Suggestion: Your energy usage is high. Reduce appliance usage hours.")
            suggestions_found = True

        if not suggestions_found:
            print("Good job! Your appliance settings are energy efficient.")